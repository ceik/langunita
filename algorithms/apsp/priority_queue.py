#!/usr/bin/env python3

import heapq


class PriorityQueue(object):
    """ Priority Queue class for Dijkstra's algorithm."""

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed>'

    def add(self, node, priority):
        """ Adds a node to the priority queue and the entry finder."""
        entry = [priority, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.pq, entry)

    def update(self, node, priority):
        """ Marks a node as removed and reinserts it with a new priority value.
        """
        if node in self.entry_finder:
            self.remove(node)
            self.add(node, priority)
            return
        raise KeyError("The node you're trying to update doesn't exist")

    def remove(self, node):
        """ Marks the node as removed. Marked nodes are skipped in the pop
        method. This approach prevents breaking the heap property when
        'removing' a node.
        """
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
        return entry[0]

    def pop(self):
        """ Pop the lowest priority non-removed node from pq."""
        while self.pq:
            priority, node = heapq.heappop(self.pq)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return (priority, node)
        raise KeyError("Can't pop from an empty Priority Queue")
