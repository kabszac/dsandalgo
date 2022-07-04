def longest_path(graph):
  longest = float('-inf')
  for node in graph:
    path_distance = traverse(graph, node)
    if path_distance > longest:
      longest =path_distance
  return longest
  
def traverse(graph, start):
  stack = [(start, 0)]
  st = set()
  
  while stack:
    
    node, distance= stack.pop()
    st .add(distance)
    
    
    for neighbor in graph[node]:
      stack.append((neighbor, distance+1))
  return max(st)
      




