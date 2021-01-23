'''
Migratory Birds:
https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
def migratoryBirds(arr):
	one=two=three=four=five=0
	for i in arr:
		if(i==1):
			one+=1
		elif(i==2):
			two+=1
		elif(i==3):
			three+=1
		elif(i==4):
			four+=1
		elif(i==5):
			five+=1
	birdIds=[one,two,three,four,five]
	result=birdIds.index(max(birdIds))+1
