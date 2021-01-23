'''
Link:
https://www.hackerrank.com/challenges/2d-array/problem
'''
def hourglassSum(x):
	sums = []
	x1=0
	for i in range(4):
		y1=0
		for j in range(4):
			r1=sum((x[x1][j:y1+3]))
			mid=x[x1+1][y1+1]
			r2=sum((x[x1+2][j:y1+3]))
			result = r1+mid+r2
			sums.append(result)
			y1+=1
		x1+=1
	return max(sums)