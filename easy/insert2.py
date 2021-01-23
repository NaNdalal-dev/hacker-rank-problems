def insertionSort(arr):
	k=0
	for index in range(1,len(arr)):
		current_ele=arr[index]
		pos=index
		while(current_ele<arr[pos-1] and pos>0):
			k+=1
			arr[pos]=arr[pos-1]
			pos-=1
		arr[pos]=current_ele
		#for i in arr :
		#	print(i,end=' ')
		#print()
	print(k)
			
arr=[2,1,3,1,2]
insertionSort(arr)
