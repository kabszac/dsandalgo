def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo: 
    return memo[s]
  
  if len(s) == 0:
    return True
  
  for word in words:
    if s.startswith(word) :
      if _can_concat(s[len(word):],words, memo) == True:
        memo[s] =  True
        return True
  memo[s] = False
  return False

