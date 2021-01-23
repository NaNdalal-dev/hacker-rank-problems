'''
Strange Counter:
https://www.hackerrank.com/challenges/strange-code/problem
'''
def level(n):
	count=1
	while True:
		if(n==1 or n==2 or n==3):
			break
		if((n+1)%2==0):
			n=((n+1)//2)-2
		else:
			n=((n+1)//2)-1
		count+=1
	return count
def strangeCounter(t):
	lvl=level(t)
	max_level=(3*(2**lvl))-3
	return max_level-t+1
