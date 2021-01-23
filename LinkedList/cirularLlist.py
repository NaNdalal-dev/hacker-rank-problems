class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
	def __repr__(self):
		return repr(self.data)

class CircularList:
	def __init__(self):
		self.head=None	
	def Trav(self):
		x=self.head
		first=self.head
		while x:
			print(x.data,end=" ")
			x=x.next
			print("->",x)
			if(x==first):
				break
			
	def search(self,val):
		x=self.head
		first=self.head
		while x:
			if(x.data==val):
				return 1
			x=x.next
			if(x==first):
				break
		return 0
			
		
	def __repr__(self):
		return repr(self.head)

a=CircularList()
a.head=Node(10)
b=Node(20)
c=Node(30)
a.head.next=b
b.next=c
c.next=a.head
while True:
	print("Menu")
	print("1.Traversal")
	print("2.Search")
	print("3.Exit")
	ch=int(input("Your choice:"))
	if(ch==1):
		print("Circular Linked List Traversal:")
		a.Trav()
	elif(ch==2):
		num=int(input("Enter a number to search:"))
		if(a.search(num)):
			print(f"{num} found in circular linked list.")
		else:
			print(f"{num} not found in circular linked list.")
		
	elif(ch==3):
		print("Bye")
		break
	else:
		print("Invalid option.")
	print()
