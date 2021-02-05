'''
Link:
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
'''
import string
lower = string.ascii_lowercase
def is_pangram(s):
	count = 0
	s = set(s.lower())
	for char in s:
		if char in lower:
			count += 1
	print(count)
	if count == 26:
		return True
	return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
    