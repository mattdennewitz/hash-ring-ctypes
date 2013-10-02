"""Wrapper for C hash-ring library
"""

import collections
import ctypes

from const import *
from models import *


__all__ = ('HashRing', 'HASH_FUNCTION_MD5', 'HASH_FUNCTION_SHA1',
           'HASH_RING_OK', 'HASH_RING_ERR', )


try:
    dll = ctypes.cdll.LoadLibrary('libhashring.so')
except OSError:
    try:
        dll = ctypes.cdll.LoadLibrary('libhashring.dylib')
    except OSError:
        raise ImportError('libhashring could not be loaded')

dll.hash_ring_create.argtypes = (ctypes.c_uint32, HASH_FUNCTION, )
dll.hash_ring_create.restype = ctypes.POINTER(hash_ring_t)

dll.hash_ring_free.argtypes = (ctypes.POINTER(hash_ring_t), )
dll.hash_ring_free.restype = None

dll.hash_ring_add_node.argtypes = (
    ctypes.POINTER(hash_ring_t), ctypes.c_char_p, ctypes.c_uint32)
dll.hash_ring_add_node.restype = ctypes.c_int

dll.hash_ring_remove_node.argtypes = (
    ctypes.POINTER(hash_ring_t), ctypes.c_char_p, ctypes.c_uint32)
dll.hash_ring_remove_node.restype = ctypes.c_int

dll.hash_ring_find_node.argtypes = (ctypes.POINTER(hash_ring_t), ctypes.c_char_p, ctypes.c_uint32, )
dll.hash_ring_find_node.restype = ctypes.POINTER(hash_ring_node_t)


class HashRing(object):
    def __init__(self, replicas=5, nodes=None, enc=HASH_FUNCTION_MD5,
                 fail_silently=False):
        if not enc in (HASH_FUNCTION_MD5, HASH_FUNCTION_SHA1):
            raise ValueError('"enc" arg must be one of '
                             'HASH_FUNCTION_MD5 or HASH_FUNCTION_SHA1')

        self.fail_silently = fail_silently

        # create ring
        self._ring = dll.hash_ring_create(replicas, enc)

        # add nodes to ring
        if isinstance(nodes, collections.Iterable):
            map(self.add_node, nodes)

    def __len__(self):
        return self._ring.contents.numNodes

    def __del__(self):
        """Frees the ring before object instance is destroyed."""

        dll.hash_ring_free(self._ring)
        self._ring = None

    def _check_retcode(self, res, exc_type, msg):
        """Checks return code from hash ring functions, acts appropriately.
        """

        if res == HASH_RING_ERR:
            if not self.fail_silently:
                # something went wrong, and the user wants to know
                raise exc_type(msg)

            # something went wrong, but user does not want to know
            return HASH_RING_ERR

        return HASH_RING_OK

    def add_node(self, node, fail_silently=False):
        """Adds a node to the ring.

        Nodes are unique. Attempting to add a non-unique node
        will result in a `ValueError`.
        """

        if not isinstance(node, basestring):
            raise ValueError('Node value must be a string')

        # add node to ring
        ret = dll.hash_ring_add_node(self._ring, node, len(node))

        return self._check_retcode(
            ret, ValueError, 'Could not add node. Is it already in the ring?')

    def remove_node(self, node):
        """Removes a node from the ring.

        Attempts to remove a node not in the ring
        will result in a `ValueError`.
        """

        if not isinstance(node, basestring):
            raise ValueError('Node value must be a string')

        ret = dll.hash_ring_remove_node(self._ring, node, len(node))

        return self._check_retcode(
            ret, ValueError, 'Could not remove node. Was node not in ring?')

    def lookup(self, value):
        """Returns node name that corresponds to given `value`.

        If the ring is empty and the user has suppressed errors,
        this function returns `None`.
        """

        if not isinstance(value, basestring):
            raise ValueError('Node value must be a string')

        if len(self) == 0:
            if not self.fail_silently:
                raise ValueError('This ring has no nodes')
            return None

        ret = dll.hash_ring_find_node(self._ring, value, len(value))

        return ret.contents.name
