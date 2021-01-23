num=int(input())
x=1
for i in range(num):
	if(i%2==0):
		for even_row in range(num):
			print(x,end=' ')
			x+=1
		x-=1
	else:
		y=x+num
		for odd_row in range(num):
			print(y,end=' ')
			y-=1
			x+=1
		x+=1
	print()
