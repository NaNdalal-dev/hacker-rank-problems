def isEmpty(arr):
	return arr == []
def equalStacks(n1, n2, n3 ,h1, h2, h3):
	new_h1 = []
	new_h2 = []
	new_h3 = []

	vals = 0
	for i in range(n1-1, -1, -1):
		vals+=h1[i]
		new_h1.append(vals)

	vals = 0
	for j in range(n2-1, -1, -1):
		vals+=h2[j]
		new_h2.append(vals)

	vals = 0
	for k in range(n3-1, -1 ,-1):
		vals+=h3[k]
		new_h3.append(vals)

	running = True
	while running:
		if(isEmpty(new_h1) or isEmpty(new_h2) or isEmpty(new_h3)):
			return 0

		s1 = new_h1[-1]
		s2 = new_h2[-1]
		s3 = new_h3[-1]

		if s1 == s2 and s2 == s3:
			return s1

		elif s1 >= s2 and s1 >= s3:
			new_h1.pop()

		elif s2 >= s1 and s2 >= s3:
			new_h2.pop()
		elif s3 >= s1 and s3 >=s1 :
			new_h3.pop()
