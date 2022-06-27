def connected_components_count(graph):
  count = 0
  st = set()
  for node in graph:
    if traverse(graph, node, st) == True:
      count += 1
  return count
    
    
def traverse(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    traverse(graph, neighbor, visited)
  return True
  
#O(n) space
#O(e) run