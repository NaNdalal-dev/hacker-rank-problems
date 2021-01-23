'''
Modified Kaprekar Numbers:
https://www.hackerrank.com/challenges/kaprekar-numbers/problem?h_r=next-challenge&h_v=zen
'''
def count(n):
	c=0
	while(n):
		n//=10
		c+=1
	return c
def kaprekarNumbers(p, q):
	s=''
	for i in range(p,q+1):
		sq_val=i**2
		d=count(i)
		if(count(sq_val)==2*count(i)):
			left=int(str(sq_val)[:d])
			right=int(str(sq_val)[d:])
			res=left+right
			if(i==res):
				s=s+str(res)+' '
		elif(count(sq_val)==1):
			if(sq_val==i):
				res=i
				s=s+str(res)+' '	
		else:
			left=int(str(sq_val)[:d-1])
			right=int(str(sq_val)[d-1:])
			res=left+right
			if(i==res):
				s=s+str(res)+' '	
	if(s==''):
		print('INVALID RANGE')
	else:
		print(s)
