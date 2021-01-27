'''
Link:
https://www.hackerrank.com/challenges/simple-text-editor/problem
'''
def text_editor(n):
    s = ''
    stk = []
    for i in range(n):
    	q = input().split(' ')
    	if q[0] == '1':
    		stk.append(s)
    		s += q[1]
    		

    	elif q[0] == '2':
    		stk.append(s)	
    		s = s[:-int(q[1])]


    	elif q[0] == '3':
    		index = int(q[1]) - 1
    		print(s[index])

    	else:
    		s = stk.pop()
    	



n = int(input())
text_editor(n)