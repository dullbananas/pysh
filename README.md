![build](https://img.shields.io/travis/dullbananas/shellp/develop.svg)
![Read the Docs (version)](https://img.shields.io/readthedocs/shellp/develop.svg)
![Codacy branch coverage](https://img.shields.io/codacy/coverage/0d67da41aecc427d82b8a0e7b6747f83/develop.svg)
![Codacy branch grade](https://img.shields.io/codacy/grade/0d67da41aecc427d82b8a0e7b6747f83/develop.svg)
![license](https://img.shields.io/github/license/dullbananas/shellp.svg?color=blue)
![pypi](https://img.shields.io/pypi/v/shellp.svg?color=blue)
![PyPI - Status](https://img.shields.io/pypi/status/shellp.svg?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dm/shellp.svg)

# ShellP
Click here to watch a demo:
[![asciicast](https://asciinema.org/a/257573.svg)](https://asciinema.org/a/257573)
ShellP is a shell implemented in Python and currently in alpla stage of development. This is an example shell session that utilizes [argument functions](https://shellp.readthedocs.io/en/latest/features/arg_funcs.html):

```
$ echo $$random
64
$ echo $$random
40
$ echo $$tempfile
/tmp/my_temp_file.txt
$ echo $$weekday
Thursday
```

## Advantages over other shells
  * Easy to configure (e.g. PS1 value is more readable and easier to make yourself)
  * Easy to install without root access
  * Variety of values that you can use for PS1, including git branch and execution duration of previous command


## Basic Usage
Install ShellP:

```
pip3 install --user shellp
```

Start ShellP:

```
python3 -m shellp
```

## Project Links
  * [Documentation](https://shellp.readthedocs.io/en/latest/)
  * [GitHub repo](https://github.com/dullbananas/shellp)
  * [Contributing guidelines](https://github.com/dullbananas/shellp/blob/master/CONTRIBUTING.md)
  * [PyPI project](https://pypi.org/project/shellp)
