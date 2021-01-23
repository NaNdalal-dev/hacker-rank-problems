'''
Fair Rations:
https://www.hackerrank.com/challenges/fair-rations/problem
'''
def even(n):
	return n%2==0
def fairRations(B):
	count=0
	for i in range(len(B)-1):
		if(B[i]%2==0):
			pass
		else:
			B[i]+=1
			B[i+1]+=1
			count+=2
	if(all(list(map(even,B)))):
		return count
	else:
		return 'NO'
