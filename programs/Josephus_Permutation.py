'''
Link:
https://www.codewars.com/kata/555624b601231dc7a400017a/train/python
'''
import sys
sys.setrecursionlimit(10000)
def josephus_survivor(n,k):
	if n == 1:
		return 1
	else:
		return (josephus_survivor(n-1,k) + k-1 )% n + 1