def plusMinus(arr):
	l=len(arr)
	plus=0
	minus=0
	zeros=0
	for i in arr:
		if(i>0):
			plus+=1
		elif(i<0):
			minus+=1
		else:
			zeros+=1
	plus_ratio=float(format(plus/l,'6g'))
	minus_ratio=float(format(minus/l,'6g'))
	zero_ratio=float(format(zeros/l,'6g'))
	
	print(plus_ratio)
	print(minus_ratio)
	print(zero_ratio)
plusMinus([-4,3,-9,0,4,1])
