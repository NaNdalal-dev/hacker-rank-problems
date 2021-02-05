'''
Link:
https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python
'''
def all_two(val):
	return val == 2

def all_one(val):
	return val == 1
def is_solved(board):
	print(board)
	a,b,c = board[0][0],board[1][1],board[2][2]
	if a == b == c == 1 or  a == b == c == 2:
		return a
	e,f,g = board[0][2],board[1][1],board[2][0]
	if e == f == g == 1 or  e == f == g == 2:
		return e

	for row in board:
		twos = list(map(all_two,row))
		ones = list(map(all_one,row))
		if all(twos):
			return 2
		elif all(ones):
			return 1

	a,b,c = board[0][0],board[1][0],board[2][0]
	if a == b == c == 1 or  a == b == c == 2:
		return a
	a,b,c = board[0][1],board[1][1],board[2][1]
	if a == b == c == 1 or  a == b == c == 2:
		return a	
	a,b,c = board[0][2],board[1][2],board[2][2]
	if a == b == c == 1 or  a == b == c == 2:
		return a
	for row in board:
		if 0 in row:
			return -1
	return 0

board = [[1, 2, 1],
         [1, 1, 2],
         [2, 1, 1]]
print(is_solved(board))