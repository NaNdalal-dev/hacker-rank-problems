'''
Mars Exploration:
https://www.hackerrank.com/challenges/mars-exploration/problem?h_r=next-challenge&h_v=zen
'''
class marsExploration:
	def __init__(self,msg):
		self.msg=msg
	def wrongMsg(self):
		def Os(self):
			self.wrongOs=0
			self.oindex=1
			self.olen=len(self.msg)//3
			for i in range(self.olen):
				if(self.msg[self.oindex]!='O'):
					self.wrongOs+=1
				self.oindex+=3
			return self.wrongOs
		def Ss(self):
			self.wrongSs=0
			self.sindex=0
			k=0
			self.slen=len(self.msg)-((len(self.msg))//3)
			for i in range(self.slen):
				if(self.msg[self.sindex]!='S'):
					self.wrongSs+=1
				if(k%2==0):
					self.sindex+=2
					k=1
				else:
					self.sindex+=1
					k=2

			return self.wrongSs
		return Ss(self)+Os(self)	
