'''
Link:
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''

def tower_builder(n_floors):
	spaces = n_floors - 1
	tower = []
	towerStr = " "
	stars = 1
	for i in range(n_floors):
		x = towerStr*spaces + '*'*(stars) + towerStr*spaces
		tower.append(x)
		spaces -= 1
		stars += 2
	return tower
