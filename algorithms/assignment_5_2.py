#!/usr/bin/env python3

import utils
import heapq
from shortest_path import dijkheap

data = utils.load_tab_delimited_file('data/dijkstraData.txt')

d = dijkheap.DijkHeap(data)

# print(d.nodes[5].id)
# for e in d.nodes[5].edges:
#     print(e.end, e.length)


d.comp_sps(0)
# d.init_dijks(0)


# for x in d.dijks.pq:
#     print(x[0], x[1])

# for x in d.processed_nodes.items():
#     print(x)
# for x in d.shortest_paths.items():
#     print(x)

# Test if algo gives right answers
print(7, d.shortest_paths['7'] == 2599)
print(37, d.shortest_paths['37'] == 2610)
print(59, d.shortest_paths['59'] == 2947)
print(82, d.shortest_paths['82'] == 2052)
print(99, d.shortest_paths['99'] == 2367)
print(115, d.shortest_paths['115'] == 2399)
print(133, d.shortest_paths['133'] == 2029)
print(165, d.shortest_paths['165'] == 2442)
print(188, d.shortest_paths['188'] == 2505)
print(197, d.shortest_paths['197'] == 3068)

# print(d.dijks[0][0], d.dijks[0][1].id)
# print(d.dijks[1][0], d.dijks[1][1].id)
# print(d.dijks[2][0], d.dijks[2][1].id)
# print(d.dijks[3][0], d.dijks[3][1].id)
# print(d.dijks[4][0], d.dijks[4][1].id)
# print(d.dijks[5][0], d.dijks[5][1].id)
# print(d.dijks[6][0], d.dijks[6][1].id)

# d.dijks[0], d.dijks[5] = d.dijks[5], d.dijks[0]
# print('--- flipped 0 & 1 ---')

# print(d.dijks[0][0], d.dijks[0][1].id)
# print(d.dijks[1][0], d.dijks[1][1].id)
# print(d.dijks[2][0], d.dijks[2][1].id)
# print(d.dijks[3][0], d.dijks[3][1].id)
# print(d.dijks[4][0], d.dijks[4][1].id)
# print(d.dijks[5][0], d.dijks[5][1].id)
# print(d.dijks[6][0], d.dijks[6][1].id)

# heapq.heappop(d.dijks)
# print('--- popped ---')

# print(d.dijks[0][0], d.dijks[0][1].id)
# print(d.dijks[1][0], d.dijks[1][1].id)
# print(d.dijks[2][0], d.dijks[2][1].id)
# print(d.dijks[3][0], d.dijks[3][1].id)
# print(d.dijks[4][0], d.dijks[4][1].id)
# print(d.dijks[5][0], d.dijks[5][1].id)
# print(d.dijks[6][0], d.dijks[6][1].id)
