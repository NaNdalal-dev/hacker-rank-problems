'''
Link for Description:
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''
def breakingRecords(scores):
	currentHighScore=scores[0]
	currentLowScore=scores[0]
	hs=0
	ls=0
	for i in range(1,len(scores)):
		if(currentHighScore<scores[i]):
			currentHighScore=scores[i]
			hs+=1
		if(currentLowScore>scores[i]):
			currentLowScore=scores[i]
			ls+=1
	return (hs,ls)
