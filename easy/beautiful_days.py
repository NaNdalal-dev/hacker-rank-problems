'''
Link:
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen
'''
print('Link for the Description:\nhttps://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen')
def reverse(num):
	rev=0
	while(num):
		r=num%10
		rev=rev*10+r
		num//=10
	return rev
def beautifulDays(start,end,div):
	bdays=0
	for i in range(start,end+1):
		if(abs(i-reverse(i))%div==0):
			bdays+=1
	return bdays
