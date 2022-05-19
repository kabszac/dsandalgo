def uncompress(s):
  strng = ''
  numbers = '0123456789'
  i = 0
  j= 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      strng += ( s[j] * num)
      j += 1
      i = j
  return strng

  #O(nm) largest group * number of grps(1000*2)
  #1000p1000q

  