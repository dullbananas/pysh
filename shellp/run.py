'''Main script'''


def main():
	from .options import options, load_config
	import sys
	from .parse_prompt import parse_prompt
	from os import system, chdir, path
	from pathlib import Path
	from select import select
	
	while True:
		# get input from user
		try:
			prompt = parse_prompt(options['ps1'] + '{style.clear}')
			if options['timeout'] == 0:
				cmd = input(prompt)
			else:
				print(prompt, end='')
				i, _, _ = select([sys.stdin], [], [], float(options['timeout']))
				if i:
					cmd = sys.stdin.readline().strip()
				else:
					print('\nTimeout exceded ({} seconds)'.format(options['timeout']))
					sys.exit(0)
				del i
		except (EOFError, KeyboardInterrupt):
			print('\nType "exit" to exit ShellP.')
		
		else:
			try:
				# exit ShellP
				if cmd == 'exit':
					sys.exit(0)
				# cd to home directory
				elif cmd == 'cd':
					chdir(Path.home())
				# cd to custom dir
				elif cmd.startswith('cd '):
					path_ = cmd[3:]
					if path_[0] == '~':
						path_ = path.join(Path.home(), path_[2:])
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
				elif cmd.startswith('eval:'):
					statement = cmd[5:].replace('\\n', '\n')
					print(eval(statement))
				# reload user config
				elif cmd == 'reload':
					load_config()
					print('User config reloaded')
				# run command
				else:
					system(cmd)
			except Exception as e:
				print('unexpected error: ' + repr(e))


def run():
	from .__init__ import __version__
	print('Starting ShellP {}...'.format(__version__))
	main()


if __name__ == '__main__':
	run()
