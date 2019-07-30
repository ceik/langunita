#!/usr/bin/env python3

import math
import itertools
# from .bellman_ford import BellmanFord
# from .dijkstra import Dijkstra


class Tsp:
    def __init__(self, num_nodes, data):
        self.num_nodes = num_nodes
        self.nodes = []

        for n in range(num_nodes):
            self.nodes.append({})

        for e in data:
            self.nodes[e[0] - 1][e[1] - 1] = e[2]

        print(self.nodes)

    def tsp(self, start, curr_set):
        tsp_data = {}
        # print(curr_set, ':')

        # Base Case
        if len(curr_set) == 2:
            val = self.nodes[curr_set[0]][curr_set[1]]
            if curr_set[0] == start:
                last_node = curr_set[1]
            else:
                last_node = curr_set[0]
            tsp_data[last_node] = val
            # print(curr_set, ':', tsp_data)
            return tsp_data

        for last_node in curr_set:
            if last_node == start:
                continue
            prev_set = curr_set.copy()
            prev_set.remove(last_node)
            prev_data = Tsp.tsp(self, start, prev_set)

            for e in prev_data:
                prev_data[e] += self.nodes[e][last_node]
            sec_last_node = min(prev_data, key=prev_data.get)
            prev_set_min = prev_data[sec_last_node]
            tsp_data[last_node] = prev_set_min

        # print(curr_set, ':', tsp_data)
        return tsp_data

    def main(self):

        data_by_start = {}
        for start in range(self.num_nodes):
            curr_data = Tsp.tsp(self, start, list(range(self.num_nodes)))
            data_by_start[start] = min(curr_data.values())
            # print(start, curr_data, min(curr_data.values()))
        return min(data_by_start.values())
