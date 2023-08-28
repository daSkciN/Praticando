class Professor:
    def __init__(self,nome,matricula,ch):
        self.__nome = nome
        self.__matricula = matricula
        self.__ch = ch

    def getNome(self):
        return self.__nome
    
    def setNome(self,novoNome):
        self.__nome = novoNome

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self,novaMatricula):
        self.__matricula = novaMatricula
      
    def getCh(self):
        return self.__ch
  
    def setCh(self,novoCh):
        self.__ch = novoCh
    
    def maisHoras(self,horasMais):
        self.__ch += horasMais
    
    def menosHoras(self,horasMenos):
        if (self.__ch > horasMenos):
          self.__ch -= horasMenos
        else:
            self.__ch = 0
            
        
        
        