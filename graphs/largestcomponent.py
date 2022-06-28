def largest_component(graph):
  visited = set()
  largest = 0
  for node in graph:
    size = traverse(graph, node, visited)
    if  size > largest:
      largest = size
       
  return largest
  
def traverse(graph, current, visited):
  if current in visited:
    return 0
  
  visited.add(current)
  size  = 1 
  for neighbor in graph[current]:
    size += traverse(graph,neighbor,visited)
  return size

  #O(n) space
  #O(e) runtime