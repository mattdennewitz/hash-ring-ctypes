import ctypes

from const import HASH_FUNCTION, HASH_MODE


class ll_t(ctypes.Structure):
    pass

ll_t._fields_ = [
    ('data', ctypes.c_void_p),
    ('next', ctypes.POINTER(ll_t)),
]


class hash_ring_node_t(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('nameLen', ctypes.c_uint32),
    ]


class hash_ring_item_t(ctypes.Structure):
    pass

hash_ring_item_t._fields_ = [
    ('node', ctypes.POINTER(hash_ring_node_t)),
    ('number', ctypes.c_uint64),
]


class hash_ring_t(ctypes.Structure):
    _fields_ = [
        ('numReplicas', ctypes.c_uint32),
        ('nodes', ctypes.POINTER(ll_t)),
        ('numNodes', ctypes.c_uint32),
        ('items', ctypes.POINTER(ctypes.POINTER(hash_ring_item_t))),
        ('numItems', ctypes.c_uint32),
        ('hash_fn', HASH_FUNCTION),
        ('hash_mode', HASH_MODE),
    ]
