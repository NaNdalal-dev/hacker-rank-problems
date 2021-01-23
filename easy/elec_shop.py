'''
Electronics Shop:
https://www.hackerrank.com/challenges/electronics-shop/problem
'''
def getMoneySpent(keyboards, drives, b):
	keyboards.sort(reverse=True)
	drives.sort(reverse=True)
	values=[]
	for k in keyboards:
		for d in drives:
			if(k+d<=b):
				values.append(k+d)
	if(values==[]):
		return -1
	else:
		return max(values)
