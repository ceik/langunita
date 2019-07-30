#!/usr/bin/env python3

import math


class BellmanFord:
    def __init__(self, num_nodes, num_edges, data):
        self.num_nodes = num_nodes
        self.num_edges = num_edges

        self.edge_dict = {}
        for n in range(1, self.num_nodes + 1):
            self.edge_dict[n] = []
        for e in data:
            self.edge_dict[e[1]].append(e)

    def shortest_path(self, s):
        """ Returns either a list of the shortest paths from s to all other
        nodes, or False if the graph contains a negative cycle.
        """
        paths = []

        # i == 0
        for node in range(1, self.num_nodes + 1):
            if node == s:
                paths.append(0)
            else:
                paths.append(math.inf)

        for i in range(1, self.num_nodes + 1):
            prev_paths = paths
            paths = []
            print('i = ', i)
            for n in range(1, self.num_nodes + 1):
                # source node
                if n == s:
                    paths.append(0)
                    continue
                # Get A
                a = prev_paths[n - 1]
                # Get B
                b = math.inf
                for v in self.edge_dict[n]:
                    b = min(b, prev_paths[v[0] - 1] + v[2])
                paths.append(min(a, b))

        # Check neg cycles
        if paths != prev_paths:
            return False
        else:
            return prev_paths
