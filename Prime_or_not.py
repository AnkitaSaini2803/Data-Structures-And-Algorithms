# Find out whether 'n' is prime or not.                     26-08-2025

from math import *
n=int(input('Enter Number: '))
def prim(n):
 if n<2:
   return 'Not Prime'
 for i in range(2,int(sqrt(n))+1):
    if n%i==0:
       return 'Not Prime'
 
 return 'Prime'

print(prim(n))