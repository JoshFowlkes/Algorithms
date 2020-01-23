#!/usr/bin/python

import argparse

''' 
If you bought the perfect low and sold the perfect high 
'''
def max_profit(prices):
  return max(prices) - min(prices)

''' 
If you bought the lowest possible point early on, and sold at highest point 
thereafter in the list.
'''
def find_max_profit(prices):
  min_price = prices[0]
  max_price = prices[1] - min_price

  for i in range(1, len(prices)):
    price = prices[i]
    max_price = max(price-min_price, max_price)
    min_price = min(price, min_price)
  return max_price

  amzn_prices = [1870, 1888, 1892, 1900, 1903, 1909, 1917, 1932]
  find_max_profit(amzn_prices)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))