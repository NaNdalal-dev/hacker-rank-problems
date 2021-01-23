def camelcase(s):
	count=1
	for i in s:
		if(ord(i)>=65 and ord(i)<=90):
			count+=1
	return count

