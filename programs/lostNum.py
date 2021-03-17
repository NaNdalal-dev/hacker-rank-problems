"""
Link:
https://www.codewars.com/kata/595aa94353e43a8746000120/train/python
"""
def find_deleted_number(arr, mixed_arr):
	print(arr)
	print(mixed_arr)
	if arr == [] and mixed_arr == []:
		return 0
	elif mixed_arr == []:
		return arr[0]

	mixed_arr.sort()
	index = 0

	for value in mixed_arr:
		if value != arr[index]:
			return arr[index]
		index += 1
	return 0
print(find_deleted_number([],[]))