#!/usr/bin/env python3

import utils
from clustering import kruskal

data = utils.load_space_delimited_file('data/clusteringData1_test1.txt')

# print(data)

num_nodes = int(data.pop(0)[0])

x = kruskal.krustering(num_nodes, data, 4)

print(x)
# print(x.cluster_count)

# for n in x.nodes.items():
#     print(n[1].id)
