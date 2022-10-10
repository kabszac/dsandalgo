def how_high(node):
  if node is None:
    return -1
  if node is not None:
    match = 1
  
  left_trav = how_high(node.left)
  right_trav = how_high(node.right)
  
  return match + max(left_trav,right_trav)

#O(n) runtime
#O(n) space

# using  bfs
from collections import deque

def how_high2(node):
  if node is None:
    return -1
  
  stack = deque([(0, node)])
  while stack:
    distance, currentNode = stack.popleft()
    
    if currentNode.left:
      stack.append((distance+1, currentNode.left))
    if currentNode.right:
      stack.append((distance+1, currentNode.right))
  return distance