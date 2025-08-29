'''Fibonacci sequence using matrix Exponentiation                   29-08-2025'''
# Time Complexity - O(log(n))

n=int(input('Enter Fibonacci Number: '))
MOD=10**9+7
def fib(n):
    if n<0:
        raise 'ValueError'
    elif n<=1:
        return n
    M=[[1,1],[1,0]]
    result=matrix_exp(M,n-1)
    return  result[0][0] % MOD                         #result
    
def multiply(m1,m2):
    res=[[0,0],[0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j]=(res[i][j]+m1[i][k]*m2[k][j]) % MOD
    return res

def matrix_exp(M,b):
    if b==0:
        return [[1,0],[0,1]]       #Identity Matrix
    elif b==1:
        return M
    half=matrix_exp(M,b//2)
    half_sqr=multiply(half,half)
    if b%2==0:
        return half_sqr
    else:
        return multiply(M,half_sqr)
    
print(fib(n))
