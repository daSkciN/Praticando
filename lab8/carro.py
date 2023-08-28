from veiculo import Veiculo
class Carro(Veiculo):
  
   def __init__(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,numerodeportas):
       super().__init__(placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo)
       self.__numerodeportas = numerodeportas
       
   def getNumeroPortas(self):
       return self.__numerodeportas
   def setNumeroPortas(self,numPortas):                                                             
       self.__numerodeportas = numPortas
   def imprime(self):
       super().imprime()
       print("Numero de Portas:" + str(self.__numerodeportas))