'''
Between Two Sets:
https://www.hackerrank.com/challenges/between-two-sets/problem
'''
def getFactors(n,minimum):

	factors=[]
	for i in range(2,minimum+1,2):
		if i%n==0:
			#print(minimum,i)
			factors.append(i)
	
	return factors

def getTotalX(a, b):
	minimum=min(b)
	x=0
	for i in a:
		k=getFactors(i,minimum)
		print(k)
		if x==0:
			setx=set(k)
		else:
			setx=setx.intersection(k)
		x+=1
	count=0
	x=0
	for bval in b:
			for s in setx:
						
	#return setx

if __name__=='__main__':
	#print(getFactors(910))
	print(getTotalX([2,4],[16,32,96]))
