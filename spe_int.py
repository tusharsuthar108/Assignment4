def find_special_integer(nums):
  nums.sort()
  for i in range(len(nums)):
    if len(nums) - i == nums[i]:
      return nums[i]
  return -1

nums = [1, 2, 3, 4, 5]
special_integer = find_special_integer(nums)
print(special_integer)
