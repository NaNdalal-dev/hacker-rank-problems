"""
Link:
https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
"""

changeSign = lambda n : -n

def invert(lst):
    if lst:
    	return list(map(changeSign,lst))
    return []

print(invert([1,2,-3,-4]))