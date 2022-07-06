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

# alvin
def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  distance = {}
  for course in range(num_courses):
    if len(graph[course]) == 0:
      distance[course] = 1
  
  for course in range(num_courses):
    traverse_distance(graph, course, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  max_distance = 0
  for neighbor in graph[node]:
    neighbor_distance = traverse_distance(graph, neighbor, distance)
    if neighbor_distance > max_distance:
      max_distance = neighbor_distance
    
  distance[node] = 1 + max_distance
  return distance[node]

def build_graph(num_courses, prereqs):
  graph = {}
  
  for course in range(num_courses):
    graph[course] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  
  return graph



    #p = # prereqs
    #c = # courses
    #Time: O(p)
    #Space: O(c)


