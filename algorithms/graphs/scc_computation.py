#!/usr/bin/env python3

import heapq


class Node():
    """A class to represent nodes in a DirectedGraph. It has attributes for
    performing DFS."""

    def __init__(self, i):
        self.id = i
        self.edges = []
        self.rev_edges = []
        self.explored = False
        self.fin_time = 0
        self.leader = 0

    def add_edge(self, edge_id):
        self.edges.append(edge_id)

    def add_rev_edge(self, edge_id):
        self.rev_edges.append(edge_id)

    def mark_explored(self):
        self.explored = True

    def set_leader(self, leader_id):
        self.leader = leader_id

    def set_fin_time(self, fin_time):
        self.fin_time = fin_time


class DirectedGraph():
    """A class to represent directed graphs via the adjacency list approach.
    Each dictionary entry is a Node."""

    def __init__(self, length, list_of_edges):
        self.nodes = {}
        self.nodes_by_fin_time = {}
        self.length = length
        self.fin_time = 0  # counter for the finishing time
        self.fin_time_2 = length  # counter for the finishing time
        self.leader_count = 0  # counter for the size of leader nodes
        self.scc_heapq = []  # heapq to store the ssc by size

        for n in range(1, length + 1):
            self.nodes[str(n)] = Node(str(n))

        for n in list_of_edges:
            ns = n[0].split(' ')
            self.nodes[ns[0]].add_edge(ns[1])
            self.nodes[ns[1]].add_rev_edge(ns[0])

    def n_largest_sccs(self, n):
        """Can only be run after compute_sscs."""
        return heapq.nlargest(n, self.scc_heapq)

    def compute_sccs(self):
        """First compute the finishing times and the resulting order of nodes
        via a DFS loop. Second use that new order to compute the SCCs and order
        them by their size."""

        # Go through the given graph in reverse order, computing the finishing
        # times of each node, and create a second graph that uses the finishing
        # times as the IDs.
        i = self.length
        while i > 0:
            node = self.nodes[str(i)]
            if not node.explored:
                self.dfs_fin_times(str(i))
            i -= 1

        # Populate the edges of the nodes_by_fin_time
        for n in self.nodes.values():
            for e in n.edges:
                e_head_fin_time = self.nodes[e].fin_time
                self.nodes_by_fin_time[n.fin_time].add_edge(e_head_fin_time)

        # Use the nodes ordered by finishing times to calculate the SCCs.
        i = self.length
        while i > 0:
            self.leader_count = 0
            node = self.nodes_by_fin_time[str(i)]
            if not node.explored:
                self.dfs_leaders(str(i))

            heapq.heappush(self.scc_heapq, (self.leader_count, node.id))
            i -= 1

    def dfs_fin_times(self, start_node_id):
        stack = [self.nodes[start_node_id]]
        while len(stack) > 0:
            curr_node = stack.pop()
            curr_node.mark_explored()
            curr_node.set_fin_time(self.fin_time_2)
            self.fin_time_2 -= 1
            for e in curr_node.rev_edges:
                if not self.nodes[e].explored:
                    stack.append(self.nodes[e])

    def dfs_leaders(self, start_node_id):
        curr_node = self.nodes_by_fin_time[start_node_id]
        curr_node.mark_explored()
        for e in curr_node.edges:
            if not self.nodes_by_fin_time[e].explored:
                self.dfs_leaders(e)

        self.leader_count += 1

    def dfs_fin_times_rec(self, start_node_id):
        curr_node = self.nodes[start_node_id]
        curr_node.mark_explored()
        for e in curr_node.rev_edges:
            if not self.nodes[e].explored:
                self.dfs_fin_times(e)

        self.fin_time += 1
        curr_node.fin_time = str(self.fin_time)
        self.nodes_by_fin_time[str(self.fin_time)] = Node(str(self.fin_time))

    def dfs_fin_times_tail(self, start_node_id):
        curr_node = self.nodes[start_node_id]
        curr_node.mark_explored()
        curr_node.set_fin_time(self.fin_time_2)
        self.fin_time_2 -= 1
        for e in curr_node.rev_edges:
            if not self.nodes[e].explored:
                self.dfs_fin_times_tail(e)

