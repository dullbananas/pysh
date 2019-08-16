import re
import os



patterns = {
}


class Line:
	@staticmethod
	def factory(line):
		# Get indent_level and text
		indent_level = None
		for i, char in enumerate(line):
			if char != '\t':
				indent_level = i
				break
		if indent_level == None:
			return None
		text = line[indent_level:]
		
		# Get type of line and return instance of the corresponding class
		return Command(indent_level=indent_level, text=text)



class Command(Line):
	def __init__(self, indent_level, text):
		self.indent_level = indent_level
		self.text = text
	
	
	def run(self):
		os.system(self.text)



class Interpreter:
	def __init__(self):
		self.lines = []
	
	
	def feed_line(self, line):
		line = Line.factory(line)
		if line == None:
			return False
		self.lines.append(line)
		if self.ready():
			self.execute()
			self.lines = []
			return False
		else:
			return True
	
	
	def ready(self):
		return True
	
	
	def execute(self):
		self.lines[0].run()
