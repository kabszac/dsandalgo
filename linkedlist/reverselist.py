def reverse_list(head):
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current 
        current = next
    return prev

# we do not want to lose access to next
#space(O(1))
#runtime O(n)