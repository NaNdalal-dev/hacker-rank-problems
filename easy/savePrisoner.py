def savePrisoner(n,m,s):
	r=m%n
	if((r+(s-1))%n==0):
		return n
	else:
		return (r+(s-1))%n

print(savePrisoner(4,6,2))
			
