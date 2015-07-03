========
``grep``
========

yield items matching a pattern

Usage
-----

* ``<iterable> | grep(<test>…)``
* ``grep(<test>, <iterable>…)``

*test* is:

* a regular expression;
* or a single argument function.

Examples
--------

>>> from grapevine import *
>>> grep('a[rz]', ['foo', 'bar', 'baz']) | tuple
('bar', 'baz')
>>> range(-10, 10) | grep(lambda x: x % 7 == 1) | tuple
(-6, 1, 8)

.. seealso::

 * `GNU grep <http://www.gnu.org/software/grep/doc/grep.html>`_

.. vim:ts=3 sts=3 sw=3 et
