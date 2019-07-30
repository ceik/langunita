#!/usr/bin/env python3

import utils
from mst import prim

data = utils.load_space_delimited_file('data/primEdges.txt')

# print(data)

x = prim.PrimHeap(data)

# for n in x.nodes.items():
#     print(n[1].id)

x.comp_mst()

# print(x.processed_nodes)

# p = 30
# while p > 0:
#     y = x.remaining_nodes.pop()
#     print(y[0], y[1].id)
#     p -= 1

s = 0

for e in x.mst.values():
    s += e.cost

print(s)
