'''
Cut the Sticks:
https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''
def minimum(arr):
	m=arr[0]
	for i in range(1,len(arr)):
		if(m==0):
			m=arr[i]
		if(m>arr[i]):
			m=arr[i]
	return m
def noSticks(arr):
	c=0
	for i in arr:
		if(i!=0):
			c+=1
	return c
def cutTheSticks(arr):
	result=[]
	l=len(arr)
	arr=sorted(arr)
	for i in range(l):
		m=minimum(arr)
		sticks=noSticks(arr)
		result.append(sticks)
		for j in range(l):
			if(arr[j]>0):
				arr[j]=arr[j]-m
		if(any(arr)==False):
			break
	return result
