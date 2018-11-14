import utils
# from merge_sort import merge_sort
from quick_sort import quick_sort
from quick_sort import quick_sort_with_count

data = utils.load_array_from_file('data/QuickSort.txt')
# data = utils.create_reversed_array(5)
# data = [1, 5, 4, 3, 6]

# print(quick_sort.quick_sort(data))
print(quick_sort_with_count.quick_sort(data))
