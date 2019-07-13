Inputting Commands
==================

ShellP has many features with inputting commands. These are made possible using
the ``prompt_toolkit`` library.

History
-------
.. versionadded:: 0.2.0
ShellP stores command history in ``~/.shellp/history``. You can use the up and
down arrow keys to navigate through the history.

Auto suggestion
--------------
.. versionadded:: 0.2.0
Auto suggestion allows you to quickly insert commands that you have typed before.
When you start typing a command, suggestions appear in grey. Pressing either the
right arrow key or ^E will cause the suggestion to be filled in.

Syntax Highlighting
-------------------
.. versionadded:: 0.2.0
ShellP uses Pygments to highlight commands as you type. You can use the
``highlight_style`` config option to set any style that is built in to Pygments.
