def birthdayCakeCandles(arr):
	maximum=arr[0]
	for i in range(1,len(arr)):
		if(arr[i]>maximum):
			maximum=arr[i]
	count=0
	for i in range(len(arr)):
		if(arr[i]==maximum):
			count+=1
	return count
