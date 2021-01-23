'''
Library Fine:
https://www.hackerrank.com/challenges/library-fine/problem
'''
def libraryFine(d1, m1, y1, d2, m2, y2):
	fine=0
	if(m1==m2 and y1==y2 and d2<d1):
		fine=(d1-d2)*15
		return fine
	elif(y1==y2 and m2<m1):
		fine=(m1-m2)*500
		return fine
	elif(y2<y1):
		fine=(y1-y2)*10000
		return fine
	else:
		return fine
