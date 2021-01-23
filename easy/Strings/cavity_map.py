'''
Cavity Map:
https://www.hackerrank.com/challenges/cavity-map/problem
'''
'''
for i in range(5):
	for j in range(5):
		if(i==0 or i==4 or j==0 or j==4):
			print("*",end=' ')
		else:
			print(" ",end=' ')
	print()
>>> str1 = "mystring"
>>> list1 = list(str1)
>>> list1[5] = 'u'
>>> str1 = ''.join(list1)
>>> print(str1)
mystrung
>>> type(str1)
'''
def l(x):
	return list([x])
def cavityMap(grid):
	l=len(grid)
	ngrid=['' for i in range(l)]
	for i in range(l):
		for j in range(l):
			if(i!=0 and i!=l-1 and j!=0 and j!=l-1):
				
				if((grid[i][j]>grid[i][j+1]) and (grid[i][j]>grid[i][j-1]) and (grid[i][j]>grid[i+1][j]) and (grid[i][j]>grid[i-1][j])):
					ngrid[i]+='X'#print(grid[i][j])
				else:
					ngrid[i]+=(grid[i][j])
			else:
				ngrid[i]+=(grid[i][j])
	return ngrid
	
	
	
	
	
	
