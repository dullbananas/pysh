'''Main script'''


# Prevent terminal from breaking if ShellP exits while prompting for user input
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
	
	import prompt_toolkit
	from prompt_toolkit import ANSI
	from prompt_toolkit.lexers import PygmentsLexer
	from prompt_toolkit.styles.pygments import style_from_pygments_cls
	from prompt_toolkit.history import FileHistory
	from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
	
	from pygments.lexers.shell import BashLexer
	from pygments.styles import get_style_by_name
	
	from . import builtin_commands, utils, run_pipes, split_cmd
	
	# Create history file
	histfile = os.path.expanduser('~/.shellp/history')
	open(os.path.expanduser(histfile), 'a').close()
	
	# Initialize PromptSession object
	psession = prompt_toolkit.PromptSession(
		lexer=PygmentsLexer(BashLexer),
		include_default_pygments_style=False,
		history=FileHistory(histfile),
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
					# prompt_toolkit raises KeyError when the timeout exceeds
					sys.exit(0)
			
			# Get individual arguments of the inputted command
			cmd = split_cmd.split_cmd(cmd)
			
			# Ignore empty command
			if cmd == []:
				continue
		except KeyboardInterrupt:
			print()
		except EOFError:
			sys.exit(0)
		except TimeoutError:
			print('\nTimeout exceeded ({} seconds)'.format(options['timeout']))
		except ValueError as e:
			print('Invalid command: '+str(e))
		
		# Run command
		else:
			if options['debug']:
				print(cmd)
			start_time = time.time()
			# run builtin command
			builtin_funcs = utils.filter_roles(builtin_commands.__dict__.values(), 'cmd_func')
			for func in filter((lambda x: x.name == cmd[0]), builtin_funcs):
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
			elapsed = time.time() - start_time


def run():
	from .__init__ import __version__
	print('Starting ShellP {}'.format(__version__))
	main()


if __name__ == '__main__':
	run()
