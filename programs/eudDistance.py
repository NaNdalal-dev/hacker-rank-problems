"""
Link:
https://www.codewars.com/kata/58dced7b702b805b200000be/train/python
"""
"""
This code is already predefined in codewars
class Point:
	def __init__(self, a, b):
		self.x = a
		self.y = b
"""
distance_between_points = lambda a,b: round((abs(a.x - b.x)**2 + abs(a.y- b.y)**2 )**0.5,6)

