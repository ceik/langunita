def sort(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr
    else:
        h1 = sort(arr[0: arr_len // 2])
        h2 = sort(arr[arr_len // 2:])
        return merge(h1, h2)


def merge(h1, h2):
    total_len = len(h1) + len(h2)
    return_array = []

    for i in range(total_len):
        if not h1:
            return_array.append(h2.pop(0))
        elif not h2:
            return_array.append(h1.pop(0))
        elif h1[0] < h2[0]:
            return_array.append(h1.pop(0))
        else:
            return_array.append(h2.pop(0))

    return return_array
