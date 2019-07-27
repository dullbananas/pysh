'''Contains utilities used by ShellP

This module contains miscelaneous functions that are used by various tools in
ShellP.
'''

import sys
import os
import pathlib
import importlib
import itertools
from . import nothing


home_dir = pathlib.Path.home()
shellp_dir = os.path.join(home_dir, '.shellp')


def dot_shellp(name):
	'''Imports script from ~/.shellp
	
	This function imports a module from the user's .shellp directory and returns
	the module. If the module has been modified, then those changes will take
	place, sine this function reloads the module before returning it.
	
	Args:
		name: The name of the module.
		
	Returns:
		The module if it exists, or an empty module if it doesn't.
	'''
	
	if shellp_dir not in sys.path:
		sys.path.insert(0, shellp_dir)
	
	try:
		module = importlib.import_module(name)
		importlib.reload(module)
	except ImportError:
		module = nothing
	
	sys.path.remove(shellp_dir)
	return module


def filter_roles(funcs, role):
	def check(func):
		if 'role' in dir(func):
			if func.role == role:
				return True
		return False
	return filter(check, funcs)


def split_list(l, condition):
	groupby = itertools.groupby(l, condition)
	return [list(group) for k, group in groupby if not k]


def debug(obj):
	from .options import options
	if options['debug']:
		print(obj)
