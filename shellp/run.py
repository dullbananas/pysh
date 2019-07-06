'''Main script'''


def main():
	elapsed = 0
	
	from .options import options, load_config
	import sys
	from .parse_prompt import parse_prompt
	from .split_cmd import split_cmd
	from .read_cmd import read_cmd
	from os import chdir, path
	from pathlib import Path
	import time
	import subprocess
	import traceback
	
	while True:
		# get input from user
		try:
			prompt = parse_prompt(options['ps1'], exec_time=round(elapsed,1))
			cmd = read_cmd(prompt, options['timeout'])
			# Get individual arguments of the inputted command
			cmd = split_cmd(cmd, options['aliases'])
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
				# exit ShellP
				if cmd[0] == 'exit':
					sys.exit(0)
				# cd to home directory
				elif cmd == ['cd']:
					chdir(Path.home())
				# cd to custom dir
				elif cmd[0] == 'cd':
					path_ = cmd[1]
					try:
						chdir(path.abspath(path_))
					except FileNotFoundError:
						if path_ == '--help':
							print('cd: usage: cd [dir]')
						else:
							print('cd: no such file or directory')
					except NotADirectoryError:
						print('cd: specified path is not a directory')
				# eval python statement
				elif cmd[0] == 'eval':
					print(eval(cmd[1]))
				# reload user config
				elif cmd[0] == 'reload':
					load_config()
					print('User config reloaded')
				# run command
				else:
					try:
						proc = subprocess.Popen(cmd)
						proc.communicate() # Wait until command finishes
					except OSError as e:
						print(f'Error {e.errno}: {e.strerror}')
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
