'''
Link:
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
'''
def zeros(n):
	if n <= 100:
		return (n//5) + (n//25)
print(zeros(100))