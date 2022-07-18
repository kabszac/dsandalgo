def prereqs_possible(num_courses, prereqs):
  graph = createAdjacencyList(prereqs)
  visiting = set()
  visited = set()
  for node in graph:
    if traverse(graph, node, visiting, visited) == True:
      return False
  return True
    
def traverse(graph, node, visiting, visited):
  if node in visited:
    return False
  
  if node in visiting:
    return True
  visiting.add(node)
  
  for neighbor in graph[node]:
    if traverse(graph, neighbor, visiting, visited) == True:
      return True
    
  visiting.remove(node)
  visited.add(node)
  return False
    

def createAdjacencyList(prereqs):
  adjacencyList = {}
  
  for node in prereqs:
    a, b = node
    
    if a not in adjacencyList:
      adjacencyList[a] = []
      
    if b not in adjacencyList:
      adjacencyList[b] = []
      
    adjacencyList[a].append(b)
    
  return adjacencyList



# p = # prereqs
# n = # courses
# Time: O(n + p)
# Space: O(n)
