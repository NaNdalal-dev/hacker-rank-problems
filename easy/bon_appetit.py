'''
Bon Appetit:
https://www.hackerrank.com/challenges/bon-appetit/problem
'''
def sumOfBillBy2(bill):
	s=0
	for i in bill:
		s+=i
	return s/2
def bonAppetit(bill, k, b):
	refund=bill[k]/2
	bill[k]=0
	paid=sumOfBillBy2(bill)
	if(paid==b):
		print('Bon Appetit')
	else:
		print(refund)
