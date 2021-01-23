'''def diagonalX():
    # Write your code here
    d1=0
    d2=0
    for i in range(5):
        for j in range(5):
            if(i==j):
            	print('*',end=' ')
            elif(i+j==4):
            	print('*',end=' ')
            else:
            	print(' ',end=' ')
        print()'''
              
def diagonalDifference(arr):
    # Write your code here
    d1=[]
    d2=[]
    x=0
    y=len(arr)-1
    for i in arr:
        d1.append(i[x])
        d2.append(i[y])
        x+=1
        y-=1
    d1=sum(d1)
    d2=sum(d2)
    return abs(d1-d2)
      
r=diagonalDifference([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(r)
