def counting_change(amount, coins):
  return _counting_change(amount, coins , 0, {})
  
def _counting_change(amount, coins , i, memo):
  # if i in memo:
  #   return memo[i]
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
      
  coin = coins[i]
  count = 0
  for amt in range(0, (amount//coin) + 1):
    rem = amount - (coin*amt)
    count += _counting_change(rem, coins, i+1, memo)
    # memo[i] = count
  
  return count
