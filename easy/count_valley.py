'''
Counting Valleys:
https://www.hackerrank.com/challenges/counting-valleys/problem
'''
def countingValleys(n, s):
	v=0
	valley=0
	for i in s:	
		if(i=='U'):
			v+=1
			if(v==0):
				valley+=1
		else:
			v-=1
	return valley
