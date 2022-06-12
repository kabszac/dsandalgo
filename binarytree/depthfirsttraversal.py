# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


## iterative traversal

def depth_first_values(root):
  if root is None:
    return []
  value = []
  stack = [root]
  while stack:
    current = stack.pop()
    value.append(current.val)
    
    if current.right is not None:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return value


## recursive

def depth_first_values(root):
    #base casse
    if root is None:
        return []
    ## get the root .left values returns a list
    left_values = depth_first_values(root.left)
    ## get the root .right values
    right_values = depth_first_values(root.right)

    ## concatnate the list together
    return [root.val, *left_values, *right_values]
    
#O(n) space each node is being added once
#O(n) runtime each node is being traversed once