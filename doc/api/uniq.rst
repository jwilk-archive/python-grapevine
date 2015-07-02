========
``uniq``
========

discard all but one of successive equal items

Usage
-----

* ``<iterable> | uniq``

Examples
--------

>>> from grapevine import *
>>> cat((1, 2, 3, 3, 2, 1)) | uniq | tuple
(1, 2, 3, 2, 1)

.. seealso::

 * :doc:`zuniq`
 * `GNU coreutils: uniq <http://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
