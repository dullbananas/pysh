import pytest
from shellp.parse_prompt import parse_prompt

def test_prompt_symbol():
	assert parse_prompt('{symbol}') in ('$', '#')
