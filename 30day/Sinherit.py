class Student:
	def __init__(self,fname,lname,uid):
		self.fname=fname
		self.lname=lname
		self.uid=uid
	def details(self):
		print('First Name :',self.fname)
		print('Last Name :',self.lname)
		print('UID:',self.uid)
	def __repr__(self):
		return 'Student({},{},{})'.format(self.fname,self.lname,self.uid)

class StudentInfo(Student):
	def nothing(self):
		return None
