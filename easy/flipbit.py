'''
Flipping bits:
https://www.hackerrank.com/challenges/flipping-bits/problem
'''
def make32(n):
	x=''
	for i in range(n):
		x+='1'
	return x
def inv_bin_to_dec(inv_bin):
	inv_bin=inv_bin[::-1]
	bit=0
	i=0
	power=0
	ans=0
	while(bit<32):
		ans=ans+((2**power)*int(inv_bin[i]))
		i+=1
		power+=1
		bit+=1
	return ans
def flippingBits(n):
	#bin_num=''
	inv_bin=''
	while n:
		r=n%2
		if(r==0):
			inv_bin+='1'
		else:
			inv_bin+='0'
		#bin_num+=str(r)
		#print(r)
		n//=2
	l=make32(32-len(inv_bin))
	inv_bin=l+inv_bin[::-1]
	return inv_bin_to_dec(inv_bin)	
