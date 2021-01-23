def countSort1(arr):
	l=len(arr)
	k=max(arr)+1
	new_arr=[0 for i in range(k)]
	for i in range(l):
		new_arr[arr[i]]+=1
	return new_arr
