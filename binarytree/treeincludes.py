def tree_includes(root, target):
  if root is None:
    return False
  
  stack = [root]

  while stack:
    current_node = stack.pop()
    if current_node.val == target:
      return True
    if current_node.right:
      stack.append(current_node.right)
    if current_node.left:
      stack.append(current_node.left)
  return False


  #O(n) runtime
  #O(1) space
  