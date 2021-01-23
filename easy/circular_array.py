'''
Link for the description:
https://www.hackerrank.com/challenges/circular-array-rotation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
print('''
https://www.hackerrank.com/challenges/circular-array-rotation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
''')
'''
def circularArrayRotation(arr, k, queries):
	for i in range(k):
		n_arr=[arr[len(arr)-1]]
		for i in range(len(arr)-1):
			n_arr.append(arr[i])
		arr=n_arr.copy()
	sol=[n_arr[i] for i in queries]
	return sol
'''
def circularArrayRotation(arr,k,queries):
	for i in range(len(queries)):
		queries[i]=arr[(queries[i]-k)%len(arr)]
	return queries
