'''
The Hurdle Race:
https://www.hackerrank.com/challenges/the-hurdle-race/problem
'''
def maximum(arr):
	m=arr[0]
	for i in range(1,len(arr)):
		if(m<arr[i]):
			m=arr[i]
	return m
def hurdleRace(k, height):
	magic=maximum(height)
	if(k>magic):
		return 0
	else:
		return magic-k
