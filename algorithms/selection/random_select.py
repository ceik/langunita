#!/usr/bin/env python3

import random


def rselect(arr, i, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # base case
    if right - left < 1:
        return arr[left]

    pivot = random.randrange(left, right)
    pivot = partition(arr, pivot, left, right)

    if pivot == i - 1:
        return arr[pivot]
    if pivot > i - 1:
        return rselect(arr, i, left, pivot - 1)
    if pivot < i - 1:
        return rselect(arr, i, pivot + 1, right)


def partition(arr, pivot, left, right):
    # Swap pivot to first position
    arr[left], arr[pivot] = arr[pivot], arr[left]

    # Partition
    j = left + 1
    i = left + 1
    while i <= right:
        if arr[i] < arr[left]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1

    # Swap pivot into right spot
    arr[left], arr[j - 1] = arr[j - 1], arr[left]

    # Return position that pivot was swapped into
    return (j - 1)
