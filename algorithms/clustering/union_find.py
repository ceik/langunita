#!/usr/bin/env python3


class UnionFind():
    """ Implement a very basic Union Find datastructure."""

    def __init__(self, components=[]):
        self.mapping = [c for c in components]
        self.cluster_count = len(self.mapping)

    def find(self, x):
        """ Find & return the group that x belongs to."""
        return self.mapping[x - 1]

    def union(self, x, y):
        """ Merge the two groups that contain x and y."""
        if self.find(x) == self.find(y):
            return
        else:
            x_val = self.mapping[x - 1]
            y_val = self.mapping[y - 1]
            for i, v in enumerate(self.mapping):
                if v == x_val:
                    self.mapping[i] = y_val
            self.cluster_count -= 1


class UnionFindDict():
    """ Implement a very basic Union Find datastructure."""

    def __init__(self, components):
        self.cluster_count = 0
        self.mapping = {}
        for c in components:
            self.cluster_count += 1
            self.mapping[str(c)] = c

    def find(self, x):
        """ Find & return the group that x belongs to."""
        return self.mapping[str(x)]

    def union(self, x, y):
        """ Merge the two groups that contain x and y."""
        if self.find(x) == self.find(y):
            return 0
        else:
            x_val = self.mapping[str(x)]
            y_val = self.mapping[str(y)]
            # for i, v in enumerate(self.mapping):
            for i, v in self.mapping.items():
                # print(i, v)
                if v == x_val:
                    self.mapping[i] = y_val
            self.cluster_count -= 1
            return 1


class UnionFindDictLazy():
    """ Implement a basic Union Find datastructure with lazy unions."""

    def __init__(self, components):
        self.cluster_count = 0
        self.mapping = {}
        for c in components:
            self.cluster_count += 1
            self.mapping[str(c)] = c

    def find(self, x):
        """ Find & return the group that x belongs to."""
        curr_x = x
        curr_parent = self.mapping[str(curr_x)]

        while curr_x != curr_parent:
            curr_x = curr_parent
            curr_parent = self.mapping[str(curr_x)]

        return curr_parent

    def union(self, x, y):
        """ Merge the two groups that contain x and y."""
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return 0
        else:
            x_val_parent = self.mapping[str(x_parent)]
            self.mapping[str(y_parent)] = x_val_parent
            self.cluster_count -= 1
            return 1


class UnionFindDictLazyComp():
    """ Implement a basic Union Find datastructure with lazy unions and path
    compression."""

    def __init__(self, components):
        self.cluster_count = 0
        self.mapping = {}
        for c in components:
            self.cluster_count += 1
            self.mapping[str(c)] = c

    def find(self, x):
        """ Find & return the group that x belongs to."""
        curr_x = x
        curr_parent = self.mapping[str(curr_x)]
        comp_list = []

        while curr_x != curr_parent:
            comp_list.append(curr_x)
            curr_x = curr_parent
            curr_parent = self.mapping[str(curr_x)]

        for elem in comp_list:
            self.mapping[str(elem)] = curr_parent

        return curr_parent

    def union(self, x, y):
        """ Merge the two groups that contain x and y."""
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return 0
        else:
            x_val_parent = self.mapping[str(x_parent)]
            self.mapping[str(y_parent)] = x_val_parent
            self.cluster_count -= 1
            return 1


class UnionFindDictLazyCompNum():
    """ Implement a basic Union Find datastructure with lazy unions and path
    compression.
    Names elements in consecutive numbers.
    Also provides a reverse mapping that allows finding all elements that store
    a certain value.
    """

    def __init__(self, components):
        self.cluster_count = 0
        self.mapping = {}
        self.reverse_mapping = {}
        for c in components:
            self.mapping[self.cluster_count] = [self.cluster_count, c]
            if str(c) not in self.reverse_mapping:
                self.reverse_mapping[str(c)] = [self.cluster_count]
            else:
                self.reverse_mapping[str(c)].append(self.cluster_count)
            self.cluster_count += 1

    def find_ids(self, x):
        """ Find & return the ids that match a certain value."""
        try:
            ids = self.reverse_mapping[x]
        except KeyError:
            ids = []
        return ids

    def find_parents(self, x):
        """ Find & return the ultimate parent that x belongs to.
        Performs path compression."""
        curr_x = x
        curr_parent = self.mapping[curr_x][0]
        compression_list = []

        # TODO: Should this be curr_parent != curr_grandparent?
        while curr_x != curr_parent:
            compression_list.append(curr_x)
            curr_x = curr_parent
            curr_parent = self.mapping[curr_x][0]

        for node_id in compression_list:
            self.mapping[node_id][0] = curr_parent

        return curr_parent

    def union(self, x, y):
        """ Merge the two groups that contain x and y."""
        x_parent = self.find_parents(x)
        y_parent = self.find_parents(y)
        if x_parent == y_parent:
            return 0
        else:
            self.mapping[y_parent][0] = x_parent
            self.cluster_count -= 1
            return 1
