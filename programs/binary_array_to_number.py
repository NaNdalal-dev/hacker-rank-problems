'''
Link:
https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
'''
def binary_array_to_number(arr):
	result = 0
	i = 0
	for val in arr[::-1]:
		result += (2**i)*val
		i += 1
	return result
print(binary_array_to_number([0,0,1,1]))