#!/usr/bin/env python3


def dselect(arr, i, left=0, right=None):
    # print(arr, left, right)
    if right is None:
        right = len(arr) - 1

    # base case
    if right - left < 1:
        return arr[left]

    m = median_of_fives(arr[left:right])
    len_m = len(m)
    if len_m % 2 == 1:
        len_m += 1
    pivot = arr.index(dselect(m, len_m // 2))

    pivot = partition(arr, pivot, left, right)

    if pivot == i - 1:
        return arr[pivot]
    if pivot > i - 1:
        return dselect(arr, i, left, pivot - 1)
    if pivot < i - 1:
        return dselect(arr, i, pivot + 1, right)


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


def median_of_fives(arr):
    # divide the array into groups of 5
    n = len(arr)
    no_groups = n // 5
    remainder = n % 5
    medians = []

    # add the median for each of the groups to the array medians
    # print(n, no_groups, remainder)
    for i in range(no_groups):
        x = arr[0 + i * 5:5 + i * 5]
        x.sort()
        # print(x)
        medians.append(x[2])

    # add the median of the remainder to the array medians
    if remainder > 0:
        x = arr[no_groups * 5:]
        x.sort()
        len_x = len(x)
        if len_x == 1 or len_x == 2:
            medians.append(x[0])
        elif len_x == 3 or len_x == 4:
            medians.append(x[1])
        else:
            medians.append(x[2])

    return medians
