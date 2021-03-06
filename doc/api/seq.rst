=======
``seq``
=======

yield a sequence of numbers

Usage
-----

* ``seq(<last>)``
* ``seq(<first>, <last>)``
* ``seq(<first>, <increment>, <last>)``

Examples
--------

>>> from grapevine import *
>>> seq(5) | tuple
(1, 2, 3, 4, 5)
>>> seq(3.5, 6) | tuple
(3.5, 4.5, 5.5)
>>> seq(-10, 40, 100) | tuple
(-10, 30, 70)

.. seealso::

 * `GNU coreutils: seq <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
