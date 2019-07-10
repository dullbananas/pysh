Configuration
=============

You can create a configuration file at ``~/.shellp/config.py`` to customize
ShellP. In this file, you simple define them as variables, just like in Sphinx's
``conf.py`` file. Here is an example of a configuration file::

   aliases = {
      'cd': 'cd --color',
      'ga': 'git add',
   }
   debug = True
   timeout = 3600


List of Options
---------------
These are the options that you can use in your config file:

``aliases``
   A dictionary mapping aliases to commands. Example::
   
      aliases = {
         'ga': 'git add .',
         'l': 'ls --color -l',
      }

``bash_alias_files``
   This option allows you to make ShellP parse one or more Bash files and
   extract aliases from it. Example::
   
      bash_alias_files = ['/home/user/.bashrc']

``debug``
   This option enables debug mode when set to ``True``. These are the changes
   that take effect when you enable this option:
   
   - Before a command is run, the array of arguments that will be passed to the
     command will be shown (e.g. ``['git', 'commit', '-m', 'i hate you']``)

``env_lists``
   This option allows you to set colon-separated environment variables such as
   ``$PATH`` with arrays instead of messy colon-separated strings. The items you
   add in the array are prepended to the environment variable's existing value.
   Example::
   
      env_lists = {
         'PATH': [
            '/home/user/bin',
            '/other/path',
         ],
      }

``env_vars``
   This is a dictionary of environment variables to set. Example::
   
      env_vars = {
         'EDITOR': 'vim',
      }

``ps1``
   This is the prompt that is shown before the command you type. See `Prompt
   Format`_ for details on the format of this option.

``timeout``
   This sets the timeout for command input in seconds. You can use either an
   integer or a float.


Prompt Format
-------------

``ps1`` uses a clean format that is much more readable than Bash's escape codes.
It is parsed using ``str.format()``. Example::

   ps1 = '{style.green}{cwd} {symbol} '

Here are the values you can use:

``{bell}``
   ASCII BEL character; same as ``chr(7)``

``{cwd}``
   The current working directory

``{git_branch}``
   The current Git branch, or an empty string if you're not in a Git directory.

``{hostname}``
   Your device's hostname

``{platform["*"]}``
   Shows the result of the specified function in the ``platform`` module; for
   example, ``platform["processor"]``

``{shellp_version}``
   The version of ShellP that you are using

``{style.*}``
   The ``beautiful_ansi`` module

``{symbol}``
   A ``#`` if you are root, otherwise ``$``

``{time["*"]}``
   The current time formatted with ``time.strftime()``

``{uid}``
   Your user ID

``{user}``
   Your username