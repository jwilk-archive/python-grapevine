========
``head``
========

yield the first items
  
Usage
-----

* ``<iterable> | head[<int>]``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | head(2) | tuple
('foo', 'bar')
>>> ('foo', 'bar', 'quux') | head(-2) | tuple
('foo',)

.. seealso::

 * :doc:`tail`
 * :doc:`select`
 * `GNU coreutils: head <http://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
