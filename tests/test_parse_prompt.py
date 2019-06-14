import pytest
from shellp.parse_prompt import parse_prompt

def test_prompt_symbol():
	assert parse_prompt('{symbol}') in ('$', '#')

def test_prompt_platform():
	import platform
	assert parse_prompt('{plaform["processor"]}') == platform.processor()
