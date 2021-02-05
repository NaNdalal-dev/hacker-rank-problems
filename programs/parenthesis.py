'''
Link:
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
'''

def valid_parentheses(string):
	if string == "":
		return True
	flag = 1
	i = -1
	result = []
	for char in string:
		if flag:
			if char == ')':
				return False
			flag = 0
		if char == '(' or char == ')':
			result.append(char)
			i+=1

		if i>0:
			if result[-2] == '(' and result[-1] == ')':
				result.pop()
				result.pop()
				i-=2

	if result == []:
		return True
	return False	