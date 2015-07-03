=====================
Generators with input
=====================

Usage
-----

* ``cat(<generator-with-input>…)``
* ``<pipelined-iterable> | <generator-with-input>``

Use the special ``STDIN`` to access your input.

Examples
--------

>>> from grapevine import *

>>> cat((1, 2, 3)) | (-x for x in STDIN) | tuple
(-1, -2, -3)

>>> cat(x + 1 for x in (1, 2, 3)) | (x * x for x in STDIN) | tuple
(4, 9, 16)

>>> def tmp():
...     n = 0
...     for i in STDIN:
...             n += i
...             if n > 10:
...                     yield n
...                     n = 0
...
>>> range(10) | cat([4], tmp(), [2]) | tuple
(4, 15, 13, 17, 2)

.. seealso::

 * `Python Tutorial: Generators <https://docs.python.org/tutorial/classes.html#generators>`_
 * `Python Tutorial: Generator Expressions <https://docs.python.org/tutorial/classes.html#generator-expressions>`_

.. vim:ts=3 sts=3 sw=3 et
