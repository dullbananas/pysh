import subprocess
import os
import sys
import shutil
from . import utils, split_cmd
from .options import options


def run_pipeline(cmds):
	# Array of dictionaries of parameters to pass to Popen
	popen_params = []
	# Contains list of corresponding stdout FIFO filenames
	stdout_fifos = []
	
	for index, cmd in enumerate(cmds):
		params = {
			'args': cmd,
			'stderr': sys.stderr.buffer,
		}
		# Create FIFO for command's stdout unless it's the last command, with filename "~/.shellp/stdout_pipes_{shellp pid}/{command index in pipeline}"
		if index < len(cmds) - 1:
			# Generate path to pipe
			pid = str(os.getpid())
			fifo_name = os.path.join(utils.shellp_dir, f'stdout_pipes_{pid}/{index}')
			# Make sure that the directory containing the pipe exits and is empty
			try:
				pipes_dir = os.path.join(utils.shellp_dir, f'stdout_pipes_{pid}')
				shutil.rmtree(pipes_dir, ignore_errors=True)
				os.mkdir(pipes_dir)
			except FileExistsError:
				pass
			os.mkfifo(fifo_name)
			stdout_fifos.append(fifo_name)
			utils.debug('Created FIFO: '+fifo_name)
		
		# Set parameters for first command
		if index == 0:
			params['stdin'] = None
			params['stdout'] = os.open(fifo_name, os.O_WRONLY|os.O_NONBLOCK)
		
		# Set parameters for last command
		elif index == len(cmds) - 1:
			params['stdin'] = os.open(stdout_fifos[index-1], os.O_RDONLY|os.O_NONBLOCK)
			params['stdout'] = None
		
		# Set parameters for other commands
		else:
			params['stdin'] = os.open(stdout_fifos[index-1], os.O_RDONLY|os.O_NONBLOCK)
			params['stdout'] = os.open(fifo_name, os.O_WRONLY|os.O_NONBLOCK)
		
		# Append params to popen_params
		popen_params.append(params)
		utils.debug(params)
	
	# Run processes
	input('Press enter to run pipeline')
