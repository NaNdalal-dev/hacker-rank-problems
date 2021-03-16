"""
Link:
https://www.codewars.com/kata/563b662a59afc2b5120000c6
"""

def nb_year(p0, percent, aug, p):
	print(p0, percent, aug, p)
	x = p0
	count = 0
	while True:
		x = int(x+(x * (percent/100)) + aug)
		count += 1
		print(x)
		if x >= p:
			return count