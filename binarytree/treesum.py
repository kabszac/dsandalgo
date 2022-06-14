def tree_sum(root):
  if root is None:
    return 0
  
  count = 0
  stack = [root]
  
  while stack:
    current_node =stack.pop()
    count += current_node.val
    
    if current_node.right:
      stack.append(current_node.right)
    if current_node.left:
      stack.append(current_node.left)
  return count


#O(n) space each node is being added once
#O(n) runtime each node is being traversed once