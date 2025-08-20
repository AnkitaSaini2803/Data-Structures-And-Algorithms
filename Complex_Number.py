# Asked in MICROSOFT                                          18-08-2025
import math
a,b=map(int,input('Enter Value: ').split())
c,d=map(int,input('Enter Value: ').split())
ch=int(input('Enter Value: '))

class complex_Number:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def addition(self):
          c1=self.a+self.c
          c2=self.b+self.d
          # return f'{c1} + i{c2}'
          # return c1
          return str(c1) + " + i" + str(c2)

    def multiply(self):
          c1=(self.a * self.c)-(self.b * self.d)
          c2=(self.a * self.d)+(self.c * self.b)
          # return f'{c1} + i{c2}'
          return str(c1) + " + i" + str(c2)
     
     
    
cob=complex_Number(a,b,c,d)
if ch==1:
          print(cob.addition())
elif ch==2:
          print(cob.multiply())


#it was not accepting match case so it was required to change with if-elif


'''             Using Built-in Complex                             STOP           
import math
a,b=map(int,input('Enter Value: ').split())
c,d=map(int,input('Enter Value: ').split())
ch=int(input('Enter Value: '))

class complex_Number:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
  # match ch:
    #    case 1:
    def addition(self):
          c1=complex(a,b)
          c2=complex(c,d)
          c1=c1+c2
          return c1

    def multiply(self):
         c1=complex(a,b)
         c2=complex(c,d)
         c1=c1*c2
         return c1

         
cob=complex_Number(a,b,c,d)
match ch:
     case 1:
          print(cob.addition())
     case 2:
          print(cob.multiply())


'''