from .cmd_funcs import command
from . import utils, options
import os
import sys


@command
def exit(args):
	sys.exit(0)


@command
def cd(args):
	if args == ['cd']:
		os.chdir(utils.home_dir)
	else:
		os.chdir(args[1])


@command
def eval(args):
	print(eval(args[1]))


@command
def reload(args):
	options.load_config()
	print('User config reloaded')
