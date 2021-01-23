class binary_search:
	def __init__(self,arr):
		self.arr=sorted(arr)
	def search(self,val):
		self.val=val
		self.left=0
		self.right=len(self.arr)-1
		while(self.left<=self.right):
			self.mid=(self.left+self.right)//2
			if(self.val==self.arr[self.mid]):
				return self.mid
			elif(self.val>self.arr[self.mid]):
				self.left=self.mid+1
			else:
				self.right=self.mid-1
		return 0
	def __repr__(self):
		return 'binary_search({})'.format(self.arr)
