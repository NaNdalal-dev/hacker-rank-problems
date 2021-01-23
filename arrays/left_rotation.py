def left_rotation(d,arr,n):

	new_arr = []
	for i in range(0,n):
		val = arr[(i+d)%n]
		new_arr.append(val)

	return new_arr