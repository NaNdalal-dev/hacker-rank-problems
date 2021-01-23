'''
Kangaroo:
https://www.hackerrank.com/challenges/kangaroo/problem
'''
def kangaroo(x1, v1, x2, v2):
	if(v1>v2):
		res=(x1-x2)%(v2-v1)
		if(res==0):
			return 'YES'
		else:
			return 'NO'
	return 'NO'
