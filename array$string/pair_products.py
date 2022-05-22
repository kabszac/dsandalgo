def pair_product(numbers, target_product):
  dict1 = {}
  for index, num in enumerate(numbers):
    result = target_product // num
    
    if result in dict1:
      return dict1[result], index
    
    dict1[num] = index

# O(n) runtime
#O(n) space where n is length of list