#!/usr/bin/env python3

import utils
import cProfile
from clustering import hamming

data = utils.load_space_delimited_file_ints('data/clusteringData2.txt')

meta_info = data.pop(0)
num_nodes = int(meta_info[0])
node_len = int(meta_info[1])

# print(num_nodes, node_len)
# print(data[:25])

x = hamming.min_space_cluster(num_nodes, data, node_len)
# cProfile.run("hamming.min_space_cluster(num_nodes, data, node_len)")

print(x)
# print(x.cluster_count)

# # Find duplicates
# for n in range(num_nodes):
#     p = data.pop(0)
#     if p in data:
#         print(p)

# duplicates:
# [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]

# wrong:
# 7510
# 7330
# 6150