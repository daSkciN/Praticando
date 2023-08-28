from veiculo import Veiculo


class Moto(Veiculo):
   def __init__(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,cilindradas):
       super().__init__(placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo)
       self.__cilindradas = cilindradas
   def getCilindradas(self):
       return self.__cilindradas
   def setCilindradas(self,numPortas):
       self.__cilindradas = numPortas
   def imprime(self):
       super().imprime()
       print("Cilindradas:" + str(self.__cilindradas))
