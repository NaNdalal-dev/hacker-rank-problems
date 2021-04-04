'''
Link:
https://www.codewars.com/kata/55eca815d0d20962e1000106/train/python
'''
def generate_range(m1, m2, step):
	'''
	return list(range(m1,m2,step))
	'''
	res = []
	while m1 <= m2:
		res.append(m1)
		m1 += step
	return res
