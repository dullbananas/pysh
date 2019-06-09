'''Main script'''


def main():
	from .options import options
	from sys import exit
	from .parse_prompt import parse_prompt
	from os import system
	
	while True:
		try:
			cmd = input(parse_prompt(options['ps1'] + '{style.clear}'))
		except (EOFError, KeyboardInterrupt):
			print('\nType "exit" to exit ShellP.')
		
		else:
			if cmd == 'exit':
				exit(0)
			else:
				system(cmd)


def run():
	from .__init__ import __version__
	print('Starting ShellP {}...'.format(__version__))
	main()


if __name__ == '__main__':
	run()
