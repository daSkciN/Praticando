class Item:
  def __init__(self,titulo,tempreprod,possuo,comentario):
    self.__titulo = titulo
    self.__tempreprod = tempreprod
    self.__possuo = possuo
    self.__comentario = comentario
  
  def getTitulo(self):
       return self.__titulo

  def getTempreprod(self):
       return self.__tempreprod

  def getDiretor(self):
       return self.__diretor

  def getPossuo(self):
       return self.__possuo
  
  def getComentario(self):
       return self.__comentario
  
  def setTitulo(self,novoTitulo):
       self.__titulo = novoTitulo

  def setTempreprod(self,novoTempreprod):
       self.__tempreprod = novoTempreprod
  
  def setArtista(self,novoDiretor):
       self.__diretor = novoDiretor
  
  def setPossuo(self,novoPossuo):
       self.__possuo = novoPossuo
  
  def setComentario(self,novoComentario):
       self.__comentario = novoComentario

  