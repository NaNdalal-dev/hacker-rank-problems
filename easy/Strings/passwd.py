'''
Strong Password:
https://www.hackerrank.com/challenges/strong-password/problem
'''
def minimumNumber(n, password):
	left_chars=0
	num=0
	lower=0
	upper=0
	spl=0
	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"
	for letter in password:
		if(letter in numbers):
			num+=1
		elif(letter in upper_case):
			upper+=1
		elif(letter in lower_case):
			lower+=1
		elif(letter in special_characters):
			spl+=1
	if(num==0):
		left_chars+=1
	if(lower==0):
		left_chars+=1
	if(upper==0):
		left_chars+=1
	if(spl==0):
		left_chars+=1
	return max(left_chars,6-n)
