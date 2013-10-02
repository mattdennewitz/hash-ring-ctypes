import timeit


print timeit.timeit(stmt="""
for i in range(10):
  ring.lookup('artwork/' + str(i) + '/header.jpg')
""",
              setup="""
import hash_ring
ring = hash_ring.HashRing()
map(ring.add_node, ('cdn1', 'cdn2', 'cdn3', 'cdn4', ))
              """, number=10000)
