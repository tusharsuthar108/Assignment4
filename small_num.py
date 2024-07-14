def smaller_numbers_than_current(nums):
  count = [0] * len(nums)
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i != j and nums[j] < nums[i]:
        count[i] += 1
  return count

nums = [8, 1, 2, 2, 3]
smaller_numbers = smaller_numbers_than_current(nums)
print(smaller_numbers)
