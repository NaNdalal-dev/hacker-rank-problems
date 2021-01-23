def mat(arr):
	r=-1
	row=0
	for k in range(4):
		for i in range(3):
			for j in range(k,k+3):
				print(row,end=' ')
				row+=1
				#print(arr[r][c],end=' ')
				
			print()
			row-=2
arr=[[i for i in range(1,7)],[i for i in range(7,13)],[i for i in range(13,19)],[i for i in range(19,25)],[i for i in range(25,31)],[i for i in range(31,37)]]
mat(arr)
