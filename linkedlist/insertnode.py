class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  if index == 0:
    inserted = Node(value)
    inserted.next = head
    return inserted
  current = head
  count = 0
  while current :
    if count == index-1:
      nxt = current.next
      inserted = Node(value)
      current.next = inserted
      inserted.next = nxt
    count += 1
    current= current.next
  return head