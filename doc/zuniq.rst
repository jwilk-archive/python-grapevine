=========
``zuniq``
=========

omit duplicate items

Usage
-----

* ``<iterable> | zuniq``

Examples
--------

>>> from grapevine import *
>>> cat((1, 2, 3, 3, 2, 1)) | zuniq | tuple
(1, 2, 3)

Caveats
-------

Items need to be hashable.

.. seealso::

 * :doc:`uniq`

.. vim:ts=3 sts=3 sw=3 et
