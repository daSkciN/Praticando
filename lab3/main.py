from professor import Professor

def main():
   
  professor1 = Professor(input("Digite o nome:"),input("Digite a matricula:"),int(input("Digite a carga horaria:")))

  print(professor1.getNome())
  print(professor1.getMatricula())
  print(professor1.getCh())

  mudaNome = professor1.setNome(input("Digite o novo nome:"))
  mudaMatricula = professor1.setMatricula(input("Digite a nova matricula:"))
  mudaCh = professor1.setCh(int(input("Digite a nova carga horaria:")))

  print(professor1.getNome())
  print(professor1.getMatricula())
  print(professor1.getCh())

  aumentaHoras = professor1.maisHoras(int(input("Digite as horas que quer adicionar:")))
  print(professor1.getCh())
  diminuiHoras = professor1.menosHoras(int(input("Digite as horas que quer diminuir:")))
  

  print(professor1.getNome())
  print(professor1.getMatricula())
  print(professor1.getCh())
 





if __name__ == '__main__':
   main()