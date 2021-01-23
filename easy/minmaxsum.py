
def miniMaxSum(arr):
	sums=[]
	for i in range(len(arr)):
		x=arr[i]
		arr[i]=0
		sums.append(sum(arr))
		arr[i]=x
	
	minimum=sums[0]
	for i in range(1,len(sums)):
		if(sums[i]<minimum):
			minimum=sums[i]
	maximum=sums[0]
	for i in range(1,len(sums)):
		if(sums[i]>maximum):
			maximum=sums[i]
	print(minimum,maximum)
