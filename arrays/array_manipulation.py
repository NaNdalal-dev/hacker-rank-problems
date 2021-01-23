'''
Link:
https://www.hackerrank.com/challenges/crush/problem
'''


def prefixsum(arr):
	maximum = 0
	sums=[]
	va=0
	for val in arr:
		va+=val
		maximum = max(maximum,va)
	return maximum

def arrayManipulation(n,queries):
	arr = [0 for i in range(n+2)]

	for q in queries:
		a,b,k = q
		arr[a] += k
		arr[b+1] = arr[b+1]-k
	result = prefixsum(arr)
	return result