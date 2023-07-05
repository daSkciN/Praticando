class Aluno:
    ano_atual = 2023
    def __init__(self,matricula,nome,idade,curso, creditos):
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso
        self.__creditos = creditos

#Propriedades e getters
    @property
    def matricula(self):
        return self.__matricula
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def curso(self):
        return self.__curso
    @property
    def creditos(self):
        return self.__creditos
    
    def setCreditos(self,creditos):
        self.__creditos = creditos

    def addCreditos(self,creditos):
        self.__creditos += creditos
    
        
    def get_ano_nascimento(self):
        return (self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls,matricula,nome,curso,ano_nascimento,creditos):
        idade = cls.ano_atual - ano_nascimento
        return cls(matricula,nome,ano_nascimento,curso,creditos)



