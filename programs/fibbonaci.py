"""
Link:
https://www.codewars.com/kata/5239f06d20eeab9deb00049b/train/python
"""
def fibonacci(n):
    if n <= 0:
    	return []
    if n == 1:
    	return [0]
    fibbArray = [0,1]
    for i in range(2,n):
    	fibbArray.append(fibbArray[i-2] + fibbArray[i-1])
    return fibbArray