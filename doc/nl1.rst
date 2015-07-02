=======================
``nl`` (a.k.a. ``nl1``)
=======================

number items of an iterable (start with 1)

Usage
-----

* ``<iterable> | nl1``
* ``<iterable> | nl``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | nl1 | list
[(1, 'foo'), (2, 'bar'), (3, 'quux')]
>>> nl is nl1
True

.. seealso::

 * :doc:`nl0`
 * `GNU coreutils: nl <http://www.gnu.org/software/coreutils/manual/html_node/nl-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
