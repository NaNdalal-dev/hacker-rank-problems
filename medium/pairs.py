'''
Pairs:
https://www.hackerrank.com/challenges/pairs/problem
'''
def pivot_ele(arr,first,last):
	pivot=arr[last]
	left=first
	right=last-1
	running=True
	while running:
		while(left<=right and arr[left]<=pivot):
			left+=1
		while(left<=right and arr[right]>=pivot):
			right-=1
		if(left>right):
			running=False
		else:
			arr[left],arr[right]=arr[right],arr[left]
	arr[last],arr[left]=arr[left],arr[last]
	return left
def quickSort(arr,first,last):
	if(first<last):	
		p=pivot_ele(arr,first,last)
		quickSort(arr,first,p-1)
		quickSort(arr,p+1,last)
		
def pairs(k, arr):
	quickSort(arr,0,len(arr)-1)
	return arr
