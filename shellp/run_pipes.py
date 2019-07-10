import subprocess
import time
import signal


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
	time.sleep(0.1)
	
	# Create processes in the middle
	for index, cmd in enumerate(cmds):
		if index == 0:
			continue
		elif index < len(cmds) - 1:
			procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout, stdout=subprocess.PIPE))
		else:
			procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout))
		time.sleep(0.1)
	
	# Communicate with processes
	old_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
	procs[0].communicate()
	signal.signal(signal.SIGINT, old_handler)
	procs[-1].wait()
