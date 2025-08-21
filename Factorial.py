#                                     21-08-2025
n=int(input())
fact=1
if n==0 or n==1:
        print(1) 
elif n<0:
        print('Error')
else:
    for i in range(n):
      fact*=n
      n=n-1
    print(fact)



# Through Recursion
# def factorial(n):
#         if n<0:
#                 return 'Error'
#         elif n==0 or n==1:
#                 return 1
#         else:
#                 return n*factorial(n-1)
# print(factorial(n))




















