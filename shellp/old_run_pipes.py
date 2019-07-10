import sys
import os
import subprocess
from collections import namedtuple
from . import utils, split_cmd
from .options import options


PipedCmd = namedtuple('PipedCmd', 'args istream ostream')


def parse_pipes(cmds):
	# List of PipedCmds
	pipeset = []
	# First and last items in cmds
	first = cmds[0]
	last = cmds[-1]
	# Iterate cmd and set items in cmds
	for index, cmd in enumerate(cmds):
		if cmd == first:
			utils.debug('first: ' + str(cmd))
			istream = None
			ostream = os.pipe()
		elif cmd == last:
			utils.debug('last: '  + str(cmd))
			istream = pipeset[index-1].ostream[0]
			ostream = (None, None)
		else:
			utils.debug('not first nor last: ' + str(cmd))
			istream = pipeset[index-1].ostream[0]
			ostream = os.pipe()
		
		pc = PipedCmd(cmd, istream, ostream)
		utils.debug(pc)
		pipeset.append(pc)
	
	return pipeset


def run_pipes(pipeset):
	input('Press enter to run pipes now')
	# Array of Popen objects
	processes = []
	# Create processes
	for args, istream, ostream in pipeset:
		utils.debug('Running ' + repr(args))
		processes.append(subprocess.Popen(args, stdin=istream, stdout=ostream[1], stderr=sys.stderr))
		input(repr(processes[-1]))
	# Communicate with processes
	for proc in processes:
		proc.communicate()


def run_args(args):
	run_pipes(parse_pipes(split_cmd.split_pipes(args, options['aliases'])))
