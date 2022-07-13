def has_path(graph, src, dst):
  stack = [src]
  while stack:
    curr_val= stack.pop() 
    if curr_val == dst:
      return True
    for neighbor in graph[curr_val]:
      stack.append(neighbor)
  return False

#O(n) space and time


def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    # if true return true for the parent call stack
    if has_path(graph, neighbor, dst) == True:
      return True
  
  return False

#O(e) runtime visit all edges
#O(n) space
