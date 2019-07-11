'''Main script'''


def main():
	elapsed = 0
	
	from .options import options
	import sys
	from .parse_prompt import parse_prompt
	from .read_cmd import read_cmd
	import time
	import subprocess
	import traceback
	from . import builtin_commands, utils, run_pipes, split_cmd
	
	while True:
		# get input from user
		try:
			prompt = parse_prompt(options['ps1'], exec_time=round(elapsed,1))
			cmd = read_cmd(prompt, options['timeout'])
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
