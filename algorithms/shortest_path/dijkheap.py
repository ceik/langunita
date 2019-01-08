#!/usr/bin/env python3

from .priority_queue import PriorityQueue


class Edge():
    """ A class to represent undirected edges with weights.
    Only one end of the edges is stored here. The other end of the edge
    is the Node in which the Edge is stored.
    """
    def __init__(self, edge_data):
        edge_list = edge_data.split(',')
        self.end = edge_list[0]
        self.length = edge_list[1]


class Node():
    """ A class to represent nodes in a weighted, undirected graph. """
    def __init__(self, node_list):
        self.id = node_list[0]
        self.edges = []

        for e in node_list[1:]:
            self.edges.append(Edge(e))

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


class DijkHeap():
    """ A class to store undirected, weighted graphs, and compute the shortest
    paths (sp) between nodes using Dijkstra's algorithm.
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
            curr_dist, curr_node = self.dijks.pop()
            self.mark_node_processed(curr_dist, curr_node)
            self.update_dijks(curr_node)
            dijk_len -= 1

        return

    def update_dijks(self, moved_node):
        """ Update the keys of the dijks affected by processing curr_node."""
        for e in moved_node.edges:
            if e.end not in self.processed_nodes:
                curr_node = self.nodes[int(e.end) - 1]
                self.dijks.remove(curr_node)
                new_dist = self.comp_dist(curr_node)
                self.dijks.add(curr_node, new_dist)

    def mark_node_processed(self, curr_dist, curr_node):
        """ Adds curr_node to shortest_paths and processed_nodes."""
        self.shortest_paths[curr_node.id] = curr_dist
        self.processed_nodes[curr_node.id] = curr_node

    def init_dijks(self, source):
        """ Initialize the dijks priority queue with all nodes except the
        source.
        """
        for n in self.nodes:
            if int(n.id) == source + 1:
                continue
            dist = self.comp_dist(n)
            self.dijks.add(n, dist)

    def comp_dist(self, n):
        """ Returns the shortest distance between Node n and the source Node.
        As per the specs, if there is no direct edge between n and any Node
        that has already been processed, the distance is set to 1000000.
        """
        shortest_dist = 1000000
        for e in n.edges:
            if e.end in self.processed_nodes:
                end_dist = self.shortest_paths[e.end]
                shortest_dist = min(shortest_dist, end_dist + int(e.length))
        return shortest_dist
