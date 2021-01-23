class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		
	def __repr__(self):
		return str(self.data)
		
class LinkedList:

	def __init__(self):
		self.head=None
		
	def Trav(self):
		x=self.head
		while x:
			print(x.data,end=" ")
			x=x.next
			print("->",x)
			
	def front_insert(self,data):
		new_data=Node(data)
		new_data.next=self.head
		self.head=new_data
		
	def last_insert(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return
		last=self.head
		while last.next:
			last=last.next
		last.next=new_node
		return
			
			
	def search(self,val):
		x=self.head		
		while x:
			if(x.data==val):
				print(f"{x.data} found in linked list.")
				break
			x=x.next
		else:
			print(f"{val} not found in linked list.")

a=LinkedList()
a.head=Node(10)
b=Node(20)
c=Node(30)
a.head.next=b
b.next=c
c.next=None

while True:
	print("Menu")
	print("1.Traversal")
	print("2.Search")
	print("3.Insert at front")
	print("4.Insert at last")
	print("5.Exit")
	ch=int(input("Your choice:"))
	if(ch==1):
		print("Single Linked List Traversal:")
		a.Trav()
	elif(ch==2):
		num=int(input("Enter a number to search:"))
		a.search(num)
	elif(ch==3):
		num=int(input("Enter a number:"))
		a.front_insert(num)
	elif(ch==4):
		num=int(input("Enter a number:"))
		a.last_insert(num)
	elif(ch==5):
		print("Bye")
		break
	else:
		print("Invalid option.")
	print()
