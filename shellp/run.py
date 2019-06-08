'''Main script'''
from .__init__ import __version__
if __name__ == '__main__':
	print('Starting ShellP version {}'.format(__version__))

#import beautiful_ansi as style
from .options import options
import sys
from .parse_prompt import parse_prompt
import os
#import subprocess


def main():
	while True:
		try:
			cmd = input(parse_prompt(options['ps1']))
		except (EOFError, KeyboardInterrupt):
			print('\nType "exit" to exit ShellP.')
		
		else:
			if cmd == 'exit':
#				print('Exiting ShellP...')
				sys.exit(0)
			else:
				os.system(cmd)


def run():
	main()


if __name__ == '__main__':
	run()
