'''Defines builtin commands'''

from .cmd_funcs import command
from . import utils, options
import os
import sys
import builtins


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
	expr = args[1]
	print(builtins.eval(expr))


@command
def reload(args):
	options.load_config()
	print('User config reloaded')
