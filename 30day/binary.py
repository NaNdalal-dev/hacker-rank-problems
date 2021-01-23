n=int(input())
binary=''
if(n<0):
	n=-n
while(n):
	r=n%2
	binary+=str(r)
	n//=2
binary=(binary[::-1])
ones=0
vals=[]
for i in range(len(binary)):
	if(binary[i]=='1'):
		ones+=1
		vals.append(ones)
	else:
		ones=0
print(max(vals))
