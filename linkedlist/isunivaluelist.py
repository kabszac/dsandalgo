def is_univalue_list(head):
  current = head
  st = set()
  while current:
    st.add(current.val)
    current =current.next
  if len(st) == 1:
    return True
  return False

  #O(n) runtime
  #O(n) space worst case

  #better

def is_univalue_list(head):
    current = head 
    while current:
        if current.val != head.val:
            return False
        current = current.next
    return True

#O(n) ru
#O(1) space
