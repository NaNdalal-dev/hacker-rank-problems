'''
Link for the description:
https://www.hackerrank.com/challenges/sock-merchant/problem
'''
def sockMerchant(n, ar):
	pair=0
	for i in range(n):
		if(ar[i]!=None):
			for j in range(i+1,n):
				if(ar[i]==ar[j]):
					ar[i]=ar[j]=None
					pair+=1
					i+=2
					break
	return pair

