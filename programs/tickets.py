'''
Link:
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
'''
'''
NOT EXECUTED
'''
def tickets(queue):
	total = 0
	flag = 0
	if queue == [] or queue[0] > 25:
		return'NO'
	for val in queue:
		if val == 25:
			total += val
		elif val == 50:
			total -= 25
			if total < 0:
				return 'NO'
			else:
				total += 25

				
		elif val == 100:
			total -= 75
			if total < 0:
				return 'NO'
			else:
				total += 25
	if total<0:
		return 'NO'
	return 'YES'
print(tickets([25,25,50,25,25,100]))