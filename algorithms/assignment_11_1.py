#!/usr/bin/env python3

import utils
import cProfile
from tsp import dynamic

# data = utils.load_space_delimited_file_ints('data/tsp_test.txt')
# data = utils.load_space_delimited_file_floats('data/tsp_test3.txt')
data = utils.load_space_delimited_file_floats('data/tsp.txt')

num_nodes = int(data.pop(0)[0])
starter_set = list(range(num_nodes))

# print(num_nodes)
# print(data)

x = dynamic.Tsp(num_nodes, data)

# y = x.tsp(3, [0, 1, 2, 3])
# y = x.tsp(0, starter_set)
y = x.main()
print(y)

# cProfile.run("y = x.main()")
