import pytest
from shellp.parse_prompt import parse_prompt
import beautiful_ansi as style

def test_prompt_symbol():
	assert parse_prompt('{symbol}')[0] in ('$', '#')

def test_prompt_platform():
	import platform
	assert parse_prompt('{platform[processor]}') == platform.processor() + style.clear
