def level_averages(root):
  if root is None:
    return []
  results = []
  levels = []
  stack = [(root, 0)]
  while stack:
    curr_node, level = stack.pop()
    if len(levels) == level:
      levels.append([curr_node.val])
    else:
      levels[level].append(curr_node.val)
    
    if curr_node.right:
      stack.append((curr_node.right, level+1))
    if curr_node.left:
      stack.append((curr_node.left, level+1))
      
  for l in levels:
    total = sum(l)
    average = total / len(l)
    results.append(average)
  return results