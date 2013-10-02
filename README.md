# hash-ring-ctypes

Fast ctypes-based wrapper around [libhashring](https://github.com/chrismoos/hash-ring/).

## Installation

For now, clone from this repo:

```shell
$ pip install -e git+https://github.com/mattdennewitz/hash-ring-ctypes#egg=hash_ring
```

## Usage

```python
import hash_ring

# create a ring with nodes with 10 replicas
# and a handful of nodes
nodes = ['cdn1', 'cdn2', 'cdn3', 'cdn4']
ring = hash_ring.HashRing(replicas=10, nodes=nodes)

# or create an empty ring with the default number of replicas (5)
# and add nodes by hand
ring = hash_ring.HashRing()
map(ring.add_node, ['cdn1', 'cdn2', 'cdn3', 'cdn4'])

# look up a node for a certain value, like a filename
fn = 'artwork/1/header.jpg'
cdn_endpoint = ring.lookup(fn)
```

## Tests

To run tests, run `tests.py`.

```shell
$ python tests.py
```
