'''
Equalize the Array:
https://www.hackerrank.com/challenges/equality-in-a-array/problem
'''
def mincount(arr):
	l=len(arr)
	count=0
	c=[]
	for i in range(l):
		for j in range(l):
			if(arr[i]!=arr[j]):
					count+=1
		c.append(count)
	return min(x)

def equalizeArray(arr):
	return mincount(arr)
	
#done
