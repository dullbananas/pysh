'''Importer for user config and extensions'''

import importlib
import sys
import os
from . import utils


def load_config(defaults, path='~/.shellp'):
	# Initialize result with default config
	result = defaults
	
	# Prepare for importing
	importlib.invalidate_caches()
	sys.path.insert(0, os.path.expanduser(path))
	
	# Import ~/.shellp/config.py
	try:
		user_config = importlib.import_module('config').__dict__
	except ImportError:
		user_config = {}
	# Merge user config into result
	result = {**result, **user_config}
	
	# Import extensions
	for ext_name in result['extensions']:
		try:
			ext = importlib.import_module(ext_name).__dict__
			result = {**result, **ext}
		except ImportError:
			utils.error(f'extension "{ext_name}" not found')
	
	# Organize classes
	classes = filter((lambda x: isinstance(x, type)), result.items())
	for cls in classes:
		# Get name of parent class
		try:
			parent_name = cls.__bases__[0].__name__
		except IndexError:
			# Ignore class if it doesn't have a parent
			continue
		# Make sure that result[parent_name] exists
		try:
			result[parent_name]
		except NameError:
			result[parent_name] = []
		# Append class th result[parent_name]
		result[parent_name].append(cls)
		
	# Remove ~/.shellp from sys.path
	sys.path.pop(0)
	# Return the resulting dictionary
	return result
