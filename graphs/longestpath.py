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
      
#alvin solution using dfs recursion
def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
      
  for node in graph:
    traverse_distance(graph, node, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]

#add your terminal nodes first
#loop through each node in the graph and call your traverse function
#check if it is already in our dict  if it is return the distance of the node
# traverse through the neighbors and check for the lonest path
# add it to our distance dict 
# return the value of the distance of the node



  #O(e) runtime
  #(n) space



