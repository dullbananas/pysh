import re

# A pattern that represents a single line in a bash script that defines an alias:
#	* Optional whitespace
#	* The word 'alias'
#	* One or more white space characters
#	* The name of the alias which can contain any character except for '='
#	* Optional whitespace
#	* '=' symbol
#	* Single or double quote
#	* The command that the alias is for, which can contain any character except for the quotes used
#	* The same quote as before
#	* Optional whitespace
pattern = r'\s*alias\s+(?P<alias>[^\=]+)\s*\=({}|\")(?P<replacement>[^\2]+)\2\s*'.format('\\\'')


def parse_files(filenames):
	# Maps aliases to replacements
	result = {}
	
	for filename in filenames:
		with open(filename) as file:
			contents = file.read()
		
		for line in contents.split('\n'):
			match = re.match(pattern, line)
			if match:
				result[match.group('alias')] = match.group('replacement')
	
	return result
