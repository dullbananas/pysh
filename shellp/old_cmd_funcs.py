def cmd_func(flags={}, arg_flags={}):
	def decor(f):
		def wrapper(args):
			# Help
			if '--help' in args:
				print('Help not implemented yet')
				return
			
			# Dictionary of parameters to be passed to the wrapped function
			params = {}
			# List of valid flags
			flags = flags.keys()
			# List of valid flags that accept arguments
			arg_flags = arg_flags.keys()
			
			get_long_flags = lambda flags: [i[0] for i in flags]
			get_short_flags = lambda flags: [i[1] for i in filter((lambda x: len(x) >= 2), flags)]
			
			# Set the flags that are passed to True
			for flagset in flags:
				# Long flag names
				if flagset[0] in args:
					params[flag[0][2:]] = True
					flags.remove(flagset[0])
					break
				# Short flag names
				if len()
	
	return decor
