import curses
from shellp import __version__
import beautiful_ansi as style


def main(stdscr):
	# Clear screen
	stdscr.clear()
	# Initialize the shell area of the screen
	shell_win = curses.newwin(curses.LINES - 3, curses.COLS, 0, 0)
	stdscr.refresh()
	shell_win.addstr('ShellP version ' + __version__)
	shell_win.refresh()
	
	# Initialize the status bar at the bottom of the screen
	status_win = curses.newwin(3, curses.COLS, curses.LINES - 3, 0)
	status_win.addstr(style.blightwhite + ' '*3*curses.COLS)
	status_win.refresh()
	stdscr.getkey()


def run():
	curses.wrapper(main)

if __name__ == '__main__':
	run()
