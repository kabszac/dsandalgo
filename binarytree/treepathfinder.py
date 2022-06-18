#method 1 dfs

def path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [ root.val, *left_path ]
  
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [ root.val, *right_path ]
  
  return None

#O(n2) run time because we are copying the list
#O(n) space


#method 2

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [root.val]
  
  left_trav = _path_finder(root.left, target)
  if left_trav is not None:
    left_trav.append(root.val)
    return left_trav
  
  right_trav = _path_finder(root.right, target)
  if right_trav is not None:
    right_trav.append(root.val)
    return right_trav
  
  
  return None

  #O(n) runtime
  #O(n) space

  