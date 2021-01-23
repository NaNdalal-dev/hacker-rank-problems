'''
Link for description:
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
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
				return 1
			elif(self.val>self.arr[self.mid]):
				self.left=self.mid+1
			else:
				self.right=self.mid-1
		return 0
	def __repr__(self):
		return 'binary_search({})'.format(self.arr)
n=int(input())
name_ph={}
for i in range(n):
	name,phno=input().split()
	phno=int(phno)
	name_ph.update({name:phno})
keys=binary_search(list(name_ph.keys()))
result=[]

for j in range(n):
	name=input()
	if(keys.search(name)==0):
		result.append('Not found')
	else:
		result.append('{}={}'.format(name,name_ph.get(name)))
for i in result:
	print(i)
