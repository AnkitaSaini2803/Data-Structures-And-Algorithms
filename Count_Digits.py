'''                                                    26-08-2025
Input: ‘n’ = 336  Output: 3
Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted
two time
'''                                                
n=int(input())
count=[]
for i in str(n):
    if int(i)!=0  and n % int(i)==0:
       count.append(int(i)) #or count.append(i)

print(len(count))

        