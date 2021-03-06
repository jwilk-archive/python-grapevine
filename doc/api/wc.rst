======
``wc``
======

return the number of items

Usage
-----

* ``<pipelined-iterable> | wc``
* ``wc(<iterable>)``

Examples
--------

>>> from grapevine import *
>>> wc(['foo', 'bar', 'quux'])
3
>>> cat(None for x in range(0, 7) for y in range(0, x) for z in range(y, x)) | wc
56

.. seealso::

 * `GNU coreutils: wc <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
