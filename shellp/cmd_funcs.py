import traceback


def command(f):
	def wrapper(args):
		try:
			f(args)
		except Exception:
			print(traceback.format_exc())
	
	wrapper.role = 'cmd_func'
	wrapper.name = f.__name__
	return wrapper
