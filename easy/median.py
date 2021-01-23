def median(arr):
	for i in range(len(arr)-1,0,-1):
		for j in range(i):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	med=len(arr)//2
	return arr
