import subprocess
from . import utils


def run_pipeline(cmds):
	'''Runs a pipeline
	
	Args:
		cmds: A list of lists of arguments, such as ``[['ls', '-l'], ['grep', '.py']]``
	Returns:
		FBI OPEN UP
	'''
	
	# List of processes
	procs = []
	
	# Create first process
	procs.append(subprocess.Popen(cmds[0], stdout=subprocess.PIPE))
	
	# Create processes in the middle
	for index, cmd in enumerate(cmds):
		if index == 0:
			continue
		elif index < len(cmds) - 1:
			procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout, stdout=subprocess.PIPE))
		else:
			procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout))
	
	# Communicate with processes
	procs[0].communicate()
	procs[-1].wait()
