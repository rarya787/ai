'''Aim: To find a path from source to destination using Best first search algorithm
Procedure:
1. Create 2 empty lists: OPEN and CLOSED
2. Start from the initial node (say N) and put it in the ‘ordered’ OPEN list
3. Repeat the next steps until GOAL node is reached
1. If OPEN list is empty, then EXIT the loop returning ‘False’
2. Select the first/top node (say N) in the OPEN list and move it to the CLOSED list. Also
capture the information of the parent node
3. If N is a GOAL node, then move the node to the Closed list and exit the loop
returning ‘True’. The solution can be found by backtracking the path
4. If N is not the GOAL node, expand node N to generate the ‘immediate’ next nodes
linked to node N and add all those to the OPEN list
5. Reorder the nodes in the OPEN list in ascending order according to an evaluation
function f(n)
'''

from collections import defaultdict
class Graph:
  def __init__(self, V):
    self.V = V
    self.adj = defaultdict(list)

  def addEdge(self, u, v, h2):
    self.adj[u].append((v, h2))

  def bestFirst(self, s, d, h1):
    success = False
    open = [(s, h1)]

    closed = []

    while open and not success:
      t = open.pop(0)
      print(t[0], end = &quot; &quot;)
      if t[0] == d:
        success = True
        closed.append(t)
      else:
        closed.append(t)
        for neighbor in self.adj[t[0]]:
          if neighbor not in open and neighbor not in closed:
            open.append(neighbor)
        open.sort(key = lambda t: t[1])

v = int(input(&quot;Enter the no. vertices: &quot;))
g = Graph(v)

heuristics = dict()
for i in range(v):
  ver_h = input(&quot;Enter vertex {} and its heuristic: &quot;. format(i+1)).strip().split()
  heuristics[ver_h[0]] = int(ver_h[1])
# print(ver_h[0], int(ver_h[1]))

e = int(input(&quot;Enter the no. edges: &quot;))
for i in range(e):
  edge = input(&quot;Enter the vertices of edge {}: &quot;. format(i+1)).strip().split()
  # print(heuristics[edge[0]], heuristics[edge[1]])
  g.addEdge(edge[0], edge[1], heuristics[edge[1]])

s = input(&quot;Enter the source: &quot;)
d = input(&quot;Enter the destination: &quot;)
g.bestFirst(s, d, heuristics[s])
