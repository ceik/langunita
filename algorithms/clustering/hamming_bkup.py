#!/usr/bin/env python3

from .union_find import UnionFindDictLazyComp
# import time


def min_space_cluster(num_nodes, node_list, bits_per_node, s):
    """ Returns the largest value k so that there is a k-clustering with
    spacing at least s.
    Nodes are bits_per_node long and it is assumed that every node has an edge
    with every other node. The cost of that edge is defined by the Hamming
    distance of the two nodes.
    Currently only 2 and 3 are supported for s.
    """

    if s not in [2, 3]:
        return

    k = num_nodes
    counter = num_nodes
    # nodes = [c + 1 for c in range(num_nodes)]
    uf = UnionFindDictLazyComp(node_list)

    # st = "get_similar_hams(uf, bits_per_node, node_list[0], s)"

    # timeit.timeit(st, setup="uf=uf; bits_per_node=24; s=3;", globals=globals())

    for n in node_list:
        # start = time.time()
        # start_k = k
        # print(k)
        # print(n)
        similars = get_similar_hams(uf, bits_per_node, n, s)
        similars.append(n.copy())
        # print('similars:')
        # print(similars)

        for sim in similars:
            # unioned_clusters = uf.union(sim, n)
            # k -= unioned_clusters
            try:
                uf.find(sim)
                # print('matched: ', sim)
                unioned_clusters = uf.union(sim, n)
                k -= unioned_clusters
            except KeyError:
                pass

        counter -= 1
        print(counter)
        # print('total time', time.time() - start)
        # try:
        #     print('time per k', (time.time() - start) / (start_k - k))
        # except ZeroDivisionError:
        #     print('time per k', 0)

    return k


def get_similar_hams(uf, bits_per_node, n, s):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of s of the original node n.
    """
    node = uf.find(str(n))
    hams = []
    # ham_set = set()

    # 1 bit changed
    for b in range(bits_per_node):
        new_b = node.copy()
        new_b[b] = 1 - new_b[b]

        # Another loop if needed
        # temp_hams = []

        for c in range(bits_per_node):
            if c == b:
                continue
            new_c = new_b.copy()
            new_c[c] = 1 - new_c[c]
            hams.append(new_c)
            # try:
            #     uf.find(new_c)
            #     # hams.append(new_c)
            #     if str(new_c) not in ham_set:
            #         ham_set.add(str(new_c))
            #         hams.append(new_c)

            # except KeyError:
            #     pass

        hams.append(new_b)
        # try:
        #     uf.find(new_b)
        #     # hams.append(new_b)
        #     if str(new_b) not in ham_set:
        #         ham_set.add(str(new_b))
        #         hams.append(new_b)
        # except KeyError:
        #     pass

    return hams


def get_similar_hams_bkp3(uf, bits_per_node, n, s):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of s of the original node n.
    """
    node = uf.find(str(n))
    hams = []
    ham_set = set()

    # 1 bit changed
    for b in range(bits_per_node):
        new_b = node.copy()
        new_b[b] = 1 - new_b[b]

        # Another loop if needed
        # temp_hams = []

        for c in range(bits_per_node):
            if c == b:
                continue
            new_c = new_b.copy()
            new_c[c] = 1 - new_c[c]
            try:
                uf.find(new_c)
                # hams.append(new_c)
                if str(new_c) not in ham_set:
                    ham_set.add(str(new_c))
                    hams.append(new_c)

            except KeyError:
                pass

        # Add new values to hams unless they have already been added
        # for h in temp_hams:
        #     if str(h) not in ham_set:
        #         ham_set.add(str(h))
        #         hams += [h]

        try:
            uf.find(new_b)
            # hams.append(new_b)
            if str(new_b) not in ham_set:
                ham_set.add(str(new_b))
                hams.append(new_b)
        except KeyError:
            pass

    return hams


def get_similar_hams_bkp2(uf, bits_per_node, n, s):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of s of the original node n.
    """
    node = uf.find(str(n))
    hams = []
    ham_set = set()

    # 1 bit changed
    for b in range(bits_per_node):
        new_b = node.copy()
        new_b[b] = 1 - new_b[b]

        # Another loop if needed
        if s == 3:
            temp_hams = []

            for c in range(bits_per_node):
                if c == b:
                    continue
                new_c = new_b.copy()
                new_c[c] = 1 - new_c[c]
                temp_hams.append(new_c)

            # Add new values to hams unless they have already been added
            for h in temp_hams:
                if str(h) not in ham_set:
                    ham_set.add(str(h))
                    hams.append(h)

        hams.append(new_b)

    return hams


def get_similar_hams_bkp(uf, bits_per_node, n, s):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of s of the original node n.
    """
    node = uf.find(str(n))
    hams = []
    hams_1 = []
    ham_set = set()

    # 1 bit changed
    for b in range(bits_per_node):
        hams_1.append(node.copy())
        hams_1[b][b] = 1 - hams_1[b][b]

        # Another loop if needed
        if s == 3:
            temp_hams = []

            for c in range(bits_per_node):
                temp_hams.append(hams_1[b].copy())
                temp_hams[c][c] = 1 - temp_hams[c][c]
            # print(len(temp_hams))

            # Removing the node that would have been equal to the initial node
            temp_hams.pop(b)

            # Add new values to hams unless they have already been added
            for h in temp_hams:
                check = str(h) not in ham_set
                if check:
                    ham_set.add(str(h))
                    hams += [h]
                    # print(h)

    # print(len(hams))
    return hams


def get_similar_hams_debug(uf, bits_per_node, n, s):
    """ Calculates and returns in a list all the possible nodes that are within
    Hamming distance of s of the original node n.
    """

    node = uf.find(n)
    hams = []
    hams_1 = []

    # 1 bit changed
    for b in range(bits_per_node):
        hams_1.append(node.copy())
        # print('old', hams_1[b])
        hams_1[b][b] = 1 - hams_1[b][b]
        # print('new', hams_1[b])
        # print('----------------')

        # Another loop if needed
        if s == 3:
            temp_hams = []

            for c in range(bits_per_node):
                temp_hams.append(hams_1[b].copy())
                # print('old', temp_hams[c])
                temp_hams[c][c] = 1 - temp_hams[c][c]
                # print('new', temp_hams[c])

            # print('----------------')
            # for h in temp_hams:
            #     print(h)

            temp_hams.pop(b)

            # print('----------------')
            # for h in temp_hams:
            #     print(h)

            # print('----------------')

            hams += temp_hams

    for h in hams:
        print(h)
    # print(hams)

    return hams





