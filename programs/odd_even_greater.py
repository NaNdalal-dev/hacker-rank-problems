"""
Link:
https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python
"""

def even_or_odd(s):
    evens = 0
    odds = 0
    for val in s:
    	value = int(val)
    	if value%2:
    		odds += value
    	else:
    		evens += value
    if odds > evens:
    	return "Odd is greater than Even"
    elif evens > odds:
    	return 'Even is greater than Odd'
    return "Even and Odd are the same"

print(even_or_odd("12"))