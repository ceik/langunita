#!/usr/bin/env python3

import utils
import cProfile
from apsp import bellman_ford
from apsp import johnson

# data = utils.load_space_delimited_file_ints('data/apsp_test2.txt')
# data = utils.load_space_delimited_file_ints('data/apsp1.txt')
# data = utils.load_space_delimited_file_ints('data/apsp2.txt')
data = utils.load_space_delimited_file_ints('data/apsp3.txt')

meta_info = data.pop(0)
num_nodes = int(meta_info[0])
num_edges = int(meta_info[1])

# print(num_nodes, num_edges)
# print(data[:25])

x = johnson.Johnson(num_nodes, num_edges, data)

# x.shortest_path(1)
y = x.all_pairs_shortest_path()
print(y)
# print(x.edge_dict)

# cProfile.run("x.all_pairs_shortest_path()")
