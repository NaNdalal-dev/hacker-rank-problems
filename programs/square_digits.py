'''
Link:
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
'''
def square_digits(num):
	concat = ''
	for n in str(num):
		concat += str(int(n)**2)
	return int(concat)


#print(square_digits(9119))