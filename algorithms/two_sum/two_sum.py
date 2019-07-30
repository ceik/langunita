#!/usr/bin/env python3


def two_sum(nums, target):
    ht = {}
    y = None
    for n in nums:
        ht[n] = n

    for x in nums:
        try:
            y = ht[target - x]
            break
        except KeyError:
            pass

    return y is not None


def two_sum_array(nums, target):
    ht = {}
    y = None
    matches = 0
    counter = target[0]
    for n in nums:
        ht[n] = n

    while counter != target[1] + 1:
        print(counter)
        y = 0
        for x in nums:
            try:
                y = ht[counter - x]
                matches += 1
                break
            except KeyError:
                continue

        counter += 1

    return matches
