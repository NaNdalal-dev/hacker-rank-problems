'''
Ice Cream Parlor:
https://www.hackerrank.com/challenges/icecream-parlor/problem
'''
def icecreamParlor(m, arr):
	n_arr=arr.copy()
	val=dict()
	for i in range(len(arr)):
		x=arr[i]
		y=m-x
		if(str(y) in val.keys()):
			yi=val[str(y)]+1
			xi=i+1
			return yi,xi
		else:
			val[str(x)]=i
		
	
