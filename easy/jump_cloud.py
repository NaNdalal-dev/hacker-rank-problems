'''
Jumping on the Clouds:
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''
def jumpingOnClouds(c):
	l=len(c)
	if(l%2==1):
		fj=l//2
	else:
		if(c[l-1]==0):
			fj=l//2
		else:
			fj=(l//2)-1
	return fj
	non=0
	for i in range(l):
		if(c[i]==1):
			if(i>0 and c[i-1]!=0):
				fj-=1
			elif(i<l-1 and c[i+1]!=0):
				fj-=1
	return fj
