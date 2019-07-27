from .main import main
import sys


def run():
	interactive = sys.stdin.isatty()
	use_user_config = not (('-U' in sys.argv) or ('--no-user-config' in sys.argv))
	main(**locals())
