'''
Link:
https://www.codewars.com/kata/5772ded6914da62b4b0000f8/train/python
'''

def palindrome_pairs(words):
	flag = 1
	res = []
	i = 0
	for r in words:
		j=0
		for c in words:
			x = str(r) 
			y =  str(c)
			val = x+y
			if i != j and (val == val[::-1]):
				res.append([i,j])
				break 
			j += 1
		i += 1
	return res
#print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
#print(palindrome_pairs(["bat", "tab", "cat"]))
#print(palindrome_pairs(["dog", "cow", "tap", "god", "pat"]))
#print(palindrome_pairs([5777, 'dog', 'god', True, 75]))