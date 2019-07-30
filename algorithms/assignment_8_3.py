#!/usr/bin/env python3

import utils
from clustering import union_find

data = [1, 2, 3, 4, 5, 6]

# x = union_find.UnionFindDictLazy(data)
x = union_find.UnionFindDictLazyComp(data)

print(x.mapping)

x.union(4, 5)
x.union(1, 2)

print(x.mapping)

x.union(1, 5)

print(x.mapping)

x.union(5, 6)

print(x.mapping)

# x.union(3, 1)

# print(x.mapping)
