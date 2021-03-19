"""
Link:
https://www.codewars.com/kata/603b2bb1c7646d000f900083/train/python
"""

def shifter(sentence): 
    if sentence:
    	words = set(sentence.split(" "))
    	count = 0
    	for word in words:
    		flag = 0
    		for letter in word:
    			if letter == "H" or  letter == "I" or  letter == "N" or  letter == "O" or  letter == "S" or  letter == "X" or letter == "Z" or letter == "M" or letter == "W":
    				flag = 1
    			else:
    				break
    		if flag:
    			count += 1
    	return count

    return 0

print(shifter("I II III II"))