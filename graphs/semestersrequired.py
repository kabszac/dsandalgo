def semesters_required(num_courses, prereqs):
  if len(prereqs) == 0:
    return 1
  graph = createAdjacencyList(prereqs)
  minimum_sem = float('-inf')
  for node in graph:
    value = traverse(graph, node)
    if value > minimum_sem:
      minimum_sem = value
  return minimum_sem
  
def traverse(graph, start):
  stack = [(start, 1)]
  st = set()
  while stack:
    node, distance = stack.pop()
    st.add(distance)
    
    for neighbor in graph[node]:
      stack.append((neighbor, distance+1))
  return max(st)

def createAdjacencyList(prereqs):
  graph = {}
  
  for node in prereqs:
    a,b = node
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    
  return graph

#O(n) space
#O(e) runtime



