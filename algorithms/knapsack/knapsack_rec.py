#!/usr/bin/env python3


class Knapsack:
    def __init__(self, max_weight, num_items, data):
        self.max_weight = max_weight
        self.num_items = num_items
        self.data = data
        self.cache = {}
        self.result = self.find_max_value(max_weight, num_items)

    def find_max_value(self, w, i):
        if (w, i) in self.cache:
            return self.cache[w, i]

        if i <= 0 or w <= 0:
            self.cache[(w, i)] = 0
            return 0

        curr_item = self.data[i - 1]

        a = self.find_max_value(w, i - 1)

        if curr_item[1] > w:
            self.cache[(w, i)] = a
            return a

        b = self.find_max_value(w - curr_item[1], i - 1) + curr_item[0]
        val = max(a, b)

        self.cache[(w, i)] = val
        return val
