'''Main script'''


def main():
	from .options import options
	from sys import exit
	from .parse_prompt import parse_prompt
	from os import system, chdir
	from os.path import abspath
	
	while True:
		try:
			cmd = input(parse_prompt(options['ps1'] + '{style.clear}'))
		except (EOFError, KeyboardInterrupt):
			print('\nType "exit" to exit ShellP.')
		
		else:
			if cmd == 'exit':
				exit(0)
			elif cmd.startswith('cd '):
				chdir(abspath(cmd[3:]))
			else:
				system(cmd)


def run():
	from .__init__ import __version__
	print('Starting ShellP {}...'.format(__version__))
	main()


if __name__ == '__main__':
	run()
