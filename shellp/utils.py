import sys


def error(text, **kwargs):
	print(f'Error: {text}', file=sys.stderr, **kwargs)


def read_file(filename):
	with open(filename) as f:
		return f.read()
