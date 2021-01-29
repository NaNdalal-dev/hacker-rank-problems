'''def gameoftwo(n):
	A = []
	B = []
	count = 0
	for i in range(n):
		x= list(map(int,input().split()))

		
		A = list(map(int,input().split()))

		B  = list(map(int,input().split()))
	

	limit = int(x[2])
	x = 0;sums = 0; a=-1;b=-1
	while True:
		if sums > limit:
			return count + 1
		if x%2 == 0:
			sums += A[a]
			a-=1
			count += 1
		else:
			sums += B[b]
			b-=1
			count += 1
		x += 1
'''
def twoStacks(x, stackA, stackB):
	sums = 0
	i = j = count = 0
	while True:
		if sums > x:
			return count 
		if stackA[i] < stackB[j]:
			sums += stackA[i]
			count += 1
			i += 1
		else:
			sums += stackB[j]
			count += 1
			j += 1
	return count

print(twoStacks(10,[4,2,4,6,1],[2,1,8,5]))