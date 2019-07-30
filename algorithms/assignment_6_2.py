#!/usr/bin/env python3

import utils
from median import median

data = utils.load_array_from_file('data/MedianData.txt')

# print(data)

m = median.accum_medians(data)

print(m)
