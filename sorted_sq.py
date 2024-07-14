def sorted_squares(nums):
  squared_nums = []

  for num in nums:
    squared_nums.append(num ** 2)
  squared_nums.sort()

  return squared_nums

nums = [-4, -1, 0, 3, 10]
squared_nums = sorted_squares(nums)
print(squared_nums)
