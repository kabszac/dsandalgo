from typing import Text


def find(head, target):
    current =head
    while current != None:
        if current.val == target:
            return True
        current = current.next
    return False


#runtime O(n)
#space O(1)

def find2(head, target):
    if head == None:
        return False
    if head.val == target:
        return True
    find2(head.next, target)

#runtime O(n)
#space O(n)
