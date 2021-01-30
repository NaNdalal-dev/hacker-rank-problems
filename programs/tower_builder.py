'''
Link:
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''
def tower_builder(n):
	result = []
	space = ''
	tower = ''
	for i in range(n):
		space = space+' '*(n-i-2)
		#print(space)
		tower = (space+'*'*(i+1)+space)
		result.append(tower)
		print(result)
tower_builder(3)
