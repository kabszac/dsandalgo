class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  carry = 0
  dummy = Node(None)
  tail = dummy
  current1 = head_1
  current2 =head_2
  
  
  
  while current1 is not None or current2 is not None or carry==1:
    val1 = 0 if current1 is None else current1.val
    val2 = 0 if current2 is None else current2.val
    
    sum = val1 + val2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10
    insert= Node(digit)
    tail.next = insert
    tail = tail.next
    
    if current1 is not None:
      current1 = current1.next
    if current2 is not None:
      current2 = current2.next
  return dummy.next
    
    
    
#O(max(n,m)) space and time