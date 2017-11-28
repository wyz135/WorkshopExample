""" Here is the docstring from the :code:`__init__.py` file. In this file, it is good practise to define
 :code:`__all__` so that anyone running :code:`import *` gets the right content!

 It is also good for removing unnecessary filenames. If you read the :code:`__init__.py` file, you can see that
 someone could now run :code:`from some_module import add_stuff` instead of
 having to run :code:`from some_module.file1 import add_stuff`.

 Also note that members without documentation (such as :code:`untested_subtract` do not appear in the doco).

 """
from some_module.example import add_stuff, untested_subtract

__all__ = ['add_stuff', 'untested_subtract']
