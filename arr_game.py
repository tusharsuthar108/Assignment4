def buildArray(nums):
  arr = []
  n = len(nums)

  for i in range(n // 2):
    min_index = i
    max_index = n - 1 - i

    for j in range(i + 1, n - i):
      if nums[j] < nums[min_index]:
        min_index = j
      if nums[j] > nums[max_index]:
        max_index = j

    arr.append(nums[min_index])
    arr.append(nums[max_index])

  return arr

nums = [1, 2, 3, 4, 5, 6]
print(buildArray(nums))
