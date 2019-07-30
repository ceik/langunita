#!/usr/bin/env python3

from .union_find import UnionFind
from heapq import heapify, heappop


def krustering(num_nodes, edges, k):
    """ Returns a max-spacing clustering with k clusters of the data given by
    the number of nodes and the list of edges, that take the form [x, y, cost].
    This assumes nodes to be named in consecutive numbers, starting at 1.
    """

    uf = UnionFind([c + 1 for c in range(num_nodes)])

    edge_heap = [(int(e[2]), e[0], e[1]) for e in edges]

    heapify(edge_heap)

    while uf.cluster_count > k:
        cost, end1, end2 = heappop(edge_heap)
        uf.union(int(end1), int(end2))

    next_cost = cost
    same_cluster = True
    while cost == next_cost or same_cluster:
        next_cost, end1, end2 = heappop(edge_heap)
        same_cluster = uf.find(int(end1)) == uf.find(int(end2))

    return uf.mapping, uf.cluster_count, next_cost
