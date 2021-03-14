'''
Link:
https://www.codewars.com/kata/58e230e5e24dde0996000070/train/python
'''
from math import sqrt

def is_prime(num):
	if num <=1 :
		return False
	elif num > 2 and num%2 == 0:
		return False
	else:
		for i in range(3, int(sqrt(num))+1,2):
			if num%i == 0:
				return False
		return True


def next_prime(n):
	while True:
		n += 1

		if is_prime(n):
			return n
print(next_prime(181))