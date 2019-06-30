from shellp.split_cmd import split_cmd, modify_arg
from pathlib import Path

def test_no_args():
	assert split_cmd('') == []
	assert split_cmd('""') == ['']

def test_one_arg():
	assert split_cmd('thing') == ['thing']

def test_multiple_args():
	assert split_cmd('one two') == ['one', 'two']
	assert split_cmd('one two three') == ['one', 'two', 'three']

def test_quoted_args():
	assert split_cmd('"i hate samsung"') == ['i hate samsung']
	assert split_cmd('one two "three four"') == ['one', 'two', 'three four']
	assert split_cmd('one "two"') == ['one', 'two']

def test_aliases():
	assert split_cmd('py', {'py': 'python'}) == ['python']
	assert split_cmd('py -m shellp', {'py': 'python'}) == ['python', '-m', 'shellp']

def test_home_dir_substitution():
	home = str(Path.home())
	assert modify_arg('~') == home
