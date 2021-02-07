'''
Link:
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

Reference Link:
https://brilliant.org/wiki/trailing-number-of-zeros/
'''

from math import log,ceil
def zeros(n):
	if n <= 4:
		return 0
	k = int(ceil(log(n,5)))
	res = 0
	for i in range(1,k+1):
		res += (n//(5**i))
	return res
