'''Main script'''


import atexit
import os
@atexit.register
def reset_term():
	os.system('stty sane')


def main():
	elapsed = 0
	
	from .options import options
	import sys
	import os
	from .parse_prompt import parse_prompt
	import time
	import subprocess
	import traceback
	
	from timeoutcontext import timeout
	from prompt_toolkit import PromptSession, ANSI
	from prompt_toolkit.lexers import PygmentsLexer
	from prompt_toolkit.styles.pygments import style_from_pygments_cls
	from prompt_toolkit.history import FileHistory
	from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
	
	from pygments.lexers.shell import BashLexer
	from pygments.styles import get_style_by_name
	
	from . import builtin_commands, utils, run_pipes, split_cmd
	
	# Create history file
	open(os.path.expanduser('~/.shellp/history'), 'a').close()
	
	# Initialize PromptSession object
	psession = PromptSession(
		lexer=PygmentsLexer(BashLexer),
		include_default_pygments_style=False,
		history=FileHistory(os.path.expanduser('~/.shellp/history')),
		mouse_support=True,
		auto_suggest=AutoSuggestFromHistory(),
	)
	
	while True:
		# get input from user
		try:
			prompt = parse_prompt(options['ps1'], exec_time=round(elapsed,1))
			prompt = ANSI(prompt)
			highlight_style = style_from_pygments_cls(get_style_by_name(options['highlight_style']))
			with timeout(options['timeout']):
				try:
					cmd = psession.prompt(prompt, style=highlight_style)
				except KeyError:
					# Make sure that the terminal doesn't get messed up on timeout
					sys.exit()
			
			# Get individual arguments of the inputted command
			cmd = split_cmd.split_cmd(cmd)
			#print(cmd)
			if cmd == []:
				continue
		except KeyboardInterrupt:
			print()
		except EOFError:
			print('exit')
			sys.exit(0)
		except TimeoutError:
			print('\nTimeout exceeded ({} seconds)'.format(options['timeout']))
		except ValueError as e:
			print('Invalid command: '+str(e))
		
		else:
			if options['debug']:
				print(cmd)
			start_time = time.time()
			try:
				# run builtin command
				for func in utils.filter_roles(builtin_commands.__dict__.values(), 'cmd_func'):
					if cmd[0] == func.name:
						func(cmd)
						break
				
				# run command
				else:
					try:
						if '|' in cmd:
							pipeline = split_cmd.split_pipes(cmd)
							utils.debug(pipeline)
							run_pipes.run_pipeline(pipeline)
						else:
							proc = subprocess.Popen(cmd)
							proc.communicate() # Wait until command finishes
					except OSError as e:
						print(f'OSError {e.errno}: {e.strerror}')
			except Exception:
				print(traceback.format_exc())
				poop = input('Do you want to exit ShellP? (y/n) ')
				if poop == 'y':
					sys.exit(1)
			elapsed = time.time() - start_time


def run():
	from .__init__ import __version__
	print('Starting ShellP {}'.format(__version__))
	main()


if __name__ == '__main__':
	run()
