Argument Functions
==================

Here is an example showing what this feature does:

.. code-block:: bash

   $ echo $$func_name
   func_return_value

Argument functions allow you to run functions when typing commands and using
their return value as the resulting argument. Here is an example of a config file
that defines one that allows you to insert random numbers into your commands::

   import random
   
   def rand_100():
      return random.randrange(100)
   
   arg_funcs = {
      'rand': rand_100,
   }

Now, when you type in a command, ``$$rand`` will be replaced with a random number
from 0 to 99:

.. code-block:: bash

   $ echo $$rand
   4
   $ echo $$rand
   98
   $ echo $$rand
   45

There are so many things you can do with this, like making temporary files and
passing its name as the argument, or passing the current time as an argument.
