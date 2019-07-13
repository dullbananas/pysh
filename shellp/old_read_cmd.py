'''Defines an improved version of ``input()``'''

import sys
from select import select


def read_cmd(prompt, timeout):
	timeout = float(timeout)
	
	if timeout == 0:
		cmd = input(prompt)
	else:
		print(prompt, end='')
		i, _, _ = select([sys.stdin], [], [], timeout)
		if i:
			cmd = sys.stdin.readline()
			# Handle EOF
			if cmd == '':
				raise EOFError
			else:
				cmd = cmd.strip() # Remove trailing newline
		else:
			print(f'\nTimeout exceeded ({timeout} seconds)')
			sys.exit(0)
	
	return cmd
