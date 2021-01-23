'''
Counting Sort 2:
https://www.hackerrank.com/challenges/countingsort2/problem
'''
def countSort1(arr):
	l=len(arr)
	k=max(arr)+1
	new_arr=[0 for i in range(k)]
	for i in range(l):
		new_arr[arr[i]]+=1
	srt=[]
	index=0
	for r in new_arr:
		for c in range(r):
			srt.append(index)
		index+=1
	return srt
