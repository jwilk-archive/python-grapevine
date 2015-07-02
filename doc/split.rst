=========
``split``
=========

split an iterable into fixed-sized pieces
  
Usage
-----

* ``<iterable> | split(<int>)``

Examples
--------

>>> from grapevine import *
>>> xrange(7) | split(3) | list
[(0, 1, 2), (3, 4, 5), (6,)]

.. seealso::

 * `GNU coreutils: split <http://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
