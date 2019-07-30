#!/usr/bin/env python3

from .priority_queue import PriorityQueue
from math import inf


class Node():
    """ A class to represent nodes in a weighted, directed graph. """
    def __init__(self, node_list):
        self.id = node_list[0]
        self.edge_dict = {}

        for e in node_list[1:][0]:
            self.edge_dict[e[0]] = e[1]

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


class Dijkstra():
    """ A class to store directed, weighted graphs, and compute the shortest
    paths (sp) between nodes using a non-recursive version of Dijkstra's
    algorithm. Assumes positive edge-weights.
    """
    def __init__(self, list_of_nodes):
        self.nodes = []
        self.processed_nodes = {}
        self.dijks = PriorityQueue()
        self.shortest_paths = {}
        self.sp_source = None

        for n in list_of_nodes:
            self.nodes.append(Node(n))

    def comp_sps(self, source):
        """ Compute the shortest paths to all nodes from the source node."""

        # If shortest paths have been computed before, reset the lists
        if self.sp_source:
            self.processed_nodes = {}
            self.shortest_paths = {}
            self.dijks = PriorityQueue()

        self.sp_source = self.nodes[source]
        self.mark_node_processed(0, self.nodes[source])
        self.init_dijks(source)
        dijk_len = len(self.dijks.pq)

        while dijk_len > 0:
            curr_cost, curr_node = self.dijks.pop()
            self.mark_node_processed(curr_cost, curr_node)
            self.update_dijks(curr_node, curr_cost)
            dijk_len -= 1

        return

    def mark_node_processed(self, curr_cost, curr_node):
        """ Adds curr_node to shortest_paths and processed_nodes."""
        self.shortest_paths[curr_node.id] = curr_cost
        self.processed_nodes[curr_node.id] = curr_node

    def init_dijks(self, source):
        """ Initialize the dijks priority queue with all nodes except the
        source.
        """
        for n in self.nodes:
            if n.id == self.sp_source.id:
                continue
            elif n.id in self.sp_source.edge_dict:
                cost = self.sp_source.edge_dict[n.id]
            else:
                cost = inf
            self.dijks.add(n, cost)

    def update_dijks(self, moved_node, moved_node_cost):
        """ Update the keys of the dijks affected by processing curr_node."""
        for e in moved_node.edge_dict.items():
            if e[0] not in self.processed_nodes:
                curr_node = self.nodes[int(e[0]) - 1]
                curr_node_cost = self.dijks.remove(curr_node)
                new_cost = min(curr_node_cost, moved_node_cost + e[1])
                self.dijks.add(curr_node, new_cost)
