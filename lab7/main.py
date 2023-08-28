from classes import CD
from classes import DVD


def main():
   dvd1 = DVD('rambo',120,'Cesar',True,'ggwp')
   dvd2 = DVD('hitman',150,'John',True,'nada')
   

   dvd1.adicionaDVD(dvd1.getTitulo(),dvd1.getTempreprod(),'Jorge')


   dvd1.listaDVD()


   dvd2.adicionaDVD(dvd2.getTitulo(),120,'Kleber')


   dvd1.listaDVD()

   dvd2.listaDVD()


   dvd1.removeDVD('Gordon')


   dvd1.removeDVD('007')


   dvd1.listaDVD()


  
   print(dvd1.compareDVD('008'))


   print(dvd1.compareDVD('hitman'))














if __name__ == '__main__':
   main()
