from matematica.calculos import *
from time import sleep

def encerramento():
  linha()
  print("Muito Obrigado por utilizar nosso sistema!!!")
  linha()

def linha():
  
  print("~" * 40)

def menuPrincipal():
    
  linha()
  print ("Sistema de Calculadora".center(40))
  linha()

def menuOpcoes():

  linha()
  print("1 - Operações Básicas")
  print("2 - Fatorial")
  print("3 - Média")
  print("0 - Sair")
  linha()

  opçao = input("Escolha uma opção: ").strip()
  return opçao


def menuFatorial():
  
  linha()
  print("Calculando um Fatorial".center(40))
  linha()

def menuMedia():
  linha()
  print("Cálculo de Média".center(40))
  linha()

def InterfaceCalculos(a, b, c, d):

   
  if d == None:

    print("Erro: divisão por 0")
   
  else:
   
    print(f" {a} {c} {b} = {d} ")

def interfaceOperações():

  try:

      a = float (input("Digite o 1° valor: "))
      sleep(0.5)

      b = float (input("Digite o 2° valor: "))
      sleep(0.5)

      InterfaceCalculos(a, b, "+", soma(a,b))
      InterfaceCalculos(a, b, "-", sub (a, b))
      InterfaceCalculos(a, b, "*", multi (a, b))
      InterfaceCalculos(a, b, "/", div(a, b))
  
  except ValueError:
    print(" ERRO: Digite apenas números")

def InterfaceFatorail():

  c = int(input("Digite um valor: "))
  sleep(0.5)

  print(f"O fatorial do valor {c} será: ", end=" ")
  print(fatorial(c))
  sleep(1)


def interfaceMedia():

  valores = []

  while True:

    print("* Para parar escreva N *")
    numeros = input("Digite um número: ").strip().upper()

    if numeros == "N":
      break

    try: 
      valores.append(float(numeros))
    
    except ValueError:
      print("ERRO: Digite um número válido")

  if valores:
    print(f"A media dos valores será:{media(valores):.2f}")
  
  else:
    print()