"""
Link:
https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
"""

def rental_car_cost(days):
	if days < 3:
		return days * 40

	elif days >= 3 and days < 7:
		return (days * 40) - 20
	
	return (days * 40) - 50
