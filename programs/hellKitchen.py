"""
Link:
https://www.codewars.com/kata/57d1f36705c186d018000813/train/python
"""

from re import sub
def gordon(a):
	a =  sub('[aA]',"@",a)
	a = sub('[eiou]',"*",a).split(' ')
	l = len(a)
	result = ""
	for i in range(l):
		if i != l-1:
			result += a[i] + "!!!! "
		else:
			result += a[i] + "!!!!"
	return result.upper()

