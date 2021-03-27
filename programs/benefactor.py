"""
Link:
https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/python
"""
from math import ceil
def sum_len(arr):
	count = 0
	total = 0
	for val in arr:
		total += val
		count += 1
	return count, total

def new_avg(arr, newavg):
	length,summation = sum_len(arr)
	n = (length + 1)*newavg -summation
	if n <= 0:
		raise ValueError('-1')
	return ceil(n)