class RevArray:
	def __init__(self,arr):
		self.arr=arr
	def reverse(self):
		self.r_arr=[]
		for i in range(len(self.arr)-1,-1,-1):
			self.r_arr.append(self.arr[i])
		#return self.r_arr
		for k in self.r_arr:
			print(k,end=' ')
		print()
