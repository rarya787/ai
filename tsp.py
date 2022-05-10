'''
Given a set of cities and distances between every pair of cities, the problem is to find the
shortest possible route that visits every city exactly once and returns to the starting point.
For example, consider the graph shown in the figure on the right side. A TSP tour in the
graph is 1-2-4-3-1. The cost of the tour is 10 + 25+ 30+ 15 which is 80.

Aim:
To find the shortest possible route between pair of cities.

Procedure:
Step 1: Consider city 1 as the starting and ending point.
Step 2: Generate all (n-1)! Permutations of cities.
Step 3: Calculate cost of every permutation and keep track of minimum cost
permutation.
Step 4: Return the permutation with minimum cost.
'''
from sys import maxsize
from itertools import permutations

V = 4
def travellingSalesmanProblem(graph, s):
  vertex = []
  for i in range(V):
    if i != s:
      vertex.append(i)
  min_path = maxsize
  next_permutation=permutations(vertex)
  for i in next_permutation:
    current_pathweight = 0
    k = s
    for j in i:
      current_pathweight += graph[k][j]
      k = j
    current_pathweight += graph[k][s]
    min_path = min(min_path, current_pathweight)
  return min_path

if __name__ == "__main__":
  graph = []
  # matrix representation of graph
  #graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
  for i in range(V):
    a=[]
    for j in range(V):
      a.append(int(input()))
    graph.append(a)
  s = int(input("Starting point -> "))
  print(&quot;The matrix representation of graph is &quot;)

  for i in range(V):
  for j in range(V):
    print(graph[i][j], end = " ")
  print()
  print("The minimum weight is ", travellingSalesmanProblem(graph, s))
