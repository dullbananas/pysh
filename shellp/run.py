'''Main script'''


def main():
	from .options import options
	from sys import exit
	from .parse_prompt import parse_prompt
	from os import system, chdir
	from os import path
	from pathlib import Path
	
	while True:
		try:
			cmd = input(parse_prompt(options['ps1'] + '{style.clear}'))
		except (EOFError, KeyboardInterrupt):
			print('\nType "exit" to exit ShellP.')
		
		else:
			try:
				if cmd == 'exit':
					exit(0)
				elif cmd == 'cd':
					chdir(Path.home())
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
