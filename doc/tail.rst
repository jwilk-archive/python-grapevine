========
``tail``
========

yield the last items
  
Usage
-----

* ``<iterable> | tail[<int>]``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | tail(-1) | tuple
('quux',)
>>> ('foo', 'bar', 'quux') | tail(+3) | tuple
('quux',)

.. seealso::

 * :doc:`head`
 * :doc:`select`
 * `GNU coreutils: tail <http://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
