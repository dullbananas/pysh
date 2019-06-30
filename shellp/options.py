# Import .shellp/config.py from user directory
import sys
import pathlib
import os
import importlib
from .parse_bash_aliases import parse_files as parse_aliases

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
	'aliases': {},
	'bash_alias_files': [],
	'debug': False,
	'env_lists': {},
	'env_vars': {},
	'ps1': '{time["%H:%M:%S"]} {user}@{hostname} {style.yellow}{cwd} {git_branch} {style.bold}{style.lightgreen}{symbol} ',
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
	# Load bash aliases
	options['aliases'] = {**parse_aliases(options['bash_alias_files']), **options['aliases']}
	# Load environment variables
	os.environ = {**os.environ, **options['env_vars']}
	# Load environment lists
	for name in options['env_lists'].keys():
		value_set = options['env_lists'][name] # The list/tuple/etc. of values to be joined by colons
		try:
			if not os.environ[name].startswith(':'):
				os.environ[name] = ':' + os.environ[name]
		except KeyError:
			os.environ[name] = ''
		os.environ[name] = ':'.join(value_set) + os.environ[name]

def load_config():
	import_config()
	if config is not None:
		importlib.reload(config)
	set_config()

load_config()
