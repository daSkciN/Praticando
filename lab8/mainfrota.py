from veiculo import Veiculo
from carro import Carro
from frota import Frota
from moto import Moto
from bicicleta import Bicicleta

def mainFrota():
   
  frota = Frota()
  moto1 = Moto("YUI876", "TOYOTA", 2, "FLEX", 120)
  carro1 = Carro("IJK8867", "Honda", 4, "flex", 4)
  bicicleta1 = Bicicleta("UHY098", "CHERRY", 2, "flex", 5)
  carro2 = Carro("JFD3425", "BMW", 4, "flex", 4)

  frota.inserir_veiculo(carro1)
  frota.inserir_veiculo(moto1)
  frota.inserir_veiculo(bicicleta1)
  frota.inserir_veiculo(carro2)

  print("Busca de veiculo:")
  print(frota.buscar_veiculo("YUI876"))


  print("Lista de Veículos:")
  frota.listar_veiculos()

  frota.remover_veiculo("YUI876")

  frota.listar_veiculos()


if __name__=="__main__":
   mainFrota()