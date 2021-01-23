'''
Non-Divisible Subset:
https://www.hackerrank.com/challenges/non-divisible-subset/problem
'''
def notDivByK(s,k):
	l=len(s)
	cnt=0
	for i in range(l):
		for j in range(l):
			if(i!=j):
				sumij=s[i]+s[j]
				if(sumij%k!=0):
					cnt+=1
	if(cnt==l):
		return True
	else:
		return False	
def nonDivisibleSubset(k, s):
	l=len(s)
	listSet=set()
	for i in range(l):
		for j in range(l):
			if(i!=j):
				sumij=s[i]+s[j]
				if(sumij%k!=0):
					listSet.update([s[i],s[j]])
	if(notDivByK(list(listSet),k)):
		nonDivisibleSubset(k,list(listSet))
	return len(listSet)
print(nonDivisibleSubset(7,[278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))
