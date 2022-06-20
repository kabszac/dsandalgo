# iterative method dfs


def tree_value_count(root, target):
  
  if root is None:
    return 0
  
  count = 0
  stack = [root]
  while stack:
    curr_node = stack.pop()
    if curr_node.val == target:
      count += 1
    if curr_node.right:
      stack.append(curr_node.right)
    if curr_node.left:
      stack.append(curr_node.left)
  return count

#O(n) run
#O(n) space

#recursive
def tree_value_count(root, target):
  count = 0
  if root is None:
    return 0
  if root.val == target:
    match = 1
  else:
    match = 0
      
  left_trav = tree_value_count(root.left, target)
  right_trav = tree_value_count(root.right, target)
  
  return match + left_trav + right_trav

