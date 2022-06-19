from collections import deque

def bottom_right_value(root):
  result = []
  queue = deque([root])
  while queue:
    node_val = queue.popleft()
    result.append(node_val.val)
    
    if node_val.left:
      queue.append(node_val.left)
    if node_val.right:
      queue.append(node_val.right)
      
  return result[-1]

  #O(n) runtime and space
  