def insert1(arr):
	last=arr[len(arr)-1]
	for i in range(len(arr)-2,-1,-1):
		if(arr[i]>last):
			arr[i+1]=arr[i]
			print(arr[i])
		else:
			arr[i+1]=last
			break
	if last not in arr:
		arr[0]=last
		
	return arr

