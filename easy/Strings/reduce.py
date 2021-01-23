'''
Super Reduced String:
https://www.hackerrank.com/challenges/reduced-string/problem
'''
def superReducedString(s):
	dup=s
	ns=sorted(set(s))
	xstr=''
	for i in s:
		if(dup.count(i)%2==1 and i not in xstr):
			xstr+=i
			#s=s.replace(i,'')
	return xstr if xstr!='' else 'Empty String'
