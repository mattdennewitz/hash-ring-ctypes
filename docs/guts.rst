Guts
====

.. _hash-ring-class:

``HashRing``
------------

.. autoclass:: hash_ring.HashRing
   :members: __init__, add_node, lookup, remove_node


.. _hash-ring-consts:

Return codes
------------

.. data:: HASH_RING_OK

Returned when a hash ring operation is successful.

.. data:: HASH_RING_ERR

Returned when a hash ring operation is successful.

Hash functions
--------------

.. data:: HASH_FUNCTION_MD5

Used when hashing should be done via MD5. Default.

.. data:: HASH_FUNCTION_SHA1

Used when hashing should be done via SHA1.
