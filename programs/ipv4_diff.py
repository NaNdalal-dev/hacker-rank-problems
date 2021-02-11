'''
Link:
https://www.codewars.com/kata/526989a41034285187000de4/train/python
'''

first = lambda x : x*(256**3)
second = lambda x : x*(256**2)
third = lambda x : x*256

def ips_between(start, end):
	start = list(map(int,start.split('.')))
	end = list(map(int,end.split('.')))

	x1 = first(end[0]) - first(start[0])
	x2 = second(end[1]) - second(start[1])
	x3 = third(end[2]) - third(start[2])
	x4 = end[3] - start[3]

	return (x1 + x2 + x3 + x4)