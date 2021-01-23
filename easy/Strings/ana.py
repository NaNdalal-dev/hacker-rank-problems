'''
Anagram:
https://www.hackerrank.com/challenges/anagram/problem
'''
def __len__(s):
	count=0
	for i in s:
		count+=1
	return count
def anagram(s):
	l=__len__(s)
	if(l%2==0):
			split=l//2
			s1=s[:split]
			s2=s[split:]
			
			min_count=0
			if(sorted(s1)==sorted(s2)):
				return 0
			xy=len(s1)
			n1=s1
			s1=set(s[:split])
			s2=set(s[split:])
			new_s=s1&(s1^s2)
			for le in new_s:
				min_count=min_count+n1.count(le)
			return min_count
			

	else:
		return -1
