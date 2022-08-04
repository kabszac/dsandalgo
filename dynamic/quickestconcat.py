from distutils.command.sdist import sdist


def quickest_concat(s, words):
  if  _quickest_concat(s,words, {}) == float("inf"):
    return -1
  return _quickest_concat(s, words, {})

def _quickest_concat(s, words, memo):
  if  s in memo:
    return memo[s]
  if len(s) == 0:
    return 0
  
  min_size = float("inf")
  
  for word in words:
    if s.startswith(word):     
      size = 1 + _quickest_concat(s[len(word):], words, memo)
      min_size = min(size, min_size)
      memo[s] = min_size
  return  min_size
  
  

