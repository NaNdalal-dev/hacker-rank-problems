'''
Gemstones:
https://www.hackerrank.com/challenges/gem-stones/problem
'''
def gemstones(arr):
	gem=set(arr[0])
	l=len(arr)
	if(l==1):	
		return len(gem)
	for i in range(1,l):
		gem=gem.intersection(arr[i])
	return len(gem)
