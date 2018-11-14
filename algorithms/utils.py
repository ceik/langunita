

def create_reversed_array(n):
    arr = []
    for i in range(n, -1, -1):
        arr.append(i)

    return arr


def load_array_from_file(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            arr.append(int(line.rstrip()))
    return arr
