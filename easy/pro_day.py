'''
Day of the Programmer:
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''
def dayOfProgrammer(year):
	if(year>=1919):
		if((year%400==0) or (year%4==0 and year%100!=0)):
			return '12.09.{}'.format(year)
		else:
			return '13.09.{}'.format(year)
	elif(year<=1917):
		if(year%4==0):
			return '12.09.{}'.format(year)
		else:
			return '13.09.{}'.format(year)
	elif(year==1918):
		return '26.09.{}'.format(year)		
