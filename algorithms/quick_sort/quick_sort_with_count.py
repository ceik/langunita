#!/usr/bin/env python3

# Contains garbage code for the assignment. See quick_sort.py for proper
# implementation


def quick_sort(arr):
    global counter
    counter = 0
    # Using a global variable to make it more memory efficient
    global A
    A = arr

    left = 0
    right = len(A) - 1

    # Median of 3 Pivot
    x = []
    x.append(A[left])
    x.append(A[right])
    mid = (right - left) // 2
    x.append(A[mid])
    x.sort()
    pivot = A.index(x[1])

    pivot = partition(pivot, left, right)

    if pivot - left > 1:
        rec_sort(left, pivot - 1)
    if right - pivot > 1:
        rec_sort(pivot + 1, right)

    return counter


def partition(pivot, left, right):
    global A
    global counter

    counter += (right - left)

    # Swap pivot to first position
    A[left], A[pivot] = A[pivot], A[left]

    # Partition
    j = left + 1
    i = left + 1
    while i <= right:
        if A[i] < A[left]:
            A[j], A[i] = A[i], A[j]
            j += 1
        i += 1

    # Swap pivot into right spot
    A[left], A[j - 1] = A[j - 1], A[left]

    # Return position that pivot was swapped into
    return (j - 1)


def rec_sort(left, right):
    global A

    # Median of 3 Pivot
    x = []
    x.append(A[left])
    x.append(A[right])
    x.append(A[(right + left) // 2])
    x.sort()
    pivot = A.index(x[1])

    pivot = partition(pivot, left, right)

    if pivot - left > 1:
        rec_sort(left, pivot - 1)
    if right - pivot > 1:
        rec_sort(pivot + 1, right)
