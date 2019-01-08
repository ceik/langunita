
from .heap_errors import NoParentError
import math


class GenericNode():
    """docstring for GenericNode"""
    def __init__(self, key, li, s):
        self.key = key
        self.li = li
        self.s = s

    def get_key(self):
        return self.key


class MyHeap():
    """docstring for MyHeap"""
    def __init__(self, list_of_nodes):
        self.nodes = list_of_nodes

    def heapify():
        pass

    def get_node(self, i):
        return self.nodes[i-1]

    def get_parent(self, i):
        """Returns the parent of the element at position i."""
        if i <= 0:
            raise ValueError('%s is not a valid position' % i)
        elif i == 1:
            raise NoParentError()
        elif i > len(self.nodes):
            raise IndexError('this heap has no element at position %s' % i)
        else:
            return self.get_node(i//2), i//2

    def get_left_child_data(self, i):
        """ Returns the key and position of the left child node of the node at
        position i."""
        if i <= 0:
            raise ValueError('%s is not a valid position' % i)
        elif i > len(self.nodes):
            raise IndexError('this heap has no element at position %s' % i)
        elif (i*2) > len(self.nodes):
            raise IndexError('%s has no left child' % i)
        else:
            return self.get_node(i*2).get_key(), i*2

    def get_right_child_data(self, i):
        """ Returns the key and position of the right child node of the node at
        position i."""
        if i <= 0:
            raise ValueError('%s is not a valid position' % i)
        elif i > len(self.nodes):
            raise IndexError('this heap has no element at position %s' % i)
        elif (i*2)+1 > len(self.nodes):
            raise IndexError('%s has no right child' % i)
        else:
            return self.get_node(i*2+1).get_key(), i*2+1

    def insert(self, n):
        self.nodes.append(n)
        new_node_pos = len(self.nodes)
        new_node_key = n.get_key()

        try:
            parent_node, parent_node_pos = self.get_parent(new_node_pos)
            parent_node_key = parent_node.get_key()
        except NoParentError:
            return

        while new_node_key < parent_node_key:
            new_node_pos = self.bubble_up(new_node_pos)
            try:
                parent_node, parent_node_pos = self.get_parent(new_node_pos)
                parent_node_key = parent_node.get_key()
            except NoParentError:
                return
            # break

    def extract_min(self):
        """ Return the node at the root position and restore the heap
        property."""
        min_node = self.nodes[0]

        moving_node = self.nodes[len(self.nodes) - 1]
        self.nodes[0] = moving_node
        self.nodes.pop()

        moving_node_key = moving_node.get_key()
        moving_node_pos = 1

        try:
            left_child_key, left_child_pos = self.get_left_child_data(
                moving_node_pos)
        except IndexError:
            left_child_key, left_child_pos = math.inf, math.inf
        try:
            right_child_key, right_child_pos = self.get_right_child_data(
                moving_node_pos)
        except IndexError:
            right_child_key, right_child_pos = math.inf, math.inf

        while moving_node_key > left_child_key or \
                moving_node_key > right_child_key:

            if left_child_key < right_child_key:
                target_pos = left_child_pos
            else:
                target_pos = right_child_pos

            moving_node_pos = self.bubble_down(moving_node_pos, target_pos)

            try:
                left_child_key, left_child_pos = self.get_left_child_data(
                    moving_node_pos)
            except IndexError:
                left_child_key, left_child_pos = math.inf, math.inf
            try:
                right_child_key, right_child_pos = self.get_right_child_data(
                    moving_node_pos)
            except IndexError:
                right_child_key, right_child_pos = math.inf, math.inf

        return min_node

    def bubble_down(self, moving_node_pos, target_pos):
        if target_pos <= 0:
            raise ValueError('%s is not a valid position' % target_pos)
        elif target_pos > len(self.nodes):
            raise IndexError('this heap has no element at position %s' %
                             target_pos)

        self.nodes[moving_node_pos - 1], self.nodes[target_pos - 1] = \
            self.nodes[target_pos - 1], self.nodes[moving_node_pos - 1]

        return target_pos

    def bubble_up(self, target_pos):
        if target_pos == 0:
            raise ValueError('0 is not a valid key. Heaps are 1-indexed')
        elif target_pos == 1:
            raise NoParentError('The root node can not be bubbled up')
        parent_node, parent_pos = self.get_parent(target_pos)
        target_node = self.nodes[target_pos - 1]
        self.nodes[target_pos - 1] = self.nodes[parent_pos - 1]
        self.nodes[parent_pos - 1] = target_node
        return parent_pos
