'''
Link:
https://www.codewars.com/kata/605f5d33f38ca800322cb18f
'''

from math import ceil

def tap_code_translation(text,result = ""):
    text = text.upper()
    for char in text:
    	x = ord(char[0])
    	if char < 'K':
    		row, col = ceil((x-64)/5),ceil((x-64)%5)
    		
    		if col == 0:
    			col = 5
    			
    		result = result + ('.'*row) +' '+('.'*col)
    	
    	elif  char > 'K':
    			row, col = ceil((x-65)/5),ceil((x-65)%5)
    			if col == 0:
    				col = 5
    			result = result + ('.'*row) +' '+('.'*col)
    	
    	else:
    		row, col = 1,3
    		result = result + ('.'*row) +' '+('.'*col)
    	print(row,col)
    	result += ' '
    return result.rstrip(result[-1])
