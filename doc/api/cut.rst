=======
``cut``
=======

yield a slice of every item

Usage
-----

* ``<iterable> | cut[<int>]``
* ``<iterable> | cut[<slice>]``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | cut[-2:] | tuple
('oo', 'ar', 'ux')
>>> zip(range(0, 3), range(3, 6)) | cut[1] | tuple
(3, 4, 5)

.. seealso::

 * `GNU coreutils: cut <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
