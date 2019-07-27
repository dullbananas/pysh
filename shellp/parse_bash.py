import re


alias_pattern = r'\s*alias\s+(?P<alias>[^\=]+)\s*\=(\'|\")(?P<replacement>[^\2]+)\2\s*'


def parse_aliases(script):
	# Maps aliases to replacements
	result = {}
	
	for line in script.split('\n'):
		match = re.match(alias_pattern, line)
		if match:
			result[match.group('alias')] = match.group('replacement')
	
	return result
