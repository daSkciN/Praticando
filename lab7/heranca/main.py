from cd import Cd
from dvd import Dvd
from item import Item
from catalogo import Catalogo

def main():

  catalogo = Catalogo()
  dvd1 = Dvd('Rambo',120,True,'ggwp','Dante')
  cd1 = Cd('Phamo',30,True,'nada','Slipknot',5)
  cd2 = Cd('Tramoia',50,True,'ou','Acdc',8)

  print('Lista de Dvds e Cds:')
  catalogo.adicionaDVDouCD(dvd1)

  catalogo.adicionaDVDouCD(cd1)

  catalogo.adicionaDVDouCD(cd2)

  catalogo.listaDVDeCD()

  print(catalogo.compareDVDeCD('Acdc'))

  print(catalogo.compareDVDeCD('Tramoia'))

  print(catalogo.compareDVDeCD('Rambo'))

  catalogo.removeCDeDvd("Rambo")

  catalogo.removeCDeDvd("Acdc")

  catalogo.listaDVDeCD()















if __name__ == '__main__':
   main()
