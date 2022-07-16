def has_cycle(graph):
  visiting= set()
  visited = set()
  
  for node in graph:
    if traverse(graph, node, visiting, visited) == True:
      return True
  return False
    
def traverse(graph, node, visiting, visited):
  
  if node in visited:
    return False
  
  if node in visiting:
    return True
  
  visiting.add(node)
  
  for neighbor in graph[node]:
    if traverse(graph,neighbor,visiting, visited) == True:
      return True
  
  visiting.remove(node)
  visited.add(node)
  return False


#O(e) runtime
#O(n) space 
#white grey black algorithm

    
    
    
    
    
    
    



