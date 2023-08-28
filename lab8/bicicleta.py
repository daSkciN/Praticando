from veiculo import Veiculo


class Bicicleta(Veiculo):
   def __init__(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,nummarchas):
       super().__init__(placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo)
       self.__numMarchas = nummarchas
   def getNumeroMarchas(self):
       return self.__numMarchas
   def setNumeroMarchas(self,nummarchas):
       self.__numMarchas = nummarchas
   def imprime(self):
       super().imprime()
       print("Numero de marchas:" + str(self.__numMarchas))
