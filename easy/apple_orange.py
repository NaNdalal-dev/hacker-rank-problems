def countApplesAndOranges(s, t, a, b, apples, oranges):
	dist=range(s,t+1)
	apple_loc=a
	orange_loc=b
	apple_count=0
	orange_count=0
	for i in apples:
		#print(apple_loc,'+',i,'=',apple_loc+i)
		if((apple_loc+i) >=s and (apple_loc+i) <=t):
			apple_count+=1
	for j in oranges:
		#print(orange_loc,'+',j,'=',orange_loc+i)
		if((orange_loc+j)>=s and (orange_loc+j) <=t):
			orange_count+=1
	print(apple_count)
	print(orange_count)

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
