"""
Link:
https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/train/python
"""
def switcher(arr):
	result = ""

	for char in arr:
		if int(char) >= 1 and int(char) <= 29:
			if char == "27":
				result += "!"
			elif char == "28":
				result += "?"
			elif char == "29":
				result += " "
			else:
				val = 122 - int(char) + 1
				result += chr(val)
	return result
print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))
