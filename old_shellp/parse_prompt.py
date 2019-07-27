'''Formats PS1'''
import os
from .__init__ import __version__
import beautiful_ansi as style
import platform as pf
import pygit2
from time import strftime, gmtime
from _pygit2 import GitError
from getpass import getuser

class Platform:
	def __getitem__(self, name):
		#name = name[1:-1] # remove quotes placed by str.format
		try:
			return pf.__dict__[name]()
		except KeyError:
			return '[{}]'.format(name)

class Time:
	def __getitem__(self, fmt):
		#fmt = fmt[1:-1]
		return strftime(fmt, gmtime())

def parse_prompt(prompt, **kwargs):
	bell = chr(7)
	cwd = os.getcwd()
	try:
		git_branch = pygit2.Repository('.').head.shorthand
	except GitError:
		git_branch = ''
	hostname = pf.node()
	platform = Platform()
	shellp_version = __version__
	symbol = '#' if os.getuid() == 0 else '$'
	time = Time()
	uid = os.getuid()
	user = getuser()
	
	return prompt.format(style=style, **locals(), **kwargs)
