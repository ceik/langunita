#!/usr/bin/env python3

import utils
from graphs import scc_computation

# data = utils.load_tab_delimited_file('data/SCC.txt')
data = utils.load_tab_delimited_file('data/SCC_6.txt')

# g = scc_computation.DirectedGraph(875714, data)
g = scc_computation.DirectedGraph(11, data)

# g.compute_sccs()

# for e, v in g.nodes.items():
#     print(e, v.fin_time)

# for e, v in g.nodes_by_fin_time.items():
#     print(e, v.edges)

print(g.n_largest_sccs(20))
