'''
Link:
https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
'''
def minimum(arr):
    min_val = arr[0]

    for val in arr[1:]:
    	if min_val > val:
    		min_val = val
    return min_val

def maximum(arr):
     max_val = arr[0]
     for val in arr[1:]:
     	if max_val < val:
     		max_val = val
     return max_val