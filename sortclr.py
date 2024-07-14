def sortColors(nums):
  red_index = 0
  white_index = 0
  blue_index = len(nums) - 1

  while white_index <= blue_index:
    if nums[white_index] == 0:
      nums[red_index], nums[white_index] = nums[white_index], nums[red_index]
      red_index += 1
      white_index += 1
    elif nums[white_index] == 2:
      nums[white_index], nums[blue_index] = nums[blue_index], nums[white_index]
      blue_index -= 1
    else:
      white_index += 1
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
