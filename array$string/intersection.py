def intersection(a, b):
  sett = set()
  lst= []
  sett.update(a)
  for i in b:
    if i in sett:
      lst.append(i)
  return lst
  
    
    
    # n = length of array a, m = length of array b
    # Time: O(n+m)
    # Space: O(n)
