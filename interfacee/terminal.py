from matematica.calculos import *
from time import sleep

def encerramento():
  linha()
  print("Muito Obrigado por Utilizar Nosso Sistema!!!")
  linha()

def linha():
  
  print("~" * 40)

def menuPrincipal():
    
  linha()
  print ("Sistema de Calculadora".center(40))
  linha()

def menuFatorial():
  
  linha()
  print("Calculando um Fatorial".center(40))
  linha()

def menuMedia():
  linha()
  print("Cálculo de Média")
  linha()

def InterfaceCalculos(a, b, c, d):

   
  if d == None:

    print("Erro: divisão por 0")
   
  else:
   
    print(f" {a} {c} {b} = {d} ")

def InterfaceFatorail():

  while True:

    c = str (input("Deseja calcular o fatorial de um número [S/N]: ")).strip().upper()
    sleep(0.5)

    if c and c [0] == "S":

      try: 

        d = int(input("Digite um valor: "))
        linha()
        sleep(1)

        print(f"O fatorial de {d} será: {fatorial(d)}")
      
      except ValueError:

        print("ERRO: Digite um número inteiro")

        break
    
    elif c and c [0] == "N":

      print()
      break
    
    else:

      print("ERRO: Digite S ou N")

def interfaceMedia():

  valores = []

  while True:

    numeros = input("Digite um número (ou N para parar)").strip().upper()

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