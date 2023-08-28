import random 

class RandomTester:
    def __init__(self):
        pass
    
    def printOneRandom(self):
        print(random.random())
    
    def printMultiRandom(self,num):
        for i in range(num):
          self.aleatorio = random.random()
          print(self.aleatorio)
    
    def throwDice(self):
        return random.randint(1,6)
    
    def maxRandom(self,max):
        print(random.randint(1,max))

    def minMaxRandom(self,min,max):
        if min > max:
          print("Erro:valor minimo maior que o valor maximo")
        else:
          print(random.randint(min,max))

    
    
        
        