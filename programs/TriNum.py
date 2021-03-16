"""
Link:
https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python

Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.
"""


def is_triangular(t):
	x = int((t*2) ** 0.5)
	print(x)
	return t == x*(x+1)/2
print(is_triangular(2))
print(is_triangular(7))
print(is_triangular(14))
print(is_triangular(27))
print(is_triangular(28))