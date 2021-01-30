'''
Link:
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
'''
def digital_root(n):
    n = str(n)
    while len(n) != 1:
    	res = 0
    	for i in n:
    		res += int(i)
    	n = str(res)
    return int(n)