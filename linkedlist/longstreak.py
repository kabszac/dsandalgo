def longest_streak(head):
  if head is None:
    return 0
  current = head
  current_val = head.val
  count = 0
  lst = []
  
  while current:
    if current.val == current_val:
      count += 1
      current = current.next
    else:
      lst.append(count)
      current_val = current.val
      count = 1
      current = current.next
  lst.append(count)
  return max(lst)

  #runtime O(n)
  #space O(n) worst case


#Better space complexity using kadanes algo

def longest_streak(head):
    max_streak = 0
    current_streak = 0
    prev_node = None
    current_node = head

    while current_node:
        #check and update our current streak
        if current_node.val == prev_node:
            current_streak +=1
        else:
            current_streak = 1
        # update our prev node
        prev_node = current_node

        #check and update our max streak
        if current_streak > max_streak:
            max_streak = current_streak

        current_node = current_node.next

    return max_streak

#O(n) runtime
#O(1) space
