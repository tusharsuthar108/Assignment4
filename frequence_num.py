import collections
def frequency_sort(nums):
  count = collections.Counter(nums)
  sorted_nums = sorted(nums, key=lambda x: (count[x], -x))
  return sorted_nums

nums = [1, 1, 2, 2, 2, 3]
sorted_nums = frequency_sort(nums)
print(sorted_nums)
