'''
Aim: To find a path from source to destination using Best first search algorithm
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

heuristic = dict()
Graph = defaultdict(list)

def aStar(start, des):
  openSet = [start]
  closedSet = []
  g = {}
  parent = {}
  g[start] = 0
  parent[start] = None

  while openSet:
    n = None

  for v in openSet:
    if n == None or g[v] + heuristic[v] &lt; g[n] + heuristic[n]:
      n = v
      print(n)
    if n == d or not Graph[n]:
      pass
    else:
      for m, w in Graph[n]:
        if m not in openSet and m not in closedSet:
          openSet.append(m)
          parent[m] = n
          g[m] = g[n] + w

        else:
          if g[m] &gt; g[n] + w:
            g[m] = g[n] + w
            parent[m] = n

          if m in closedSet:
            closedSet.remove(m)
            openSet.append(m)
            
  if n == None:
    print(&quot;Path doesn&#39;t exist!!!&quot;)
    return
  if n == des:
    path = []
    while parent[n] != None:
      path.append(n)
      n = parent[n]

    path.append(s)
    print(&quot;Path found: {}&quot;.format(path[::-1]))
# print(parent)
    return
  openSet.remove(n)
  closedSet.append(n)

v = int(input(&quot;Enter the no. vertices: &quot;))
for i in range(v):
  ver_h = input(&quot;Enter vertex {} and its heuristic: &quot;. format(i+1)).strip().split()
  heuristic[ver_h[0]] = int(ver_h[1])

e = int(input(&quot;Enter the no. edges: &quot;))
for i in range(e):
  edge = input(&quot;Enter the vertices of edge {} along with the weight: &quot;. format(i+1)).strip().split()
  Graph[edge[0]].append((edge[1], int(edge[2])))

# print(Graph)

s = input(&quot;Enter the source: &quot;)
d = input(&quot;Enter the destination: &quot;)
aStar(s, d)
