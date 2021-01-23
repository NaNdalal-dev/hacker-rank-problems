'''
Pangrams:
https://www.hackerrank.com/challenges/pangrams/problem
'''
class binary_search:
	def __init__(self,arr):
		self.arr=arr
	def search(self,val):
		self.val=val
		self.left=0
		self.right=len(self.arr)-1
		while(self.left<=self.right):
			self.mid=(self.left+self.right)//2
			if(self.val==self.arr[self.mid]):
				return True
			elif(self.val>self.arr[self.mid]):
				self.left=self.mid+1
			else:
				self.right=self.mid-1
		return False
	def __repr__(self):
		return 'binary_search({})'.format(self.arr)


def pangrams(s):
	if(' ' in s):
		s.remove(' ')
		
	lower=[chr(i) for i in range(97,123)]
	upper=[chr(i) for i in range(65,91)]
	uc=0
	lc=0
	upper=binary_search(upper)
	lower=binary_search(lower)
	print(s)
	s=list(s)
	for i in s:
		print(i)
		try:
			if(upper.search(i)):
				uc+=1
				s.remove( chr((ord(i)+32)) )
			elif lower.search(i):
				lc+=1
				s.remove( chr(ord(i)-32) )
		except:
			None
	if uc+lc==26:
		return 'pangram'
	else:
		return 'not pangram'
