# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/#:~:text=To%20detect%20cycle%2C%20check%20for,a%20cycle%20in%20the%20tree.
  
from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
  
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Returns true if graph is cyclic else false
    # Find all the vertices which are not visited and are adjacent to the current node.
    # Recursively call the function for those vertices, If the recursive function returns true, return true.
    def is_cyclic(self):
        visited = [False] * (self.vertices + 1)
        rec_stack = [False] * (self.vertices + 1)
        for node in range(self.vertices):
            if visited[node] == False:
                if self.is_cyclic_helper(node, visited, rec_stack) == True:
                    return True
        return False

    def is_cyclic_helper(self, v, visited, rec_stack):
  
        # Mark current node as visited and adds to recursion stack
        visited[v] = True
        rec_stack[v] = True
  
        # Recur for all neighbours
        # If any neighbour is visited and in recursion stack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_helper(neighbour, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbour] == True:
                return True
  
        # The node needs to be popped from recursion stack before function ends
        rec_stack[v] = False
        return False
  
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
if g.is_cyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")