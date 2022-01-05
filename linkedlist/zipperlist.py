def zipper_lists(head_1, head_2):
    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0
    while current1 != None and current2 != None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        count += 1
        tail = tail.next

    if current1 == None:
        tail.next = current2

    if current2 == None:
        tail.next = current1
    
    return head_1

#runtime (min(O(n)(m)))
#space(O(1))
#lessons we have 3 variable tail which starts with the head of the head1
#current 1 and 2 
#count 
# if count is even we add current 2 to our tail, do not forget to move the pointer in  our current 2 and viceversa
# pointer of tail moves and count also increases
# if either of the linked list is none just add the rest of the remaining list takes O(1) time.

