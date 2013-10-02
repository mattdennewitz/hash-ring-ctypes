Installation and Usage
======================

Before using this library, please make sure you have `libhashring` installed.
`libhashring` is available `here <https://github.com/chrismoos/hash-ring/>`_.

Installation
------------

For now, clone from this repo:

.. code-block:: bash

    $ pip install -e git+https://github.com/mattdennewitz/hash-ring-ctypes#egg=hash_ring

Usage
-----

Creating a hash ring is simple: create an instance of the 
:ref:`hash-ring-class` class, and populate with nodes.

.. code-block:: python

    import hash_ring

    # create a ring with nodes with 10 replicas and four nodes
    nodes = ['cdn1', 'cdn2', 'cdn3', 'cdn4']
    ring = hash_ring.HashRing(replicas=10, nodes=nodes)

    # or create an empty ring with the default number of replicas (five)
    # and add nodes by hand
    ring = hash_ring.HashRing()
    map(ring.add_node, ['cdn1', 'cdn2', 'cdn3', 'cdn4'])

Once you have an instance of :ref:`hash-ring-class`,
you can start finding nodes for values with :py:meth:`~hash_ring.HashRing.lookup`

.. code-block:: python

    # look up a node for a certain value
    fn = 'artwork/1/header.jpg'
    node = ring.lookup(fn)

If you need to remove a node from the ring
-- for example, you might need to remove a feisty CDN endpoint --
you can do so with :py:meth:`~hash_ring.HashRing.remove_node`
