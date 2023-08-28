from classes import RandomTester
import random

def main():
  aleatorio = RandomTester()
  aleatorio.printOneRandom()

  aleatorio.printMultiRandom(int(input("Digite a quantidade de numeros aleatorios:")))

  print(aleatorio.throwDice())

  aleatorio.maxRandom(int(input("Digite o limite do numero aleatorio:")))

  aleatorio.minMaxRandom(int(input("Digite o menor valor do numero aleatorio:")),int(input("Digite o maior valor do numero aleatorio:")))


if __name__ == '__main__':
  main()
