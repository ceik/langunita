#!/usr/bin/env python3

import utils
from selection import random_select
from selection import deterministic_select

# data = utils.load_array_from_file('data/QuickSort.txt')
data = utils.create_reversed_array(401)
# data = [1, 5, 4, 3, 6]

# print(random_select.rselect(data, 1))
# print(random_select.rselect(data, 2))
# print(random_select.rselect(data, 3))
# print(random_select.rselect(data, 4))
# print(random_select.rselect(data, 5))

print(deterministic_select.dselect(data, 10))
print(deterministic_select.dselect(data, 20))
print(deterministic_select.dselect(data, 30))
print(deterministic_select.dselect(data, 40))
print(deterministic_select.dselect(data, 50))
