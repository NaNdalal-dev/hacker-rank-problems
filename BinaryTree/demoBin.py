class ConstructBinaryTree:
	
	def __init__(self,size):
		self.size=size
		self.tree=[None for i in range(self.size)]
		self.current=0
	
	def put(self,element):
		if self.current<self.size:
			self.tree[self.current]=element
			self.current+=1
		else:
			self.current=self.size
			raise IndexError('Tree size out of range.')
	
	def increaseSize(self,val):
		if val>=0:
			self.current-=1
			self.size+=val
			self.tree+=[None for i in range(val)]
		else:
			return IndexError('Cannot decrease the fixed size')
	
	def get_children(self,value,index=None):
		if value not in self.tree:
			raise ValueError(f"{value} is not in Tree")
		elif index is None:
			val=self.tree.index(value)*2
			if val+1 >= self.size:
				left=None
			else:
				left = self.tree[val+1]
			
			if val+2>=self.size:
				right = None
			else:
				right = self.tree[val+2]
			
			return left,right
			
		elif index is not None:
			if self.tree[index]== value:
				val=index*2
				if val+1 >= self.size:
					left = None
				else:
					left = self.tree[val+1]
					
				if val+2 >= self.size:
					right = None
				else:
					right = self.tree[val+2]
				return left,right
			
				
			else:
				raise IndexError(f'ConstructBinary[{index}]={self.tree[index]} not {value}.Hence index and value are mismatched')
			
		else:
			raise IndexError('Tree Index out of range')
			
	def allClear(self):
		self.size+=val
		self.tree+=[None for i in range(self.size)]
		return
	
	def __len__(self):
		return len(self.tree)
		
	def __getitem__(self,index):
		if index<self.size:
			return self.tree[index]
		else:
			raise IndexError('Tree Index out of range')
	
	def __delitem__(self,index):
		if index>=self.size:
			raise IndexError(f'Tree Index[{index}] out of range')
		else:
			del self.tree[index]
	
	def __repr__(self):
		return f'ConstructBinary({self.tree})'

if __name__ == '__main__':
	#Initialise ConstructBinaryTree
	tree = ConstructBinaryTree(7) #size = 7
	print(f'size of tree:{tree.size}')
	#inserting 7 values
	tree.put(0)
	tree.put(1)
	tree.put(2)
	tree.put(3)
	tree.put('hello')
	tree.put(5)
	tree.put(6)
	#Display content
	print('#Display content')
	print(tree)
	#Accessing children elements without index
	print('children of 1')
	print(tree.get_children(1))
	
	#Accessing children elements with index
	print('children of 2')
	print(tree.get_children(2,index=2))
	
	#delete item
	del tree[2]
	print('deleted 2nd index of tree')
	print(tree)
	
	#increasing the size of tree by three
	tree.increaseSize(3)
	print('increasing the size of tree by three')
	print('new tree',tree)
	#Inserting new values
	tree.put(19)
	tree.put(20)
	tree.put(21)
	print(tree,'Inserted 3 new values')
	
