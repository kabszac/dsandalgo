from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = createadjacencyList(edges)
  return helper(graph, node_A, node_B)

def helper(graph, src, dst):
  visited = set([src])
  queue = deque([(src, 0)])
  
  
  while queue:
    node, distance = queue.popleft()
    
    if node == dst:
      return distance
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance+1))
        
  return -1
    
def createadjacencyList(edges):
  adjacencyList = {}
  for edge in edges:
    a,b = edge
    if a not in adjacencyList:
      adjacencyList[a] = []
    if b not in adjacencyList:
      adjacencyList[b] = []
      
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)
    
  return adjacencyList


#runtime linear
# space linear

      
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    