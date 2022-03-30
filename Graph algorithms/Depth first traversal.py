""" Graph is a data structure can be traversed by
 two methods breadth first traversal
 and depth first traversal"""
# Depth First traversal requires stack to implement

from collections import defaultdict
class Graph:
    # constructor
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')


        for neighbour in self.graph[v]:
            if neighbour in self.graph[v]:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited)

    def  DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

# Driver Code:
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is dfs from starting from vertex 2")
g.DFS(2)
