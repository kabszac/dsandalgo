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

def get_node_value2(head, index):
    if head == None: return None
    if index == 0: return head.val
    return get_node_value2(head.next, index-1)
