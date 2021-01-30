'''
Link:
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
'''
def unique_in_order(string):
	if string:
	    unique = [string[0]]
	    i = 0
	    for val in string[1:]:
	    	if val == unique[i]:
	    		pass
	    	else:
	    		unique.append(val)
	    		i+=1
	    return unique
	else:
		return []

#print(unique_in_order('ABBCcAD'))
