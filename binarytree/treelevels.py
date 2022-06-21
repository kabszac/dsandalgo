def tree_levels(root):
  if root is None:
    return []
  levels_list = []
  stack = [(root, 0)]
  while stack:
    curr_node, level = stack.pop()
    
    if len(levels_list) == level:
      levels_list.append([curr_node.val])
    else:
      levels_list[level].append(curr_node.val)
    if curr_node.right:
      stack.append((curr_node.right, level + 1))
    if curr_node.left:
      stack.append((curr_node.left, level+1))
  return levels_list