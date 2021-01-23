'''
Repeated String:
https://www.hackerrank.com/challenges/repeated-string/problem
'''
def repeatedString(s, n):
	l=len(s)
	a=0
	div=n//l
	re=n%l
	for i in s:
		if i=='a':
			a+=1
	if(re==0):
		return a*div
	else:
		a=a*div
		for i in s[:re]:
			if(i=='a'):
				a+=1
		return a
