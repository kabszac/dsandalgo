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
