'''Utopian Tree:
https://www.hackerrank.com/challenges/utopian-tree/problem'''
from math import ceil
def utopianTree(n):
	div=ceil(n/2)
	if(n%2==0):
		result=((2**div)*2)-1
		return result
	else:
		result=((2**div)*2)-2
		return result

