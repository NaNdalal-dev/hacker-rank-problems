n=3
mat=[[0 for i in range(n)]for i in range(n)]
values=[k+1 for k in range(n*n)]
index=0
initial=True
r,c=int(n/2),n-1
for i in range((n*n)+1):
	if(r<0 and c>=n):
		r,c=0,n-2
	else:
		if(r<0):
			r=n-1
		if(c>=n):
			c=0
	if(mat[r][c] != 0):
		c-=2
		r+=1
		continue
	else:
		mat[r][c]=values[index]
	index+=1
	r,c=r-1,c+1
		
	
print(mat)
