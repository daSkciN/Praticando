from item import Item

class Dvd(Item):
    def __init__(self, titulo, tempreprod, possuo, comentario,diretor):
        super().__init__(titulo, tempreprod, possuo, comentario)
        self.__diretor = diretor

    def getDiretor(self):
        return self.__diretor
    
    def setDiretor(self, novodiretor):
        self.__diretor = novodiretor

    