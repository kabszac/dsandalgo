def most_frequent_char(s):
  count = {}
  for l in s:
    if l not in count:
      count[l] = 1
    count[l] += 1
  maxValue = max(count.values())
  for k, v in count.items():
    if v == maxValue:
      return k
    


    # n = length of string
    # Time: O(n)
    # Space: O(n)
