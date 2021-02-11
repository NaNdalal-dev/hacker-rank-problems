

def countNonEmptySubstr(str): 
	n = len(str); 
	return n * (n + 1) // 2 

# driver code 
s = "abcde"; 
print (countNonEmptySubstr(s)); 