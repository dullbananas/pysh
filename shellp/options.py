# Import .shellp/config.py from user directory
import sys
import pathlib
import os
import importlib

def import_config():
	global config
	shellp_dir = os.path.join(pathlib.Path.home(), '.shellp')
	if sys.path[0] != shellp_dir:
		sys.path.insert(0, shellp_dir)
	try:
		import config
	except ImportError:
		config = None

# Define the default options
options = {
	'ps1': '{time["%H:%M:%S"]} {style.yellow}{cwd} {git_branch} {style.bold}{style.lightgreen}{symbol} ',
	'ps2': '{style.yellow}> ',
	'timeout': 0,
}

# Load options from config.py if it exists
def set_config():
	global config
	if config is not None and '--no-user-config' not in sys.argv and '-U' not in sys.argv:
		for key, val in config.__dict__.items():
			# If the option type is a set, then merge the user's option with the default one
			if isinstance(val, set) and key in options.keys():
				options[key] = options[key] | val
			else:
				options[key] = val

def load_config():
	import_config()
	if config is not None:
		importlib.reload(config)
	set_config()

load_config()
