from abc import ABC, abstractmethod
import os



class PromptItem(ABC):
	@abstractmethod
	def __init__(self):
		pass
	
	
	@abstractmethod
	def get_str(self):
		pass



class Text(PromptItem):
	def __init__(self, text):
		self.text = text
	
	
	def get_str(self):
		return self.text



class Symbol(PromptItem):
	def __init__(self, normal='$', root='#'):
		self.normal = normal
		self.root = root
	
	
	def get_str(self):
		if os.geteuid() == 0:
			return self.root
		else:
			return self.normal
