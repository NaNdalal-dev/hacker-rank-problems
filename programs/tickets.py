'''
Link:
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
'''

def tickets(queue):
	total = 0
	flag = 0
	if queue == [] or queue[0] > 25:
		return'NO'
	count25 = 0
	count50 = 0
	for val in queue:
		if val == 25:
			count25 += 1
		elif val == 50:
			if count25 >= 1:
				count25 -= 1
				count50 += 1
			else:
				return 'NO'
		elif val == 100:
			if (count25 >= 1 and count50 >= 1):
				count50 -= 1
				count25 -= 1
			elif count25 >=3:
				count25 -=3
			else:
				return 'NO'
	return 'YES'