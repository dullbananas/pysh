import os
from .__init__ import __version__

def parse_prompt(prompt, **kwargs):
	cwd = os.getcwd()
	symbol = '$'
	version = __version__
	
	return prompt.format(**locals(), **kwargs)
