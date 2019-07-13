import pytest
from shellp.parse_prompt import parse_prompt

def test_prompt_symbol():
	assert parse_prompt('{symbol}')[0] in ('$', '#')

def test_prompt_platform():
	import platform
	assert parse_prompt('{platform[processor]}') == platform.processor()
	assert parse_prompt('{platform[subscribe to Dull Bananas]}') == '[subscribe to Dull Bananas]'
