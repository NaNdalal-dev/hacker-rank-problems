'''
Link:
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
'''
def findlen(data):
	count = 0
	for val in data:
		count += 1
	return count

def validate_pin(pin):
	pin_len = findlen(pin)
	digit_counter = 0
	if pin_len == 4 or pin_len == 6:
		for val in pin:
			if val.isdigit():
				digit_counter += 1
	else:
		return False

	if digit_counter == pin_len:
		return True
	return False

