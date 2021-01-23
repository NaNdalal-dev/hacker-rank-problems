'''
Palindrome Index:
https://www.hackerrank.com/challenges/palindrome-index/problem
'''
def isPalindrome(s):
	if(s==s[::-1]):
		return True
	else:
		return False
def palindromeIndex(s):
	if s==s[::-1]:
		return -1
	set_s=set(s)
	for i in set_s:
		if(s.replace(i,'')==s.replace(i,'')[::-1]):
			return s.index(i)


