'''
Separate the Numbers:
https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''
def separateNumbers(s):
    if s[0]=='0':
        print('NO')
        return
    new_s=''
    l=len(s)
    if l==1:
        print('NO') 
        return
    dig=1
    
    for i in range(l//2):
        val=int(s[:dig])
        while len(new_s)<l and dig<=l//2:
            new_s+=str(val)
            #print(new_s)
            val+=1
        if new_s==s:
            print('YES',new_s[:dig])
            return
        else:
            new_s=''
            dig+=1
    print('NO')
    return
