def heightChecker(heights, expected):
  count = 0

  for i in range(len(heights)):
    if heights[i] != expected[i]:
      count += 1

  return count

heights = [1, 1, 4, 2, 1, 3]
expected = [1, 2, 3, 4, 5, 6]
num_incorrect = heightChecker(heights, expected)
print(num_incorrect)
