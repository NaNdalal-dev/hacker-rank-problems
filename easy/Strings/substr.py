def subStr(s1,s2):
	s1=set(s1)
	s2=set(s2)
	flag="NO"
	for i in s1:
		for j in s2:
			if(i==j):
				flag="YES"
				break
	return flag
x='hello'
y='i'
print(subStr(x,y))
