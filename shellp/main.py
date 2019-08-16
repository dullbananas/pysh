from .__init__ import __version__
from .interpreter import Interpreter
import sys


def main(interactive, use_user_config):
	if interactive:
		print(f'ShellP version {__version__}')
	
	interpreter = Interpreter()
	
	if not interactive:
		while True:
			line = sys.stdin.readline()
			if line == '':
				return 0
			else:
				interpreter.feed_line(line[:-1])
	
	while True:
		try:
			if interactive:
				prompt = '$ '
			else:
				prompt = ''
			cmd = input(prompt)
			interpreter.feed_line(cmd)
		except EOFError:
			sys.exit(0)
