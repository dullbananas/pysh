'''Main script'''
from .__init__ import __version__
if __name__ == '__main__':
	print('Starting ShellP version {}'.format(__version__))

#import beautiful_ansi as style
from .options import options
import sys
from .parse_prompt import parse_prompt
import os


def main():
	while True:
		cmd = input(parse_prompt(options['ps1']))
		
		if cmd == 'exit':
			sys.exit(0)
		else:
			os.system(cmd)


def run():
	main()


if __name__ == '__main__':
	run()
