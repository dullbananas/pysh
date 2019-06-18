import re

pattern = r'\s*alias\s+(?P<alias>[^\=]+)\s*\=({}|\")(?P<replacement>[^\2]+)\2\s*'.format('\\\'')


def parse_files(filenames):
	result = {}
	
	for filename in filenames:
		with open(filename) as file:
			contents = file.read()
		
		for line in contents.split('\n'):
			match = re.match(pattern, line)
			if match:
				result[match.group('alias')] = match.group('replacement')
	
	return result
