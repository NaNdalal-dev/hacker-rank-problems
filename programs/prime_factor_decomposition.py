'''
Link:
https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
'''
import math
def is_prime(n):
	if n<=1:
		return False
	elif n>2 and n%2 == 0:
		return False 
	else:
		for i in range(3,int(math.sqrt(n))+1,2):
			if n%i == 0:
				return False
		return True
