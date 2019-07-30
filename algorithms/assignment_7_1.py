#!/usr/bin/env python3

import utils
from greedy_scheduler import weighted_comp_times

data = utils.load_space_delimited_file('data/jobs.txt')

# print(data)

x = weighted_comp_times.sort(data)

print(x)
