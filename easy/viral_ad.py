'''
Link for the description:
https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
print('''
Link for the description:
https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
)
def days(n):
	recipients=5
	cumulative=0
	for i in range(n):
		liked=recipients//2
		cumulative+=liked
		recipients=liked*3
	return cumulative
		
