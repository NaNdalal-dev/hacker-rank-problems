'''
Sequence Equation:
https://www.hackerrank.com/challenges/permutation-equation/problem
'''
def minus1(a):
	return a-1
def permutationEquation(p):
	p=list(map(minus1,p))
	l=len(p)
	eq=0
	res=[]
	for x in range(l):
		res.append(p.index(p.index(p[x]-1))+1)
	return res
