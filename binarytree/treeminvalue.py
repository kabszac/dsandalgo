def tree_min_value(root):
  current_min =0
  min_val = 1000
  stack = [root]
  while stack:
    current_node = stack.pop()
    current_min = current_node.val
    if current_min< min_val:
      min_val = current_min
    if current_node.right:
      stack.append(current_node.right)
    if current_node.left:
      stack.append(current_node.left)
  return min_val

  #O(n) runtime
  #O(n) space

# recursion
def tree_min_value2(root):
  if root is None:
    return float("inf")

  left_min_subtree_val = tree_min_value2(root.left)
  right_min_subtree_val = tree_min_value2(root.right)

  return min(root.val, left_min_subtree_val, right_min_subtree_val)