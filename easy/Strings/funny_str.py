'''
Funny String:
https://www.hackerrank.com/challenges/funny-string/problem
'''
def funnyString(s):
	l=len(s)
	nums=[]
	for i in range(l-1):
		nums.append(abs(ord(s[i])-ord(s[i+1])))
	if(nums==nums[::-1]):
		return 'Funny'
	else:
		return 'Not Funny'
