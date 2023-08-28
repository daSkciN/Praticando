class Veiculo:
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo):
       self.__placaVeiculo = placaveiculo
       self.__fabricanteVeiculo = fabricanteveiculo
       self.__numeroRodas = numerorodas
       self.__tipoVeiculo = tipoveiculo
      

    def imprime(self):
       print("Placa do veiculo: " + self.__placaVeiculo + "\nFabricante do veiculo: " + self.__fabricanteVeiculo + "\nNumero de rodas: " + str(self.__numeroRodas) + "\nTipo de veiculo " + self.__tipoVeiculo)
  
    def getFabricanteVeiculo(self):
       return self.__fabricanteVeiculo


    def setFabricanteVeiculo(self, fabricanteveiculo):
       if len(fabricanteveiculo) == 0:
           print ("Fabricante de veiculo vazio")
       else:
           self.__fabricanteVeiculo = fabricanteveiculo


    def getPlacaVeiculo(self):
       return self.__placaVeiculo


    def setPlacaVeiculo(self, placaveiculo):
       if len(placaveiculo) == 0:
           print ("Placa de veiculo vazio")
       else:
           self.__placaVeiculo = placaveiculo


    def getNumeroRodas(self):
       return self.__numeroRodas


    def setNumeroRodas(self, numerorodas):
       if numerorodas <= 0:
           print ("Numero de rodas invalido")
       else:
           self.__numeroRodas = numerorodas


    def getTipoVeiculo(self):
       return self.__tipoVeiculo


    def setTipoVeiculo(self, tipoveiculo):
       if len(tipoveiculo) == 0:
           print ("Tipo de veiculo vazio")
       else:
           self.__tipoVeiculo = tipoveiculo

    def adicionaVeiculo(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo):
        self.__frota.append(placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo)


