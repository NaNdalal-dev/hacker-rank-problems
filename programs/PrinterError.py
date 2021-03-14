"""
Link:
https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
"""
a_To_m = [chr(i) for i in range(97,110)] 
def printer_error(string):
	total = 0
	errors = 0
	for char in string:
		if char not in a_To_m:
			errors += 1
		total += 1
	result = f"{errors}/{total}"
	return result
