'''
Link:
https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
'''
def number(bus_stops):
	result = 0
	for vals in bus_stops:
		came_in, left = vals
		result += came_in
		result -= left
	return result

#print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
#print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))
#print(number([[10,0],[3,5],[5,8]]))
