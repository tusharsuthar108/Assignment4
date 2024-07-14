def rearrange_array(nums):
  odd_nums = []
  even_nums = []

  for i in range(len(nums)):
    if i % 2 == 0:
      even_nums.append(nums[i])
    else:
      odd_nums.append(nums[i])

  odd_nums.sort(reverse=True)
  even_nums.sort()

  result = []
  for i in range(len(nums)):
    if i % 2 == 0:
      result.append(even_nums[i // 2])
    else:
      result.append(odd_nums[i // 2])

  return result

nums = [4, 1, 2, 3]
rearranged_nums = rearrange_array(nums)
print(rearranged_nums)
