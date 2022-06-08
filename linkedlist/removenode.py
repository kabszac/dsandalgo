#my approach

def remove_node(head, target_val):
  dummy = Node(None)
  dummy.next = head
  current = head
  prev = dummy
  while current:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current= current.next
  return dummy.next

#O(n) runtime
#O(1) space

def remove_node(head, target_val):
    
    #if our head is target val
    if head.val == target_val:
        return head.next

    current = head
    prev = None

    while current:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current= current.next

    return head

#O(n) runtime
#O(1) space

