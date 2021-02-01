'''
Link:
https://www.hackerrank.com/challenges/qheap1/problem
'''
class MinHeap:
	def __init__(self):
		self.i = -1
		self.heap_arr = []
	def push(self,val):
		if val not in self.heap_arr:
			self.heap_arr.append(val)
			self.i += 1
			index = self.i
			while index>0:
				current = index
				
				if index%2 == 0:
					parent = (index // 2) -1 #Parent For Right Child
				else:
					parent = index // 2  #Parent For Left Child
				
				if self.heap_arr[current] < self.heap_arr[parent]:  #swap if current element < Parent element
					self.heap_arr[current], self.heap_arr[parent] = self.heap_arr[parent], self.heap_arr[current]

				index = parent #Modifying Index Value
		self.min = self.heap_arr[0]
		return self.heap_arr
		
	


	
#vals = list(range(6,-1,-1))
'''vals = [10,20,15,30,40]
mh = MinHeap()
for val in vals:
	print(mh.push(val))'''

