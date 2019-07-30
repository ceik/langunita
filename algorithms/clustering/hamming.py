#!/usr/bin/env python3

from .union_find import UnionFindDictLazyCompNum


def min_space_cluster(num_nodes, node_list, bits_per_node):
    """ Returns the largest value k so that there is a k-clustering with
    spacing at least 3.
    Nodes are bits_per_node long and it is assumed that every node has an edge
    with every other node. The cost of that edge is defined by the Hamming
    distance of the two nodes.
    """

    k = num_nodes
    counter = num_nodes
    uf = UnionFindDictLazyCompNum(node_list)

    for n in uf.mapping.items():
        print(counter)
        similars = get_similar_hams(uf, bits_per_node, n)

        for sim in similars:
            try:
                unioned_clusters = uf.union(sim, n[0])
                k -= unioned_clusters
            except KeyError:
                pass

        counter -= 1

    return k


def get_similar_hams(uf, bits_per_node, n):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of 3 of the original node n.
    """
    hams = []
    hams.extend(uf.find_ids(str(n[1][1])))

    # 1 bit changed
    for a in range(bits_per_node):
        new_bits_a = n[1][1].copy()
        new_bits_a[a] = 1 - new_bits_a[a]

        for b in range(bits_per_node):
            if b == a:
                continue
            new_bits_b = new_bits_a.copy()
            new_bits_b[b] = 1 - new_bits_b[b]
            hams.extend(uf.find_ids(str(new_bits_b)))

        hams.extend(uf.find_ids(str(new_bits_a)))

    return hams
