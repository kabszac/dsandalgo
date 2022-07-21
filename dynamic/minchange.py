def min_change(amount, coins):
  if _min_change(amount, coins, {}) == float("inf"):
    return -1
  return _min_change(amount, coins, {})

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  if amount == 0:
    return 0
  min = float("inf")
  size = 1
  for num in coins:
    if num <= amount:
      trial =  1 + _min_change(amount-num, coins, memo)
      if trial < min:
        min = trial
  memo[amount] = min     
  return min
    
      
