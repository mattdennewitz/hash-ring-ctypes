# hash-ring-ctypes

Fast ctypes-based wrapper around [libhashring](https://github.com/chrismoos/hash-ring/).

What is a hash ring? Check [this](http://www.martinbroadhurst.com/Consistent-Hash-Ring.html) out.

## Installation

For now, clone from this repo:

```shell
$ pip install -e git+https://github.com/mattdennewitz/hash-ring-ctypes#egg=hash_ring
```

## Usage

Documentation online at [Read the Docs](http://hash-ring-ctypes.readthedocs.org/en/latest/).

But here's a quick example! Let's say that you want to increase parallel
downloads of your site's assets by the browser via [domain sharding](https://developers.google.com/speed/pagespeed/service/ShardResources).
You've created four CNAME records pointing to your CDN,
`cdn.example.com`, `cdn2.example.com`, `cdn3.example.com`, and `cdn4.example.com`,
and you want to use a hash ring to select which address will serve
a specific asset.

```python
import hash_ring

# create a ring with nodes with 10 replicas
# and a handful of nodes
nodes = ['cdn1.example.com', 'cdn2.example.com',
         'cdn3.example.com', 'cdn4.example.com']
ring = hash_ring.HashRing(replicas=10, nodes=nodes)

# or create an empty ring with the default number of replicas (5)
# and add nodes manually
ring = hash_ring.HashRing()
map(ring.add_node, nodes)
```

Now that you have a ring, you can find which domain
you should use to serve a specific asset. In this case,
we'll look up which domain matches `artwork/1/header.jpg`.

```python
# look up a node for a certain value, like a filename
cdn_endpoint = ring.lookup('artwork/1/header.jpg')
```

## Tests

To run tests, run `tests.py`.

```shell
$ python tests.py
```

## Further Reading

- [Consistent hashing](http://en.wikipedia.org/wiki/Consistent_hashing)
- [libhashring](https://github.com/chrismoos/hash-ring)
