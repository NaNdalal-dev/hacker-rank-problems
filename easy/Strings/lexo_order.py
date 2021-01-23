'''
Bigger is Greater(Medium):
https://www.hackerrank.com/challenges/bigger-is-greater/problem
'''
def biggerIsGreater(k):
	given=k
	k=list(k)
	i=j=l=len(k)-1
	for r in range(l,-1,-1):
		if(k[r-1]<k[r]):
			break
	for c in range(l,-1,-1):
		if(r>0 and k[r-1]<k[c]):
			#print(k[c])
			break
	k[r-1],k[c]=k[c],k[r-1]
	temp=k[r:]
	del k[r:]
	k=k+temp[::-1]
	nextVal=''
	for letter in k:
		nextVal+=letter
	if(nextVal>given):
		return nextVal
	else:
		return 'no answer'
	
