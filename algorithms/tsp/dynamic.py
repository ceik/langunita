#!/usr/bin/env python3

from math import pow, sqrt


class Tsp:
    def __init__(self, num_nodes, data):
        self.num_nodes = num_nodes
        self.nodes = []
        self.cache = []

        for n in range(num_nodes):
            self.nodes.append({})
            self.cache.append({})
            for e in range(num_nodes):
                if e == n:
                    continue
                x1 = data[n][0]
                y1 = data[n][1]
                x2 = data[e][0]
                y2 = data[e][1]
                val = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
                self.nodes[n][e] = val
                if n < e:
                    self.cache[n][tuple((n, e))] = {e: val}
                else:
                    self.cache[n][tuple((e, n))] = {e: val}

    def tsp(self, curr_set):
        tsp_data = {}

        for last_node in curr_set:
            if last_node == 0:
                continue
            prev_set = curr_set.copy()
            prev_set.remove(last_node)
            try:
                prev_data = self.cache[0][tuple(prev_set)].copy()
            except KeyError:
                prev_data = Tsp.tsp(self, prev_set).copy()

            for e in prev_data:
                prev_data[e] = prev_data[e] + self.nodes[e][last_node]
            sec_last_node = min(prev_data, key=prev_data.get)
            prev_set_min = prev_data[sec_last_node]

            tsp_data[last_node] = prev_set_min

        self.cache[0][tuple(curr_set)] = tsp_data
        return tsp_data

    def main(self):
        tsp_data = Tsp.tsp(self, list(range(self.num_nodes)))
        for last_node in tsp_data:
            tsp_data[last_node] += self.nodes[last_node][0]
        lowest_cost_last_node = min(tsp_data, key=tsp_data.get)
        lowest_cost = tsp_data[lowest_cost_last_node]

        return lowest_cost
