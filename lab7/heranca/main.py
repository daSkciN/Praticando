from cd import Cd
from dvd import Dvd
from item import Item

def main():
  catalogoCdeDvd = Item('','','','','')
  catalogoCd = Cd('','','','','')
  catalogoDvd = Dvd('','','','','')
  dvd1 = Dvd('Rambo',120,'Cesar',True,'ggwp')
  cd1 = Cd('Slipknot',30,'John',True,'nada')
  cd2 = Cd('Acdc',50,'Julius',True,'ou')

  print('Lista de Dvds:')
  catalogoDvd.adicionaDVDouCD(dvd1.getTitulo(),dvd1.getTempreprod(),'Jorge')
 

  catalogoDvd.listaDVDeCD()

  print('Lista de Cds:')
  catalogoCd.adicionaDVDouCD(cd1.getTitulo(),cd1.getTempreprod(),'Kleber')


  catalogoCd.adicionaDVDouCD(cd2.getTitulo(),cd2.getTempreprod(),'jojo')

  catalogoCd.listaDVDeCD()

  print(catalogoCd.compareDVDeCD('Acdc'))

  print(catalogoDvd.compareDVDeCD('Acdc'))

  print(catalogoDvd.compareDVDeCD('Rambo'))

  catalogoCd.removeCDeDvd("007")

  catalogoCd.removeCDeDvd("Acdc")

  catalogoCd.listaDVDeCD()















if __name__ == '__main__':
   main()
