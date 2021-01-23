'''
Lonely Integer:
https://www.hackerrank.com/challenges/lonely-integer/problem
'''
def count(a,val):
	c=0
	for i in a:
		if(val==i):
			c+=1
	return c

def lonelyinteger(a):
	for r in a:
		res=count(a,r)
		if(res==1):
			return r
