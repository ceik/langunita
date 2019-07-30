#!/usr/bin/env python3

# Papadimitriou is too slow for the data set. See 12_2 for the backtracking
# approach

import utils
import cProfile
from twosat import papadimitriou


data = utils.load_space_delimited_file_ints('data/2sat5.txt')
# data = utils.load_space_delimited_file_ints('data/2sat_test.txt')

num_vars = int(data.pop(0)[0])

print(num_vars)
# print(data[:20])

x = papadimitriou.Papa(num_vars, data)

# y = x.tsp(3, [0, 1, 2, 3])
# y = x.tsp(0, starter_set)
# y = x.main()
# print(y)

cProfile.run("y = x.main()")


#1 sat
#2 sat
#3 sat
#4 sat
#5 sat
#6 sat
