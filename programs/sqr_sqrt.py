"""
Link:
https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python
"""
from math import sqrt

def sum_square_even_root_odd(nums):
	total = 0

	for value in nums:
		if value%2:
			total += sqrt(value)
		else:
			total += value**2
	return round(total,2)
