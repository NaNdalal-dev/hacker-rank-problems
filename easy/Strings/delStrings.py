class MyStr:
	
    def __init__(self,st):
            self.st=st
    def __repr__(self):
            return str(self.st)
    def __delitem__(self,index):
            self.list_st=[]
            for i in self.st:
            	self.list_st.append(i)
            del self.list_st[index]
            self.st=''
            for j in self.list_st:
            	 self.st+=j
            return  self.st
    def __getitem__(self,index):
    	return self.st[index]

