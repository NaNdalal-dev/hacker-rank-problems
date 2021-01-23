'''
Minimum Distances:
https://www.hackerrank.com/challenges/minimum-distances/problem
'''
def minimumDistances(a):
	indexes=dict()
	
	minimum=[]
	for i in range(len(a)):
		if indexes.get(str(a[i])) is not None:
			minimum.append(abs(indexes.get(str(a[i]))-i))
		else:
			indexes[str(a[i])]=i
			
	if minimum==[]:
		return -1
	return min(minimum)
