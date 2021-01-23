'''
>>> for i in range(5):
...     for j in range(i,i+3):
...             print(j,end=' ')
...     print()
Link for Description:
https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen
'''
def birthday(s, d, m):
	l=len(s)
	__sum__=0
	count=0
	for i in range(l-m+1):
		for j in range(i,i+m):
			__sum__+=s[j]
		if(__sum__==d):
			count+=1
		__sum__=0
		
	return count
