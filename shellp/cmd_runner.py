from collections import namedtuple


PUNCTUATION = '|'


Punctuation = namedtuple('Punctuation', 'symbol')
String = namedtuple('String', 'content')

def tokenize_cmd(text):
	pos = 0
	while pos < len(text):
		# Punctuation
		if text[pos] in PUNCTUATION:
			yield Punctuation(text[pos])
			pos += 1
		# Raw string
		elif text[pos:pos+2] in ('r"', "r'"):
			quote = text[pos+1] # " or '
			str_text = '' # the text in the string
			pos += 2
			while True:
				# End of string
				if text[pos] == quote:
					yield str_text
					pos += 1
				# \' or \"
				elif text


class Cmd:
	class __init__(self, args):
		for arg in args:
			if
