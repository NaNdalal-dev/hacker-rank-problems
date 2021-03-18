"""
Link:
https://www.codewars.com/kata/604287495a72ae00131685c7/train/python
"""
def doubleton(num):
    while True:
    	num += 1
    	if len(set(str(num))) == 2:
    		return num

print(doubleton(10))