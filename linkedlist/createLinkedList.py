class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  dummy = Node(None)
  tail = dummy
  for v in values:
    input = Node(v)
    tail.next = input
    tail = tail.next
  
  return dummy.next
#runtime O(n)  
#space O(n)