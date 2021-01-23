def pivot_ele(arr,first,last):
	pivot=arr[first]
	left=first+1
	right=last
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
		arr[first],arr[right]=arr[right],arr[first]
	return right
def quickSort(arr,first,last):
	if(first<last):	
		p=pivot_ele(arr,first,last)
		quickSort(arr,first,p-1)
		quickSort(arr,p+1,last)

