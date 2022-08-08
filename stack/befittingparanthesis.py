# def befitting_brackets(string):
#   count = 0
#   start = set(['(','[','{'])
#   stop = set([')',']','}'])
#   dict = {']':'[', '}':'{', ')':'('}
#   stack = []
  
#   for char in string:
#     if char in start:
#       stack.append(char)
#       count += 1
#     elif char in stop and len(stack) != 0:
#       s = stack.pop() 
#       if dict[char] == s: 
#         count -= 1
#     else:
#       return False
      
#   if count == 0:
#     return True
#   else:
#     return False

def befitting_brackets(string):
  stack = []
  dict = {'(':')', '[':']', '{':'}'}
  for char in string:
    if char in dict:
      stack.append(dict[char])
    else:
      if stack and char == stack[-1]:
        stack.pop()
      else:
        return False
        
  return len(stack) == 0
  
  #runtime

  
  
  
  
  
  
  
  
  
  
  
  
