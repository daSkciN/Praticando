
class ProfessorUFS:
    def __init__(self,nome,matricula,ch):
        self.__nome = nome
        self.__matricula = matricula
        self.__ch = ch
        self.__chmin = 8
        self.__chmax = 20

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
      if(novoCh>=self.__chmin and novoCh<=self.__chmax):
        self.__ch = novoCh
      else:
          print("Carga horaria nao aceita")
    
    def getChMin(self):
        return self.__chmin
    
    def setChMin(self,novaChMin):
        self.__chmin = novaChMin

    def getChMax(self):
        return self.__chmax
    
    def getChMin(self,novaChMax):
        self.__chmax = novaChMax
    
    def maisHoras(self,horasMais):
        self.__ch += horasMais
        if(self.__ch>self.__chmax):
            self.__ch -= horasMais
            print("Carga horaria ultrapasssou a maxima")
            
    
    def menosHoras(self,horasMenos):
        self.__ch -= horasMenos
        if(self.__ch<self.__chmin):
            self.__ch += horasMenos
            print("Carga horaria menor que a minima")
        
        
    