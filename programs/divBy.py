"""
Link:
https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
"""

def divisible_by(numbers, divisor):
	divs = []
	for value in numbers:
		if value % divisor == 0:
			divs.append(value)
	return divs