'''
Manasa and Stones:
https://www.hackerrank.com/challenges/manasa-and-stones/problem
'''
def stones(n, a, b):
	return sorted({x*a+(n-1-x)*b for x in range(n)})
		
