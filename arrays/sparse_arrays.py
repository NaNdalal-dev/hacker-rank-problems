'''
Link:
https://www.hackerrank.com/challenges/sparse-arrays/problem
'''
def matchingStrings(strings, queries):
	vals = []
	for q in queries:
		count = 0
		for ins in strings:
			if q == ins:
				count+=1
		vals.append(count)
	return vals