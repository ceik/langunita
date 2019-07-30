#!/usr/bin/env python3


def find_max_value(max_weight, num_items, data):
    """ Returns the value of the combination of items from data that maximizes
    the value, while not exceeding the max_weight.
    """

    A = []

    for i in range(num_items + 1):
        print('on ', i)
        inner = []
        for w in range(max_weight + 1):
            inner.append(rec(i, w, data, A))
        A.append(inner)

    return A[num_items][max_weight]


def rec(i, w, data, cache):
    if i <= 0 or w <= 0:
        return 0

    curr_item = data[i - 1]

    if w - curr_item[1] < 0:
        return cache[i - 1][w]
    else:
        b = cache[i - 1][w - curr_item[1]] + curr_item[0]
        return max(cache[i - 1][w], b)
