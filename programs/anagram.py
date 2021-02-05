'''
Link:
https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
'''
def anagrams(word, words=None):
	word = sorted(word)
	result = []
	for val in words:
		if word == sorted(val):
			result.append(val)
	return result