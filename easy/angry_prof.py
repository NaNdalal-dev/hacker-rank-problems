def angryProfessor(k,arr):
	intime=0
	for i in arr:
		if(i<=0):
			intime+=1
	if(intime<k):
		return 'NO'
	else:
		return 'YES'
