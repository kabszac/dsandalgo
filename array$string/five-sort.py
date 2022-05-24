def five_sort(nums):
  j = 0
  k = (len(nums) -1 )
  while j < k:
    if nums[k] == 5:
      k -= 1
    elif nums[j] == 5:
      nums[j], nums[k] = nums[k], nums[j]
      j += 1
      k -= 1
    else:
      j += 1
  return nums

# n = array size
# Time: O(n)
# Space: O(1)