def sumlist(head):
    current =head
    total = 0
    while current != None:
        total += current.value
        current = current.next
    return total


# o(n) time complexity
#O(1) space complexity

