from shellp import utils

def test_split_list():
	l = ['one', 'two', '.', 'three', '.', 'four', 'five', 'six']
	assert utils.split_list(l, (lambda x: x == '.')) == [['one', 'two'], ['three'], ['four', 'five', 'six']]
