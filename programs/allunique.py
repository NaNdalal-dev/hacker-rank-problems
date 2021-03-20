"""
Link:
https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python
"""
def has_unique_chars(string):
	unq_str = ""

	for char in string:
		if char in unq_str:
			return False
		else:
			unq_str += char
	return True

print(has_unique_chars("  "))