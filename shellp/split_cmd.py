import shlex
import os


def modify_arg(arg):
	arg = os.path.expanduser(arg)
	return arg


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
