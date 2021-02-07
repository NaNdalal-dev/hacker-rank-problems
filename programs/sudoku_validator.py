'''
Link:
https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
'''

def valid_solution(board):
	count = 0
	for row in board:
		for i in range(1,10):
			if i not in row:
				return False
	new_rows = []
	sol_row = board[0]
	for i in range(9):
		new_rows = []
		for j in range(9):
			new_rows.append(board[j][i])
		for val in sol_row:
			if val not in new_rows:
				return False
	row=0
	c1 = 0;c2 = 3
	new_rows = []
	for k in range(3):
		for i in range(9):
			for j in range(c1,c2):
				row+=1
				new_rows.append(board[i][j])
				if row%9 == 0:
					for val in sol_row:
						if val not in new_rows:
							return False
					new_rows = []
		c1 += 3
		c2 += 3
	return True
