# def sum_possible(amount, numbers):
#   if len(numbers) == 1 and amount == numbers[0]:
#     return True
  
#   if amount == 0 and len(numbers) == 0:
#     return True
  
#   for i in range(len(numbers)):
#     trial = amount - numbers[i]
#     for j in range(len(numbers)):
#       if trial % numbers[j] == 0 and trial > 0:
#         return True
#   return False

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return True
  
  
  for i in numbers:
    if i <= amount:
      if _sum_possible(amount-i, numbers, memo) == True:
        memo[amount] = True
        return True
      
  memo[amount] = False
  return False


#O(n) space and time






    
  
  
  
  
  
  
  
  
  
  
  
    
