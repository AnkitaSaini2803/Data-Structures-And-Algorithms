noOfGear=int(input())
color=input()
maxSpeed=int(input())
class Car:
    def __init__(self,noOfGear,color):
        self.noOfGear=noOfGear
        self.color=color   
        
    def printCarInfo(self):
        print(f"noOfGear:{self.noOfGear}")
        print(f"color:{self.color}")

class RaceCar(Car):
    def __init__(self,noOfGear,color,maxSpeed):
        self.maxSpeed=maxSpeed
        super().__init__(noOfGear,color)

    def RaceCarInfo(self):
        super().printCarInfo()
        print(f"maxSpeed: {self.maxSpeed}")

obj=RaceCar(noOfGear,color,maxSpeed)
obj.RaceCarInfo()