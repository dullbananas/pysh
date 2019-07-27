import shlex
import os
from .options import options
from . import utils


def modify_arg(arg):
	result = arg
	
	if arg.startswith('$$'):
		result = options['arg_funcs'][arg[2:]]()
	elif arg.startswith('$'):
		result = os.getenv(arg[1:], 'OH F**K THAT ENVIRONMENT VARIABLE DOESN\'T EXIST')
	
	result = str(result)
	result = os.path.expanduser(result)
	return result


def split_cmd(cmd):
	cmd = shlex.split(cmd)
	if len(cmd) == 0:
		return []
	cmd = replace_alias(cmd, options['aliases'])
	return [modify_arg(arg) for arg in cmd]


def replace_alias(cmd, aliases):
	for alias, replacement in aliases.items():
		if cmd[0] == alias:
			try:
				cmd = shlex.split(replacement) + cmd[1:]
			except IndexError:
				cmd = shlex.split(replacement)
			break
	return cmd


def split_pipes(cmd):
	result = utils.split_list(cmd, (lambda x: x == '|'))
	#result = [replace_alias(i, aliases) for i in result]
	
	return result
