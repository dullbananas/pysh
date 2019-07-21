class Interpreter:
	def __init__():
		self.current_lines = []
	
	
	def feed_line(line):
		self.current_lines.append(line)
		if self.ready():
			self.exec_lines()
			return False
		else:
			return True
	
	
	def exexc
