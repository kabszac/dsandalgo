def sumlist(head):
    current =head
    total = 0
    while current != None:
        total += current.value
        current = current.next
    return total