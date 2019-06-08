# Contributing to ShellP
Thank you for deciding to contribute to ShellP.

## Setup
* Make sure that you have Git installed and configured.
* Make a fork of this repository and clone the fork locally using `git clone`.
* Switch to the `develop` branch with `git checkout` and run `./setup.py develop` (setup your `venv` before doing this if you want to). If you want to install the files in your
user `site-packages` instead of the one in `/usr/lib/python`, set the `-d` option to the path to your user `site packages`;
for example: `./setup.py develop -d /home/username/.local/lib/python3.7/site-packages`.

## Making edits
* If you want to make edits to the code, don't make your changes in the `master` branch! Instead, use the `develop` branch, or
make another branch for your edits if you want.
* When you are finished with making a modification to ShellP, push to your fork on GitHub and make a pull request to the
`develop` branch of the main repository (dullbananas/shellp).

## Reporting bugs
* If you find a bug in ShellP and you don't want to fix it yourself, open an issue on the main repo.
* Be specific about the bug. If it happens when trying to run a command using ShellP, put the command you're trying to use
into the issue. If an error occurs (a Python exception), put the entire traceback of the exception into the issue if possible.
* Provide details like the version of ShellP you're using and what OS you have. Your Python version may also be necessary.
