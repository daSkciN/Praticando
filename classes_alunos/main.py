from classes_alunos import Aluno

#aluno 1
aluno1 = Aluno(2023001,'Pedro',22,'Engenharia civil',0)
aluno1.addCreditos(int(input('Digite quantos creditos quer adicionar:')))
print(f'\nA matricula do aluno 1 é: {aluno1.matricula}')
print(f'O nome do aluno 1 é: {aluno1.nome}')
print(f'A idade do aluno 1 é: {aluno1.idade}')
print(f'O curso do aluno 1 é: {aluno1.curso}')
print(f'O ano de nascimento do aluno 1 é: {aluno1.get_ano_nascimento()}')
print(f'A quantidade de creditos do aluno 1 é: {aluno1.creditos}')



#aluno 2

aluno2 = Aluno.por_ano_nascimento(2023002,'Carla','Quimica',1999,0)

print(f'\nA matricula do aluno 2 é: {aluno2.matricula}')
print(f'O nome do aluno 2 é: {aluno2.nome}')
print(f'A idade do aluno 2 é: {aluno2.idade}')
print(f'O curso do aluno 2 é: {aluno2.curso}')
print(f'O ano de nascimento do aluno 2 é: {aluno2.get_ano_nascimento()}')
print(f'A quantidade de creditos do aluno 1 é: {aluno2.creditos}')