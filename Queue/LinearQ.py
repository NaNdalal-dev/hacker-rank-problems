class LinearQueue:
	def __init__(self,size):
		self.size=size
		self.front=self.rear=-1
		self.QArray=[None for i in range(self.size)]
	
	def Enqueue(self,val):
		if self.front==-1 and self.rear==-1:
			self.front=0
			self.rear=0
			self.QArray[self.rear]=val
		else:
			self.rear+=1
			if self.rear>self.size-1:
				raise IndexError("Error! Queue Overflow")
			self.QArray[self.rear]=val
	
	def Dequeue(self):
		if self.front==-1 and self.rear==-1:
			raise IndexError("Error! Queue Underflow")
		elif self.front==self.rear:
			x=self.QArray[self.front]
			self.QArray[self.front]=None
			self.front=-1
			self.rear=-1
			return x
		else:
			x=self.QArray[self.front]
			self.QArray[self.front]=None
			self.front+=1
			return x
	def top(self):
		if(self.front==-1 and self.rear==-1):
			raise IndexError("Error! Queue Underflow")
		return self.QArray[self.rear]
	
	def isEmpty(self):
		if(self.front==-1 and self.rear==-1):
			return True
		return False
	
	def traversal(self):
		if(self.front==-1 and self.rear==-1):
			raise IndexError("Error! Queue Underflow")
			return 
		print("Elements in Queue:")
		for i in range(self.front,self.rear+1):
			print(self.QArray[i],end=" ")
		print()
		return 
	def __repr__(self):
		return f"LinearQueue({self.QArray})"

if __name__=="__main__":
	if 1:
		q=LinearQueue(5)
		q.Enqueue(10)
		q.Enqueue(20)
		q.Enqueue(30)
		q.Enqueue(40)
		q.Enqueue(50)
		#q.Enqueue(50)
		q.traversal()
	#except IndexError as ie:
	#	print(ie)
