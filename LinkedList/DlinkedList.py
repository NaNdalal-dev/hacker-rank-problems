class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
	def __repr__(self):
		return repr(self.data)

class DoubleLlist:
	def __init__(self):
		self.head=None
	
	def Trav(self):
		print("Doubly Linked List Traversal:")
		x=self.head
		while x:
			print(x.prev,"<-    ",end=" ")
			print(x.data,end=" ")
			x=x.next
			print("   ->",x)
	def search(self,val):
		x=self.head		
		while x:
			if(x.data==val):
				print(f"{x.data} found in Doubly linked list.")
				break
			x=x.next
		else:
			print(f"{val} not found in Doubly linked list.")

a=DoubleLlist()
a.head=Node(10)
b=Node(20)
c=Node(30)

a.head.next=b
b.next=c
c.next=None

a.head.prev=None
b.prev=a.head
c.prev=b

while True:
	print("Menu")
	print("1.Traversal")
	print("2.Search")
	print("3.Exit")
	ch=int(input("Your choice:"))
	if(ch==1):
		
		a.Trav()
	elif(ch==2):
		num=int(input("Enter a number to search:"))
		a.search(num)
	elif(ch==3):
		print("Bye")
		break
	else:
		print("Invalid option.")
	print()
