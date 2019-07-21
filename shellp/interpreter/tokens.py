import tokenize
import re


class SpecialStmt:
	def __init__(self, name, pattern=None):
		self.name = name
		self.pattern = pattern
	
	def parse(line):
		


class Token:
	def __init__(self, kind, exact_kind, params):
		self.kind = kind
		self.exact_kind = exact_kind
		self.params = params
	
	def __getattr__(self, name):
		try:
			return self.params[name]
		except KeyError:
			raise AttributeError


def tokenize_line(line):
	if line[0]
