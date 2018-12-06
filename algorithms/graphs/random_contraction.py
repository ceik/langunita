#!/usr/bin/env python3

from copy import deepcopy
import random


class Graph():
    """A class to represent graphs via the adjacency list approach. Each
    dictionary entry is a node, storing all the edges that touch it in a
    list."""

    def __init__(self, list_of_node_arrays):
        self.nodes = {}

        for n in list_of_node_arrays:
            self.nodes[n[0]] = n[1:]

    def find_min_cut(self):
        min_cut = 0

        # n = len(self.nodes) * len(self.nodes)
        n = 1000

        # run rcontract n times and update min_cut if a lower value was found
        for i in range(n):
            copy = deepcopy(self)
            new_cut = copy.contract_fully()
            if min_cut == 0:
                min_cut = new_cut
            else:
                min_cut = min(min_cut, new_cut)

        del copy
        return min_cut

    def contract_fully(self):
        """ Run contract_graph until left with 2 nodes, then return the number
        of edges between them."""
        while len(self.nodes) > 2:
            self.contract_graph()

        return len(self.nodes[next(iter(self.nodes))])

    def contract_graph(self):
        """Pick a random edge and merge it's nodes into one node."""

        node1, node2 = self.select_rand_edge()

        # Remove all edges with node2 from node1, since they would be
        # self-references later
        while node2 in self.nodes[node1]:
            self.nodes[node1].remove(node2)

        # Add all the edges from node2 to node1, unless they would be a
        # self-reference
        for e in self.nodes[node2]:
            if e != node1:
                self.nodes[node1].append(e)

        for n in self.nodes.values():
            # print(n)
            while node2 in n:
                n.remove(node2)
                n.append(node1)

        # Remove node2
        del self.nodes[node2]

    def select_rand_edge(self):
        """Randomly selects an entry from all the list-type values of a dict.
        Returns the key to which the list of the value belongs, and the value
        itself."""

        # Establish the total number of values. A value is an edge stored in a
        # node. This means each node is counted twice here, once on each edge
        # it is connecting.
        total_len = 0
        for v in self.nodes.values():
            total_len += len(v)

        # Generate random offset value
        offset = random.randint(1, total_len)

        # If the offset value falls within the values of a node, return that
        # node and the edge. Put differently, this approach is like lining up
        # all the values and returning the offset'th value and the node it sits
        # in
        running_len = 0
        for k, v in self.nodes.items():
            if offset <= running_len + len(v):
                internal_offset = offset - running_len - 1
                return k, v[internal_offset]
            running_len += len(v)
