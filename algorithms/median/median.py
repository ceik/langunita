#!/usr/bin/env python3

from heapq import heappush, heappop


def accum_medians(nums):
    s = 0
    lows = []
    highs = []

    n1, n2 = nums.pop(0), nums.pop(0)
    heappush(highs, max(n1, n2))
    heappush(lows, -min(n1, n2))
    s += n1 + min(n1, n2)

    for n in nums:
        len_lows = len(lows)
        len_highs = len(highs)
        candidates = [n, -heappop(lows), heappop(highs)]
        candidates.sort(key=int)

        heappush(highs, candidates.pop(-1))
        heappush(lows, -candidates.pop(0))
        if len_highs >= len_lows:
            heappush(lows, -candidates.pop(0))
        else:
            heappush(highs, candidates.pop(0))

        s += -lows[0]

    return s
