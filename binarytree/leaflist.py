from tkinter.messagebox import NO


def leaf_list(root):
  if root is None:
    return []
  
  if root.left is None and root.right is None:
    return [root.val]
  
  left_subtree = leaf_list(root.left)
  right_subtree = leaf_list(root.right)
  
  return [*left_subtree, *right_subtree]

#O(n) runtime 
#O(n) space

def leaf_list(root):
    if root is None:
        return []

    stack = [root]
    lst = []
    while stack:
        curr_node = stack.pop()

        if curr_node.right is None and curr_node.left is None:
            lst.append(curr_node.val)

        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.left)
        
    return lst

#O(n) space
#O(n) runtime

