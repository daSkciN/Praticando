class Alunos():  
    def __init__(self,matricula):
        self.matricula = matricula
        print('Objeto criado')
        print('Sua matricula é:', self.matricula)
    def get___nome(self,__nome):
        self.__nome = __nome
        print('Seu __nome é:', self.__nome)
   



matricula1 = int(input('Digite a matricula do aluno:'))
aluno1 = Alunos(matricula1)
__nome1 = input('Digite o __nome do aluno:')
aluno1.get___nome(__nome1)


