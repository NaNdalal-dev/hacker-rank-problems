'''
Encryption:
https://www.hackerrank.com/challenges/encryption/problem
'''
from math import sqrt,ceil,floor
def encryption(s):
	s=s.replace(' ','')
	l=len(s)
	rows=floor(sqrt(l))
	cols=ceil(sqrt(l))
	if(rows*cols>=l):
		i=0
		words=[]
		
		for r in range(rows):
			new_s=''
			for c in range(cols):
				try:
					#print(s[i],end='')
					new_s+=s[i]
					i+=1
				except:
					break
			words.append(new_s)
			#print()
		colnrows=[[] for i in range(cols)]
		
		for word in words:
			i=0
			for letter in word:
				colnrows[i].append(letter)
				i+=1
		#print('list1:',colnrows)
		final_s=''
		for r1 in colnrows:
			for c1 in r1:
				final_s+=c1
			final_s+=' '
		return final_s
	else:
		minimum=min([rows,cols])
		if(rows==minimum):
			while True:
				rows+=1
				if(rows*cols>=l):
					break
		else:
			while True:
				cols+=1
				if(rows*cols>=l):
					break
		#Repeat the same process of above if statement
		i=0
		words=[]
		
		for r in range(rows):
			new_s=''
			for c in range(cols):
				try:
					#print(s[i],end='')
					new_s+=s[i]
					i+=1
				except:
					break
			words.append(new_s)
			#print()
		colnrows=[[] for i in range(cols)]
		
		for word in words:
			i=0
			for letter in word:
				colnrows[i].append(letter)
				i+=1
		#print('list1:',colnrows)
		final_s=''
		for r1 in colnrows:
			for c1 in r1:
				final_s+=c1
			final_s+=' '
		return final_s
			
#(encryption('if man was meant to stay on the ground god would have given us roots'))
