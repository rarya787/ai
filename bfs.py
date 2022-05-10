'''
Aim:
	Given an unweighted graph, a source, and a destination, we need to find the shortest path from source to destination in the graph in the most optimal way using BFS.

Procedure:
1.	Initialize graph with vertices and edges.
2.	Take a visited array, all initialized to false, to keep track of visited vertices.
3.	Start searching from the source to find destination.
4.	Take a previous array to keep track of previous vertices.
5.	For a current vertex, add all its neighbors to the queue to traverse the vertices breadth wise.
6.	Break the iteration when destination is found.
7.	Track the shortest path from source to destination from previous array.
'''
import time

class Graph:
    def _init_(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.visited = [False]*V
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def BFS(self, s, d):
        prev = dict()
        queue = [s]
        self.visited[s] = True
        
        while queue:
            t = queue.pop(0)
            print(t, end = " ")
            if t == d:
                break
            
            for ver in self.adj[t]:
                if not self.visited[ver]:
                    prev[ver] = t
                    queue.append(ver)
                    self.visited[ver] = True
                    
        return prev
    
    def shortestPath(self, s, d):
        path = []
        prev = self.BFS(s, d)
        # print("\n", prev)
        at = d
        
        while at != s:
            path.append(at)
            at = prev[at]
        
        path.append(s)
        print("Shortest path: ", path[::-1])
        
    
v = int(input("Enter the no. of Vertices: "))
e = int(input("Enter the no. of Edges: "))

g = Graph(v)

for i in range(e):
    inp = input("Enter the vertices edge {}: ".format(i+1))
    edge = list(map(int, inp.split()))
    g.addEdge(edge[0], edge[1])

s = int(input("Enter the source: "))
d = int(input("Enter the destination: "))

begin = time.time()
g.shortestPath(s, d)

time.sleep(1)
end = time.time()
print("Time taken by BFS: ", end - begin)

'''
    1----0    7----6
    |    |   /|   /|
    |    |  / |  / |
    |    | /  | /  |
    |    |/   |/   |
    2    3----4----5

'''
