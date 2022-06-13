from collections import deque

def breadth_first_values(root):
  if root is None:
    return []
  values = []
  queue = deque([root])
  
  while queue:
    current_node = queue.popleft()
    values.append(current_node.val)
    
    if current_node.left is not None:
      queue.append(current_node.left)
      
    if current_node.right:
      queue.append(current_node.right)
      
  return values

#O(n) runtime
#O(n) space

