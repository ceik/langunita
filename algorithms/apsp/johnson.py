#!/usr/bin/env python3

import math
from .bellman_ford import BellmanFord
from .dijkstra import Dijkstra


class Johnson:
    def __init__(self, num_nodes, num_edges, data):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.edges = data
        self.nodes = []

    def all_pairs_shortest_path(self):
        """ Returns the cost value of the shortest path from any node to any
        other node.
        """

        # Add edges from fake node for BF neg cycle detection
        for i in range(1, self.num_nodes + 1):
            self.edges.append([self.num_nodes + 1, i, 0])

        bf = BellmanFord(self.num_nodes + 1, self.num_edges + self.num_nodes,
                         self.edges)

        node_weights = bf.shortest_path(self.num_nodes + 1)

        if not node_weights:
            print('neg cycle!')
            return 'neg cycle!'

        # Remove edges to fake node
        check = self.edges[-1][0] == self.num_nodes + 1
        while check:
            self.edges.pop()
            check = self.edges[-1][0] == self.num_nodes + 1

        # Reweight edges
        for e in self.edges:
            e[2] = e[2] + node_weights[e[0] - 1] - node_weights[e[1] - 1]
        print(node_weights)
        print(self.edges)

        # Populate the nodes list in a format that is usable by our Dijkstra
        # implementation.
        for n in range(1, self.num_nodes + 1):
            edge_list = []
            for e in self.edges:
                if e[0] == n:
                    edge_list.append(e[1:])
            self.nodes.append([n, edge_list])

        dijk = Dijkstra(self.nodes)

        min_path = math.inf
        for node in range(0, self.num_nodes):
            print('bf:', node + 1)
            dijk.comp_sps(node)
            for x in dijk.shortest_paths:
                dijk.shortest_paths[x] = (dijk.shortest_paths[x] -
                                          node_weights[node] +
                                          node_weights[x - 1])
            min_path = min(min_path, min(dijk.shortest_paths.values()))

        return min_path
