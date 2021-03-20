"""
Link:
https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
"""
def array(string):
    if string:
    	new_str=""
    	i = 1
    	for char in string.split(",")[1:-1]:
    		if i:
    			new_str += char
    			i = 0
    		else:
    			new_str += " "+char
    	if new_str != " " and new_str:
    		return new_str
    return