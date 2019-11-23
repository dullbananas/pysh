import os
import io
import subprocess
from abc import ABC, abstractmethod



class Operator(ABC):
	def __init__(self, stdin=None, stdout=None):
		self.stdin = stdin
		self.stdout = stdout
	
	
	@abstractmethod
	def handle_input(self, data):
		pass



class Process(ABC):
	def __init__(self, args):
		self.args = args
	
	
	@abstractmethod
	def run(self, stdin, stdout):
		pass



class RealProcess(Process):
	def run(self, stdin, stdout):
		self.proc = subprocess.Popen(self.args)
