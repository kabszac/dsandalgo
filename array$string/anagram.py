def anagrams(s1, s2):
  dict1 = {}
  dict2 = {}
  for s in s1:
    if s not in dict1:
      dict1[s] = 1
    else:
      dict1[s] += 1
  for s in s2:
    if s not in dict2:
      dict2[s] = 1
    else:
      dict2[s] += 1
  if dict1 == dict2:
    return True
  return False
  


    # n = length of string 1
    # m = length of string 2
    # Time: O(n + m)
    # Space: O(n + m)
