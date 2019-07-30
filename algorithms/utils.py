

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


def load_tab_delimited_file(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            cleanline = line.rstrip()
            arr.append(cleanline.split("\t"))
    return arr


def load_space_delimited_file(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            cleanline = line.rstrip()
            arr.append(cleanline.split(" "))
    return arr


def load_space_delimited_file_ints(filename):
    with open(filename) as f:
        arr = [[int(n) for n in line.split()] for line in f]
    return arr


def load_space_delimited_file_floats(filename):
    with open(filename) as f:
        arr = [[float(n) for n in line.split()] for line in f]
    return arr
