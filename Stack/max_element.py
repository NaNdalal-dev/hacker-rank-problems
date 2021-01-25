'''
Link:
https://www.hackerrank.com/challenges/maximum-element/problem
'''

class Stack:
	def __init__(self):
		self.arr = []
		self.least = -2147483648
		self.max_stk = [self.least]
	def push(self,val):
		self.arr.append(val)
		self.top = self.max_stk[-1]
		if self.top < val:
			self.top = val
			self.max_stk.append(val)
		else:
			self.max_stk.append(self.top)
	def pop(self):
		self.arr.pop()
		self.max_stk.pop()
		
	def get_max(self):
		return self.max_stk[-1]

		
n = int(input())
stk = Stack()
while n:
	query = input().split(' ')

	qt = int(query[0])

	if(len(query) == 2):
		val = int(query[1])

	if qt == 1:
		stk.push(val)
	elif qt == 2:
		stk.pop()
	elif qt == 3:
		print(stk.get_max())
	n-=1
