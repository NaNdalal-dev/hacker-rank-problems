'''
Sherlock and Array:
https://www.hackerrank.com/challenges/sherlock-and-array/problem
'''
def balancedSums(arr):
    sl=0 
    sumarr=sum(arr)
    for i in range(len(arr)):
        if(i!=0):
            sl+=arr[i-1]
        if(2*sl==sumarr-arr[i]):
            return "YES"
    return "NO"
