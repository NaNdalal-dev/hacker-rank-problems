'''
Link:
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
'''

def alphabet_position(text):
	result = ""

	for char in text:
		if char >= 'a' and char <= 'z':
			result +=  ' '+str(ord(char) - 96) 

		elif char >= 'A' and char <= 'Z':
			result +=  ' '+str(ord(char) - 64) 
	return result.replace(' ','',1)
#print(alphabet_position("The sunset sets at twelve o' clock."))