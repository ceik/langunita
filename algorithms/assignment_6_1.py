#!/usr/bin/env python3

import utils
from two_sum import two_sum

data = utils.load_array_from_file('data/2sumData.txt')

# print(data)

r = two_sum.two_sum(data, 0)

# print(r[89179175621])
# print(r[-60012933873])
# print(r[123])

# print(two_sum.two_sum(data, 46914128793))  # First two nums
# print(two_sum.two_sum(data, 78454312159))  # Two pos nums at end
# print(two_sum.two_sum(data, -22612200037))  # Two neg nums at end
# print(two_sum.two_sum(data, -29840435009))  # -55970782580+26130347571
# print(two_sum.two_sum(data, 0))

print(two_sum.two_sum_array(data, [-10000, 10000]))

# print(r)
