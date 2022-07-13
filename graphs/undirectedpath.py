def undirected_path(edges, node_A, node_B):
  graph = createAdjencyList(edges)
  return helperfunc(graph, node_A, node_B, set())
  
def helperfunc(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if helperfunc(graph, neighbor, dst, visited) == True:
      return True
  return False

#DFS iterative
# def helperfunc(graph, src, dst):
#   stack = [src]
#   st = set([src])
  
#   while stack:
#     node = stack.pop()
    
#     if node == dst:
#       return True
    
#     for neighbor in graph[node]:
#       if neighbor not in st:
#         stack.append(neighbor)
#         st.add(neighbor)
#   return False


def createAdjencyList(edges):
  adjencyList = {}
  for edge in edges:
    a,b= edge
    if a not in adjencyList:
      adjencyList[a] = []
    if b not in adjencyList:
      adjencyList[b] = []
      
    adjencyList[a].append(b)
    adjencyList[b].append(a)
    
  return adjencyList

  #O(e) where e is the number of edges runtime
  #O(n) space complexity