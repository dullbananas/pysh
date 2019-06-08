'''Formats PS1 and PS2.'''
import os
from .__init__ import __version__
import beautiful_ansi as style
import platform
import pygit2
from _pygit2 import GitError

def parse_prompt(prompt, **kwargs):
	bell = chr(7)
	cwd = os.getcwd()
	try:
		git_branch = pygit2.Repository('.').head.shorthand
	except GitError:
		git_branch = ''
	hostname = platform.node()
	shellp_version = __version__
	symbol = '#' if os.getuid() == 0 else '$'
	
	return prompt.format(style=style, **locals(), **kwargs)
