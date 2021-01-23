'''
Alternating Characters:
https://www.hackerrank.com/challenges/alternating-characters/problem
'''
def alternatingCharacters(s):
	l=len(s)
	del_count=0
	for i in range(l-1):
		if(s[i]==s[i+1]):
			del_count+=1
	return del_count
