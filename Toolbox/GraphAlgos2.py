#https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# Kurskal MST
# 1. Sort all the edges in non-decreasing order of their weight. 
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
# 3. Repeat step#2 until there are (V-1) edges in the spanning tree.

# Prim MST
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# We have discussed Kruskal’s algorithm for Minimum Spanning Tree. 
# Like Kruskal’s algorithm, Prim’s algorithm is also a Greedy algorithm. 
# It starts with an empty spanning tree. The idea is to maintain two sets of vertices. 
# The first set contains the vertices already included in the MST, 
# the other set contains the vertices not yet included. 
# At every step, it considers all the edges that connect the two sets
#  and picks the minimum weight edge from these edges. 
#  After picking the edge, it moves the other endpoint of the edge to the set containing MST. 
# A group of edges that connects two sets of vertices in a graph is called cut in graph theory.
#  So, at every step of Prim’s algorithm, we find a cut (of two sets, one contains the vertices 
#  already included in MST and the other contains the rest of the vertices), 
#  pick the minimum weight edge from the cut, and include this vertex to MST Set 
#  (the set that contains already included vertices).