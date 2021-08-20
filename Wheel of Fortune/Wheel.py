from random import randint
class Wheel:
    @staticmethod
    def makeWheel(specialamt):
        specialList=[]
        wheel=['Free Play',700,'Lose A Turn',800,500,650,500,900,'Bankrupt',5000,500,600,700,600,650,500,700,500,600,550,500,600,'Bankrupt',650]
        if specialamt==None:
            return wheel
        else:
            for i in specialamt:
                wheel[randint(0,len(wheel)-1)]=specialList[randint(0,len(specialList)-1)]

    @staticmethod
    def spin(wheel):
        return wheel[randint(0,len(wheel)-1)]