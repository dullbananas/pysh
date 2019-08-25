import os
from abc import ABC, abstractmethod



class Operator:
	def __init__(self)



class Process(ABC):
	def __init__(self, args):
		self.args = args
	
	
	@abstractmethod
	def run(self, stdin, stdout):
		pass



class RealProcess(Process):
	def run(self, stdin, stdout):
		
