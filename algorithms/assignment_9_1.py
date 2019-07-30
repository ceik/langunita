#!/usr/bin/env python3

import utils
import cProfile
import sys
from knapsack import knapsack
from knapsack import knapsack_rec

sys.setrecursionlimit(3000)
# data = utils.load_space_delimited_file_ints('data/knapsack1.txt')
data = utils.load_space_delimited_file_ints('data/knapsack2.txt')
# data = utils.load_space_delimited_file_ints('data/knapsack1_test1.txt')

meta_info = data.pop(0)
max_weight = int(meta_info[0])
num_items = int(meta_info[1])

# print(max_weight, num_items)
# print(data[:25])

# x = knapsack.find_max_value(max_weight, num_items, data)
x = knapsack_rec.Knapsack(max_weight, num_items, data)
# cProfile.run("knapsack.find_max_value(max_weight, num_items, data[:5])")
# cProfile.run("knapsack.find_max_value(max_weight, num_items, data)")

# print(x)
print(x.result)
