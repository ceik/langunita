import random


def quick_sort(arr):
    # Using a global variable to make it more memory efficient
    global A
    A = arr

    left = 0
    right = len(A) - 1
    pivot = random.randrange(left, right)

    pivot = partition(pivot, left, right)

    if pivot - left > 1:
        rec_sort(left, pivot)
    if right - pivot > 1:
        rec_sort(pivot + 1, right)

    return A


def partition(pivot, left, right):
    global A

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

    pivot = random.randrange(left, right)

    pivot = partition(pivot, left, right)

    if pivot - left > 1:
        rec_sort(left, pivot)
    if right - pivot > 1:
        rec_sort(pivot + 1, right)
