from collections import deque

def paired_parentheses(string):
  stack = deque([])
  #st = set(['('')'])
  count = 0
  
  for s in string:
    stack.append(s)
    
  
  while stack:
    s = stack.popleft()
    
    if s == '(':
      count += 1
    elif s == ')':
      count -= 1
    
    if count < 0:
      return False
    
  if count == 0:
    return True
  else:
    return False
  
  
  
  
  
  
      
    
