
import statistics as s
def pivot_place(arr,first,last):
	low=arr[first]
	high=arr[last]
	mid=(low+high)//2
	piv_val=s.median([low,arr[mid],high])
	if(piv_val==low):
		pindex=first
	elif(piv_val==high):
		pindex=last
	else:
		pindex=mid
	arr[last],arr[pindex]=arr[pindex],arr[last]
	pivot=arr[last]
	left=first
	right=last-1
	running=True
	while(running):
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
		p=pivot_place(arr,first,last)
		quickSort(arr,first,p-1)	
		quickSort(arr,p+1,last)


