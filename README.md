![build](https://img.shields.io/travis/dullbananas/shellp/develop.svg)
![Codacy branch coverage](https://img.shields.io/codacy/coverage/0d67da41aecc427d82b8a0e7b6747f83/develop.svg)
![Codacy branch grade](https://img.shields.io/codacy/grade/0d67da41aecc427d82b8a0e7b6747f83/develop.svg)
![license](https://img.shields.io/github/license/dullbananas/shellp.svg?color=blue)
![pypi](https://img.shields.io/pypi/v/shellp.svg?color=blue)
![PyPI - Status](https://img.shields.io/pypi/status/shellp.svg?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dm/shellp.svg)

# ShellP
ShellP is a shell implemented in Python and currently in pre-alpla development.

## Usage
### Installation
ShellP supports Python 3.6 and newer; make sure you have a supported version. Just run this to install:
```
pip3 install shellp
```
If you are not using a supported version, then shame on you.
### Running ShellP
You can use `python3 -m shellp` or `shellp` to run ShellP. Type `exit` to exit the shell; ^D won't work since ShellP doesn't like it.
### Configuration
You can have a custom configuration script in `~/.shellp/config.py` that overrides the default config. Here are the configuration options currently supported:

| Name   | Description                                                                             |
| :----: | --------------------------------------------------------------------------------------- |
| `ps1`  | The prompt that shows before every command you type. See below for the format of `ps1`. |

#### PS1 Format
ShellP uses Python's `str.format()` method on `ps1` to format it, unlike other shells which use ugly, unreadable escape codes. Here is an example of a config.py that sets the `ps1` option:
```
ps1 = '{style.red}{cwd} {style.yellow}{git_branch} {style.green}{symbol}'
```
This is the garbage that you would have to put in your `.bashrc` to get a similar prompt in Bash:
```
export PS1="\[\e[31m\]\w\[\e[m\] \[\e[33m\]\`parse_git_branch\`\[\e[m\] \[\e[32m\]\\$\[\e[m\] "
```
You would also have to define `parse_git_branch`, which takes up a bunch of more lines.

Here are the values you can use in `ps1`:

| Name             | Description                                                     |
| :--------------: | --------------------------------------------------------------- |
| `bell`           | An ASCII bell character                                         |
| `cwd`            | The current directory                                           |
| `git_branch`     | The current git branch, or nothing if you are not in a git repo |
| `hostname`       | The hostname of your computer                                   |
| `shellp_version` | The installed version of ShellP                                 |
| `symbol`         | `#` if you are ~~Groot~~ root, otherwise `$`                    |
| `style`          | [The `beautiful_ansi` module](https://github.com/Carrene/beautiful-ansi/blob/master/beautiful_ansi.py) |
