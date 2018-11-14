import utils
# from merge_sort import merge_sort
from inversion_count import inv_count

data = utils.load_array_from_file('data/IntegerArray.txt')
# data = utils.create_reversed_array(6)
# data = [1, 5, 4, 3, 6]

print(inv_count.inv_count(data))
