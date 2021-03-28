"""
Link:
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python
"""

def jumping_number(num):
	currentNum = num %10
	num //= 10

	while num:
		r = num % 10
		result = r - currentNum

		if result == -1 or result == 1:
			currentNum = r
			num //= 10
		else:
			return "Not!!"

	return "Jumping!!"

print(jumping_number(321))
