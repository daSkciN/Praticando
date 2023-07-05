from tkinter import *

class NumberDisplay:
  
    
    def __init__(self,limite,horario):
        self.__limite = limite
        self.__value = horario

    def increment(self):
        self.__value = (self.__value+1) % self.__limite
    def getValue(self):
        return self.__value
    
    def getDisplayValue(self):
        if (self.__value < 10):
            return "0" + str(self.__value)
        else:
            return "" + str(self.__value)

class ClockDisplay:

    def __init__(self,hora,minuto):
        self.__hour = NumberDisplay(24,hora)
        self.__minutes = NumberDisplay(60,minuto) 
            
    
    def timeTick(self):
        while True:
                Tk().after(60000,self.__updateDisplay())
                self.__minutes.increment()
                if (self.__minutes.getValue() == 0):
                    self.__hour.increment()
                

    def __updateDisplay(self):
        self.__displayString = self.__hour.getDisplayValue() + ":" + self.__minutes.getDisplayValue()
        print(self.__displayString)
        