'''
Picking Numbers
https://www.hackerrank.com/challenges/picking-numbers/problem
'''
def pickingNumbers(arr):
	index_arr=[0 for i in range(101)]
	for i in arr:
		index_arr[i]+=1
	result=index_arr[1]+index_arr[0] #Default max
	for r in range(2,101):
		result=max(result,index_arr[r]+index_arr[r-1])
	return result
if __name__=='__main__':
	print(pickingNumbers([4,6,5,3,3,1]))
