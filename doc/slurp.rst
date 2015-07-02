=========
``slurp``
=========

discard every item

Usage
-----

* ``<pipelined-iterable> | slurp``
* ``slurp(<iterable>)``

Examples
--------

>>> from grapevine import *

>>> def tmp(s): print s
...
>>> slurp(tmp(s) for s in ('foo', 'bar', 'quux'))
foo
bar
quux
>>> tmp = []
>>> cat(tmp.__iadd__([x]) for x in xrange(5)) | slurp
>>> tmp
[0, 1, 2, 3, 4]

>>> def tmp(): yield 0; raise RuntimeError()
...
>>> slurp(tmp())
Traceback (most recent call last):
...
RuntimeError

.. vim:ts=3 sts=3 sw=3 et
