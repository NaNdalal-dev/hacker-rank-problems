'''
Link for description:
https://www.hackerrank.com/challenges/drawing-book/problem
'''
def pageCount(n, p):	
	turn_from_first=p//2
	if(n%2==1):
		turn_from_last=(n-p)//2
	else:
		if(p%2==1):
			turn_from_last=((n-p)//2)+1
		else:
			turn_from_last=(n-p)//2	
	if(turn_from_first<turn_from_last):
		return turn_from_first
	else:
		return turn_from_last
