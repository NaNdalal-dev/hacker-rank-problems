"""
Link:
https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python
"""

def heron(a,b,c):

	s = (a + b +c)/2
	val = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	return round(val,2)

#print(heron(3,4,5))