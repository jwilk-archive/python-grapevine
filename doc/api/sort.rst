========
``sort``
========

sort items

Usage
-----

* ``<pipelined-iterator> | sort``
* ``<iterable> | sort(<keyword-argument>…)``
* ``sort(<iterable>…)``
* ``sort(<iterable>…, <keyword-argument>…)``

``sort`` takes additional keyword arguments: ``cmp``, ``key`` and ``reverse``.
See `Python documentation <https://docs.python.org/library/stdtypes.html#mutable-sequence-types>`_ for details.

Examples
--------

>>> from grapevine import *
>>> sort((4, 2, 1, 3)) | tuple
(1, 2, 3, 4)
>>> cat(('foo', 'bar', 'qaax')) | sort(key = lambda x: x[1:3]) | tuple
('qaax', 'bar', 'foo')
>>> print '-'.join(('foo', 'bar', 'quux') | cat | sort)
bar-foo-quux

.. seealso::

 * `GNU coreutils: sort <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
