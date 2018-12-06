#!/usr/bin/env python3

import utils
from graphs import random_contraction
from copy import deepcopy

data = utils.load_tab_delimited_file('data/kargerMinCut.txt')

g = random_contraction.Graph(data)

print(len(g.nodes))

print(g.find_min_cut())

# for n in g.nodes:
#     print(n)