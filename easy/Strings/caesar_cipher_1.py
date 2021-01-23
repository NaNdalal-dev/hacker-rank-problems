'''
caesar-cipher-1:
https://www.hackerrank.com/challenges/caesar-cipher-1/problem
'''
class Caesar_cipher:
	def __init__(self,msg,k):
		self.msg=msg
		self.k=k
	def encrypt(self):
		self.enc=''
		for self.i in self.msg:
			if(self.i.islower()):
				forward=((ord(self.i)+self.k)-97)%26
				self.enc+=chr(forward+97)

						
			elif(self.i.isupper()):
				forward=((ord(self.i)+self.k)-65)%26
				self.enc+=chr(forward+65)
			

			else:
				self.enc+=self.i				
			
		return self.enc
	def decrypt(self):
		self.dec=''
		for self.i in self.enc:
			if(self.i.islower()):
				backward=((ord(self.i)-self.k)-97)%26
				self.dec+=chr(backward+97)

						
			elif(self.i.isupper()):
				backward=((ord(self.i)-self.k)-65)%26
				self.dec+=chr(backward+65)
			

			else:
				self.dec+=self.i
		return self.dec
	def __repr__(self):
		return 'Caesar_cipher({},{})'.format(self.msg,self.k)
