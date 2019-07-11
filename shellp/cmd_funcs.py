import traceback


def command(f):
	'''A f**king decorator'''
	def wrapper(args):
		try:
			f(args)
		except Exception:
			print(traceback.format_exc())
	
	wrapper.role = 'cmd_func'
	wrapper.name = f.__name__
	return wrapper
