from . import importer, utils
from .parse_bash import parse_aliases
import os


defaults = {
	'aliases': {},
	'arg_funcs': {},
	'bash_alias_files': [],
	'debug': False,
	'env_lists': {},
	'env_vars': {},
	'extensions': [],
	'highlight_style': 'monokai',
	'ps1': '\n{lightgreen}{symbol} ',
	'ps2': '{lightblue}> ',
	'timeout': 0,
}


options = {}
def load_options():
	# Load options dictionary
	global options, original_env
	options = importer.load_config(defaults)
	
	# Load env_vars
	os.environ = {**os.environ, **options['env_vars']}
	
	# Load env_lists
	for name, values in options['env_lists'].items():
		if name in os.environ:
			current_values = os.environ[name].split(':')
			values = filter((lambda x: x not in current_values), values)
			os.environ[name] = ':'.join(values + current_values)
	
	# Load bash aliases
	for filename in options['bash_alias_files']:
		try:
			script = utils.read_file(filename)
		except OSError:
			utils.error(f'Cannot read bash alias file: {filename}')
			continue
		options['aliases'] = {**options['aliases'], **parse_aliases(script)}
