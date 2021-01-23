'''
Maximizing XOR:
https://www.hackerrank.com/challenges/maximizing-xor/problem
'''
def maximizingXor(l, r):
	arr=[i for i in range(l,r+1)]
	res=[]
	for i in arr:
		for j in arr:
			if((i%2==0 and j%2==1) or (i%2==1 and j%2==0)):
				res.append(i^j)
	return max(res)
