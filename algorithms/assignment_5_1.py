
from heaps.heap_errors import NoParentError
from heaps import heap

n1 = heap.GenericNode(11, [11, 2, 3], '1abc')
n2 = heap.GenericNode(12, [12, 2, 3], '2abc')
n3 = heap.GenericNode(13, [13, 2, 3], '3abc')
n4 = heap.GenericNode(14, [14, 2, 3], '4abc')
n5 = heap.GenericNode(15, [15, 2, 3], '5abc')
n6 = heap.GenericNode(16, [16, 2, 3], '6abc')
n7 = heap.GenericNode(17, [17, 2, 3], '7abc')
n8 = heap.GenericNode(18, [18, 2, 3], '8abc')
n9 = heap.GenericNode(19, [19, 2, 3], '9abc')

test_heap = heap.MyHeap([n1, n2, n3, n4, n5, n6, n7, n8, n9])

# # Test get_parent
# print(test_heap.get_parent(2).key)
# print(test_heap.get_parent(3).key)
# print(test_heap.get_parent(4).key)
# print(test_heap.get_parent(5).key)
# print(test_heap.get_parent(8).key)
# print(test_heap.get_parent(9).key)
# try:
#     print(test_heap.get_parent(-2))
# except ValueError as e:
#     print(e)
# try:
#     print(test_heap.get_parent(10))
# except IndexError as e:
#     print(e)
# try:
#     print(test_heap.get_parent(0))
# except ValueError as e:
#     print(e)
# try:
#     print(test_heap.get_parent(1))
# except NoParentError as e:
#     print(e.msg)


# # # Test get_left_child
# print(test_heap.get_left_child(1).key)
# print(test_heap.get_left_child(2).key)
# print(test_heap.get_left_child(3).key)
# print(test_heap.get_left_child(4).key)

# try:
#     print(test_heap.get_left_child(5))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_left_child(9))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_left_child(10))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_left_child(-2))
# except ValueError as e:
#     print(e)

# try:
#     print(test_heap.get_left_child(0))
# except ValueError as e:
#     print(e)

# # Test get_right_child
# print(test_heap.get_right_child(1).key)
# print(test_heap.get_right_child(2).key)
# print(test_heap.get_right_child(3).key)
# print(test_heap.get_right_child(4).key)

# try:
#     print(test_heap.get_right_child(5))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_right_child(9))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_right_child(10))
# except IndexError as e:
#     print(e)

# try:
#     print(test_heap.get_right_child(-2))
# except ValueError as e:
#     print(e)

# try:
#     print(test_heap.get_right_child(0))
# except ValueError as e:
#     print(e)


# # Test insert
# nn1 = heap.GenericNode(20, [20, 2, 3], '10abc')
# nn2 = heap.GenericNode(13, [3, 2, 3], '3abc')
# nn3 = heap.GenericNode(16, [6, 2, 3], '6abc')
# nn4 = heap.GenericNode(1, [123, 2, 3], '6abc')

# test_heap.insert(nn1)
# test_heap.insert(nn2)
# test_heap.insert(nn3)
# test_heap.insert(nn4)

# for n in test_heap.nodes:
#     print(n.key)

# # Test bubble_up
# test_heap.bubble_up(0)
# for n in test_heap.nodes:
#     print(n.key)

# Test extract_min
for n in test_heap.nodes:
    print(n.key)

print('----')

min_node = test_heap.extract_min()
min_node = test_heap.extract_min()
min_node = test_heap.extract_min()
min_node = test_heap.extract_min()
# print(min_node.key)

print('----')

for n in test_heap.nodes:
    print(n.key)
