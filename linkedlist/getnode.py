def get_node_value(head, index):
    current = head
    pos = 0
    while current != None:
        if pos == index:
            return current.val
        pos += 1
        current =current.next
    return None


#runtime O(n)
#space O(1)