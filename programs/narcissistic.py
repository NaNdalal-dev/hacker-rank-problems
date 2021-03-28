"""
Link:
https://www.codewars.com/kata/56b22765e1007b79f2000079/train/python
"""

def CountDigits(num):
	if num == 0:
		return 1
	count = 0
	while num:
		count += 1
		num //= 10
	return count

def is_narcissistic(num):
	temp = num
	length = CountDigits(num)
	result = 0
	while num:
		r = num % 10
		result = result + r ** length
		num //= 10
	return result == temp
print(is_narcissistic(1634))