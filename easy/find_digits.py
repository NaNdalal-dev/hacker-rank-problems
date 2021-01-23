'''
Find digits:
https://www.hackerrank.com/challenges/find-digits/problem
'''
def findDigits(n):
	m=n
	count=0
	while(n):
		r=n%10
		if(r!=0 and m%r==0):
			count+=1
		n//=10
	return count
print(findDigits(1012))
