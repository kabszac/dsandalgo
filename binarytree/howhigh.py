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