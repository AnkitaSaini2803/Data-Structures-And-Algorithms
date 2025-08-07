#                                   7-8-2025
class Rectangle:
    # def __init__(self):
    #     self.length=int(input())
    #     self.breadth=int(input())

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def getArea(self):
        return self.length*self.breadth
    
rec=Rectangle()
print(rec.getArea())