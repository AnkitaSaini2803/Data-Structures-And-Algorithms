'''Binary Exponentiation/Fast Exponentiation With Recursion         28-08-2025'''

a=int(input('Enter:'))
b=int(input('Enter:'))
def exponentiation(a,b):
    if b==0:
        return 1
    half=exponentiation(a,b//2)
    if b%2==0:
        return half*half
    else:
        return a*half*half
print(exponentiation(a,b))














'''this is not a binary exponentiation code neither an iterative approach '''
# base=int(input('Enter:'))
# exp=int(input('Enter:'))
# def exponent(base,exp):
#     if exp==0:
#         return 1
#     half=exp//2
#     ans=base**half
#     if exp%2==0:
#         return ans*ans
#     else:
#         return base*ans*ans
# print(exponent(base,exp))








# base=int(input('Enter Base: '))
# exp=int(input('Enter exponent : '))
# def exponentiation(base,exp):
#     if exp==0:
#         return 1
#     half=exponentiation(base,exp//2)
#     if exp%2==0:
#         return half*half
#     else:
#         return base*half*half

# print(exponentiation(base,exp))
