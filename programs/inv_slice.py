"""
Link:
https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python
"""

def inverse_slice(items, a, b):
	i = a
	index = 0
	new_arr = []
	for value in items:
		if i == index and i<b :
			i += 1
		else:
			new_arr.append(items[index])
		index += 1
	return new_arr