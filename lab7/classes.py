class DVD:
   def __init__(self,titulo,tempreprod,diretor,possuo,comentario):
       self.__titulo = titulo
       self.__tempreprod = tempreprod
       self.__diretor = diretor
       self.__possuo = False
       self.__comentario = ''
       self.__catalogo = list()


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


   def adicionaDVD(self,titulo,tempreprod,diretor):
       self.__catalogo.append(titulo)


   def listaDVD(self):
       for i in range(len(self.__catalogo)):
           print(self.__catalogo[i])


   def removeDVD(self,titulo):
       if titulo in self.__catalogo:
           self.__catalogo.remove(titulo)
       else:
           print("Esse titulo nao esta no catalogo")
  
   def compareDVD(self,titulo):
       if titulo in self.__catalogo:
           return True
       else:
           return False
          
class CD:
   def __init__(self,titulo,tempreprod,artista,numtrilhas,possuo,comentario):
       self.__titulo = titulo
       self.__tempreprod = tempreprod
       self.__artista = artista
       self.__numtrilhas = numtrilhas
       self.__possuo = False
       self.__comentario = ''
       self.__catalogo = list()


   def getTitulo(self):
       return self.__titulo


   def getTempreprod(self):
       return self.__tempreprod


   def getArtista(self):
       return self.__artista
  
   def getNumtrilhas(self):
       return self.__numtrilhas


   def getPossuo(self):
       return self.__comentario
  
   def setTitulo(self,novoTitulo):
       self.__titulo = novoTitulo


   def setTempreprod(self,novoTempreprod):
       self.__tempreprod = novoTempreprod
  
   def setArtista(self,novoArtista):
       self.__artista = novoArtista
  
   def setNumtrilhas(self,novoNumtrilhas):
       self.__numtrilhas = novoNumtrilhas
  
   def setPossuo(self,novoPossuo):
       self.__possuo = novoPossuo
  
   def setComentario(self,novoComentario):
       self.__comentario = novoComentario

   def adicionaCD(self,titulo,tempreprod,artista):
       self.__catalogo.append(titulo)

   def listaCD(self):
       for i in range(len(self.__catalogo)):
           print(self.__catalogo[i])


   def removeCD(self,artista):
       if artista in self.__catalogo:
           self.__catalogo.remove(artista)
       else:
           print("Esse titulo nao esta no catalogo")


   def compareDVD(self,artista):
       if artista in self.__catalogo:
           return True
       else:
           return False