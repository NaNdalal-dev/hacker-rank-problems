'''
Link:
https://www.hackerrank.com/challenges/balanced-brackets/problem
'''
def isBalanced(s):
	lgt = len(s)
	if lgt%2 == 1:
		return "NO"
	flag = 1
	stk = [s[0]]
	for val in s[1:]:
		stk.append(val)
		if flag:
			if (stk[-2] =="(" and stk[-1] == ")") or (stk[-2] =="{" and stk[-1] == "}") or (stk[-2] =="[" and stk[-1] == "]"):
				stk.pop()
				stk.pop()
		if stk == []:
			flag = 0
		else:
			flag = 1
			
	if stk == [] :
		return "YES"
	return "NO"