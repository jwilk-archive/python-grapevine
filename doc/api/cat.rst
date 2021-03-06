=======
``cat``
=======

construct a pipeline

Usage
-----

* ``<iterable> | cat``
* ``cat(<iterable>…)``

Examples
--------

>>> from grapevine import *
>>> [1, 2, 3] | cat | tuple
(1, 2, 3)
>>> cat([1, 2, 3]) | tuple
(1, 2, 3)
>>> cat([1, 2, 3], (4, 5, 6)) | tuple
(1, 2, 3, 4, 5, 6)

.. seealso::

 * `GNU coreutils: cat <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
