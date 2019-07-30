#!/usr/bin/env python3

from .priority_queue import PriorityQueue
import random


class Edge():
    """ A class to represent undirected edges with weights.
    Only one end of the edges is stored here. The other end of the edge
    is the Node in which the Edge is stored.
    """
    def __init__(self, end, cost):
        self.end = end
        self.cost = cost


class Node():
    """ A class to represent nodes in a weighted, undirected graph. """
    def __init__(self, i):
        self.id = i
        self.edges = []
        self.min_cost_edge = None

    def __lt__(self, other):
        if other == '<removed>':
            other_id = 1000000
        else:
            other_id = int(other.id)
        return int(self.id) < int(other_id)

    def __gt__(self, other):
        if other == '<removed>':
            other_id = 1000000
        else:
            other_id = int(other.id)
        return int(self.id) > int(other_id)

    def append_edge(self, end, cost):
        self.edges.append(Edge(end, cost))


class PrimHeap():
    """ A class to store undirected, weighted graphs, and compute the minimum
    spanning tree using Prim's algorithm.
    """
    def __init__(self, list_of_edges):
        self.num_nodes = int(list_of_edges.pop(0)[0])
        counter = 1
        self.nodes = {}  # V
        self.processed_nodes = {}  # X
        self.remaining_nodes = PriorityQueue()  # V - X
        self.mst = {}  # T

        while counter <= self.num_nodes:
            self.nodes[counter] = Node(counter)
            counter += 1

        for n in list_of_edges:
            self.nodes[int(n[0])].append_edge(int(n[1]), int(n[2]))
            self.nodes[int(n[1])].append_edge(int(n[0]), int(n[2]))

    def comp_mst(self):
        """ Compute the minimum spanning tree for this PrimHeap. """

        counter = 1
        start = random.randint(1, self.num_nodes)

        self.processed_nodes[start] = self.nodes[start]
        self.init_prim(start)
        num_nodes = len(self.remaining_nodes.pq)

        while counter <= num_nodes:
            curr_cost, curr_node = self.remaining_nodes.pop()
            self.mst[counter] = curr_node.min_cost_edge
            self.processed_nodes[curr_node.id] = curr_node
            self.update_costs(curr_node)
            counter += 1

        return

    def init_prim(self, start):
        """ Initialize remaining_nodes priority queue with all nodes except the
        start.
        """
        for n in self.nodes.items():
            if n[0] == start:
                continue
            node_cost = self.calc_cost(n[1])
            self.remaining_nodes.add(n[1], node_cost)

    def update_costs(self, moved_node):
        """ Update the cost of the remaining_nodes affected by processing
        moved_node.
        """
        for e in moved_node.edges:
            if e.end not in self.processed_nodes:
                curr_node = self.nodes[e.end]
                self.remaining_nodes.remove(curr_node)
                new_cost = self.calc_cost(curr_node)
                self.remaining_nodes.add(curr_node, new_cost)

    def calc_cost(self, node):
        """ Returns the current cost of adding the node to the MST. If there is
        an edge that spans the two cuts, that edge is also set as the
        min_cost_edge of the node.
        """
        min_cost = 1000000  # Arbitrary high value
        for e in node.edges:
            if e.end in self.processed_nodes:
                if e.cost < min_cost:
                    min_cost = e.cost
                    node.min_cost_edge = e
        return min_cost
