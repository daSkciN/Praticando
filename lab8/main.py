from bicicleta import Bicicleta
from carro import Carro
from moto import Moto


def mainTransporte():
   moto1 = Moto("YUI876", "TOYOTA", 2, "FLEX", 120)
   carro1 = Carro("IJK8867", "Honda", 4, "flex", 4)
   bicicleta1 = Bicicleta("UHY098", "CHERRY", 2, "flex", 5)
   print(moto1.getCilindradas())
   print(carro1.getNumeroPortas())
   print(bicicleta1.getNumeroMarchas())
   moto1.imprime()
   carro1.imprime()
   bicicleta1.imprime()


  




if __name__=="__main__":
   mainTransporte()
