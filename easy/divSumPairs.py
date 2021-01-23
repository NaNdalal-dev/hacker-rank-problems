'''
Divisible Sum Pairs:
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
def divisibleSumPairs(n,k,ar):
	count=0
	for i in range(n):
		for j in range(n):
			if(i<j and (ar[i]+ar[j])%k==0):
				count+=1
	return count
	
