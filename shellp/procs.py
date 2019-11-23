from abc import ABC, abstractmethod
import subprocess



class Proc(ABC):
	def __init__(self, args, chain):
		self.args = args
		self.chain = chain
	
	
	@abstractmethod
	def run(self, stdin, stdout):
		pass



class RealProc(Proc):
	def run(self, stdin, stdout, stderr):
		p = subprocess.Popen(self.args, stdin=stdin, stdout=stdout, stderr=stderr)
		p.wait()
