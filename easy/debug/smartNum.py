'''
Smart Number:
https://www.hackerrank.com/challenges/smart-number/problem
'''
'''
Given:

import math
def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == 1:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
'''
import math
def is_smart_number(num):
	if num==1:
		return True
	count=0
	val = int(math.sqrt(num))
	for i in range(1,val+1):
		print('i',i,'val',val)
		if(num%i==0):
			count+=1
	return count
