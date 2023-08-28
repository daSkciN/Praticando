from item import Item

class Cd(Item):
    def __init__(self, titulo, tempreprod, possuo, comentario,artista,numtrilhas):
        super().__init__(titulo, tempreprod, possuo, comentario)
        self.__artista = artista
        self.__numTrilhas = numtrilhas

    def getArtista(self):
        return self.__artista 
    
    def setArtista(self, novoartista):
        self.__artista = novoartista

    def getNumTrilhas(self):
        return self.__numTrilhas
    
    def setNumTrilhas(self, novonumtrilhas):
        self.__numTrilhas = novonumtrilhas
    