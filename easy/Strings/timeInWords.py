'''
The Time in Words:
https://www.hackerrank.com/challenges/the-time-in-words/problem
'''
def num_words():
	nword=["zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"];nums=[i for i in range(30)];d=dict(zip(nums,nword));return d
def timeInWords(h, m):
	numword=num_words()
	if(h!=12):
		if(m<=30):
			if(m==0):
				return "{} o' clock".format(numword[h])
			elif(m==15):
				return "quarter past {}".format(numword[h])
			elif(m==30):
				return "half past {}".format(numword[h])
			elif(m==1):#(int(str(m))==1):
				return "one minute past {}".format(numword[h])
			else:
				return "{} minutes past {}".format(numword[m],numword[h])
		else:
			q=60-m
			h=h+1
			if(m==45):
				return "quarter to {}".format(numword[h])
			elif(m==59):
				return "one minute to {}".format(numword[h])
			else:
				return "{} minutes to {}".format(numword[q],numword[h])
	elif(h==12):
		if(m<=30):
			if(m==0):
				return "{} o' clock".format(numword[h])
			elif(m==15):
				return "quarter past {}".format(numword[h])
			elif(m==30):
				return "half past {}".format(numword[h])
			elif(m==1):#(int(str(m))==1):
				return "one minute past {}".format(numword[h])
			else:
				return "{} minutes past {}".format(numword[m],numword[h])
		else:
			q=60-m
			if(m==45):
				return "quarter to {}".format(numword[1])
			elif(m==59):
				return "one minute to one".format(numword[q],numword[1])	
			else:
				return "{} minutes to {}".format(numword[q],numword[1])
