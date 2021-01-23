class Stack:
	def __init__(self,size):
		self.size=size
		self.bucket=[None for i in range(self.size)]
		self.i=0
	def push(self,val):
		if(self.i<self.size):
			self.val=val
			self.bucket[self.i]=self.val
			self.i+=1
			return self.bucket
		else:
			return 'Stack is Full!'
	def pop(self):
		if(self.i>0):
			print(self.bucket[self.i-1])
			self.bucket[self.i-1]=None
			self.i-=1
		else:
			return 'Stack is Empty.'	
	def Top(self):
		return self.bucket[self.i]
	def isEmpty(self):
		if(self.i==0):
			return True
		else:
			return False
	def isFull(self):
		if(self.i==self.size):
			return True
		else:
			return False	
	def __repr__(self):
		return repr('Stack({})'.format(self.bucket))
