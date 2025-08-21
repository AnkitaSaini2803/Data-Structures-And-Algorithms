#                                                  21-08-2025
n=input('Enter String: ')             #here string indxes are string only
#and in need to access the indexelement of str->they must ne int
sum_even=0
sum_odd=0
for i in range(len(n)):
    if int(n[i])%2==0:
        sum_even+=int(n[i])
    else:
        sum_odd+=int(n[i])
print(sum_even)
print(sum_odd)


print(n[0],type(n[0]))
print(n[1],type(n[1]))
