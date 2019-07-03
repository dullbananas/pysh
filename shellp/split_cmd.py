import shlex
import os
from .options import options


def modify_arg(arg):
	result = arg
	
	if arg.startswith('$$'):
		result = options['arg_funcs'][arg[2:]]()
	elif arg.startswith('$'):
		result = os.getenv(arg[1:], 'OH F**K THAT ENVIRONMENT VARIABLE DOESN\'T EXIST')
	
	result = str(result)
	result = os.path.expanduser(result)
	return result


def split_cmd(cmd, aliases=None):
	if aliases == None:
		aliases = {}
	cmd = shlex.split(cmd)
	if len(cmd) == 0:
		return []
	for alias, replacement in aliases.items():
		if cmd[0] == alias:
			try:
				cmd = shlex.split(replacement) + cmd[1:]
			except IndexError:
				cmd = shlex.split(replacement)
			break
	return [modify_arg(arg) for arg in cmd]
