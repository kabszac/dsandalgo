def max_path_sum(root):
  if root is None:
    return float("-inf")
  if root.left is None and root.right is None:
    return root.val
  
  left_trav = max_path_sum(root.left)
  right_trav = max_path_sum(root.right)
  
  return root.val + max(left_trav, right_trav)

  #O(n) space
  #O(n) time