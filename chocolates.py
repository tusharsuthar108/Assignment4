def buy_chocolates(prices, money):
  prices.sort()
  left = 0
  right = len(prices) - 1

  while left < right:
    if prices[left] + prices[right] <= money:
      left += 1
    else:
      right -= 1

  if left == 0:
    return money - prices[0] - prices[1]
  else:
    return money - prices[left - 1] - prices[left]

prices = [1, 3, 4, 6, 9]
money = 10
leftover_money = buy_chocolates(prices, money)
print(leftover_money)
