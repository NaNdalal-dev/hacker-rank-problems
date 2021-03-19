"""
Link
https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):

	if distance_to_pump // fuel_left == mpg:
		return True
	return False