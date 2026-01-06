from matematica.calculos import *
from time import sleep

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
  
  c = str (input("Deseja calcular o fatorial de um número [S/N]: ")).strip().upper()

  if c and c [0] == "S":

    d = int(input("Digite um valor: "))
    linha()
    sleep(1)

    print(f"O fatorial de {d} será: {fatorial(d)}")