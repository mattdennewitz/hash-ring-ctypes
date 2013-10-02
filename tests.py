import unittest

import hash_ring


class TestHashRing(unittest.TestCase):
    def setUp(self):
        self.ring = hash_ring.HashRing()

    def test_add_nodes(self):
        """Ensures nodes can be added to the ring
        """

        for node in ['cdn1', 'cdn2', 'cdn3', 'cdn4']:
            self.assertEqual(self.ring.add_node(node), hash_ring.HASH_RING_OK)

        self.assertEqual(len(self.ring), 4)

    def test_readd_nodes(self):
        """Ensures the user knows that a node cannot be re-added to the ring
        """

        # add a node
        res = self.ring.add_node('cdn1')
        self.assertEqual(res, hash_ring.HASH_RING_OK)

        # try to re-add that node
        self.assertRaises(ValueError, self.ring.add_node, ('cdn1', ))

        # watch to see if it can fail quietly
        self.ring.fail_silently = True
        self.assertEqual(self.ring.add_node('cdn1'), hash_ring.HASH_RING_ERR)

        # ensure we're still only at 1 node
        self.assertEqual(len(self.ring), 1)

    def test_remove_valid_node(self):
        """Ensures nodes can be removed from the ring
        """

        node = 'cdn1'

        self.ring.add_node(node)
        self.assertEqual(len(self.ring), 1)

        self.ring.remove_node(node)
        self.assertEqual(len(self.ring), 0)

    def test_lookup(self):
        """Ensures node lookup is working
        """

        fn_pairs = {
            'cdn1': ('artwork/1/header.jpg',
                     'artwork/2/header.jpg',
                     'artwork/3/header.jpg',
                     'artwork/6/header.jpg', ),

            'cdn2': ('artwork/4/header.jpg',
                     'artwork/5/header.jpg', )
        }

        self.ring.add_node('cdn1')
        self.ring.add_node('cdn2')

        for cdn, fns in fn_pairs.items():
            for fn in fns:
                node = self.ring.lookup(fn)
                self.assertEqual(cdn, node)

    def test_empty_lookup(self):
        """Ensures an empty ring cannot be used
        """

        # fail loudly
        self.assertRaises(ValueError, self.ring.lookup, ('empty', ))

        # fail quietly
        self.ring.fail_silently = True
        self.assertEqual(self.ring.lookup('empty'), None)


if __name__ == '__main__':
    unittest.main()
