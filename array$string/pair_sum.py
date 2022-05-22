def pair_sum(numbers, target_sum):
  for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return i,j

# runtime O(n2)
# sapce O(1)

# better method
def pair_sum(numbers, target_sum):
  dict1 = {}
  for i in range(len(numbers)):
    complement = target_sum - numbers[i]
    if complement in dict1:
      return (dict1[complement], i)
    
    dict1[numbers[i]] = i
    
# O(n) runtime
#O(n) space where n is length of list