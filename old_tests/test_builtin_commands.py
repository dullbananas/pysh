import pytest
from shellp import builtin_commands as cmds


def test_eval(capfd):
	cmds.eval(['eval', '2+2'])
	captured = capfd.readouterr()
	assert captured.out == '4\n'
