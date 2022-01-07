def removeNthFromEnd(head, n):
    fake = ListNode(0, head)
    left = fake
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right != None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return fake.next
