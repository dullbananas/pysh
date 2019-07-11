Pipelines
=========
.. versionadded:: 0.2.0

Like other shells, ShellP allows you to pipe multiple commands together:

.. code-block:: bash

   $ ls -R /home | less

.. note::

   There is a bug in ShellP that sometimes causes nothing to happen after a
   pipeline stops running. When this happens, sending an interrupt (``^C`` on
   Linux) should fix it.

Currently, other operators like ``>>`` are not supported.
