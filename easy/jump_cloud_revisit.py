'''
Jumping on the Clouds: Revisited
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
'''
def jumpingOnClouds(c, k):
	l=len(c)
	e=100
	i=0
	while True:
		rem=(i+k)%l
		if rem==0:
			if c[rem]==1 :
				e=e-3
				break
			else:
				e-=1
				break
		if c[rem]==1 :
			e=e-3
		else:
			e-=1
		i+=k
	return e
