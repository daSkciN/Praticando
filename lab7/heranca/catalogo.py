from item import Item

class Catalogo:
  def __init__(self):
    self.__catalogo = list()

  def adicionaDVDouCD(self,item):
    self.__catalogo.append(item)
  
  def listaDVDeCD(self):
    ordem = {"Cd": 1, "Dvd": 2}
    for index in range(1, 3):
      for item in self.__catalogo:
        if ordem[item.__class__.__name__] == index:
          print(item.getTitulo())

  def compareDVDeCD(self,titulo):
      for item in self.__catalogo:
            if item.getTitulo() == titulo:
              return True
      return False
      
  def removeCDeDvd(self,titulo):
    for item in self.__catalogo:
      if item.getTitulo() == titulo:
        if item:
          self.__catalogo.remove(item)
          break
    else:
      print("Esse titulo nao esta no catalogo")