#!/usr/bin/python

import sys
# possibiliies 
'''
1: # 1
1

2: # 2
11
2

3: # 4
111
12
21
3

4: # 7
1111
112
121
211
22
13
31
4


5: # 13
11111
2111
1211
1121
1112
311
131
113
221
212
112
32
23

# right here, it would be useful to sort these lists 


eating_cookies(0) = 0
eating_cookies(1) = 1
eating_cookies(2) = 2
eating_cookies(3) = 4
eating_cookies(4) = 7
eating_cookies(5) = 13

# Very similar to Fibonacci Output, nice, works well to break down the problem in this way

'''

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies_noCASH(n, cache=None):
  if n < 0:
    return "You can't have negative cookies, right?"
  elif n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return eating_cookies_noCASH(n-1) + eating_cookies_noCASH(n-2) + eating_cookies_noCASH(n-3) 

''' Using Cache for optimization '''
def eating_cookies(n, cache=None):
  if cache is None:
    cache = {0: 1, 1:1, 2:2}
  if n < 0:
    return 0
  elif n not in cache:
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
  return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')