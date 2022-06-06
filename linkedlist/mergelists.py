
# we create our dummy node
# tranverse while checking
# check if either of our lists is empty and replace with the other list
# return the head of our linked list which is the dummy .next

def merge_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy
  current1 = head_1
  current2 = head_2
  while current1 is not None and current2 is not None:
    if current1.val < current2.val:
      tail.next = current1
      current1 = current1.next
    else:
      tail.next = current2
      current2 = current2.next
    tail = tail.next
    
  if current1 is None:
    tail.next = current2
  if current2 is None:
    tail.next = current1
    
  return dummy.next

  #n = length of list 1 
  #m = length of lst 2
  #O(n) = min(n,m)
  #space O(1)