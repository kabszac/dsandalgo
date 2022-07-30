def array_stepper(numbers):
  return _array_stepper(numbers,0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
  
  if i == len(numbers)-1:
    return True
  
  max_steps = numbers[i]
  
  for steps in range(1, max_steps + 1):
    if _array_stepper(numbers, i + steps, memo) == True:
      memo[i] = True
      return True
    
  memo[i] = False
  return False