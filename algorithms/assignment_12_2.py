#!/usr/bin/env python3

import sys
import utils
import cProfile
from twosat import backtrack

print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

data = utils.load_space_delimited_file_ints('data/2sat4.txt')
# data = utils.load_space_delimited_file_ints('data/2sat_test.txt')

num_vars = int(data.pop(0)[0])

print(num_vars)
# print(data[:20])

x = backtrack.Backtrack(num_vars, data)

# y = x.tsp(3, [0, 1, 2, 3])
# y = x.tsp(0, starter_set)
# y = x.main()
# print(y)

cProfile.run("y = x.main()")
