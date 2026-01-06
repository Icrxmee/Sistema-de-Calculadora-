from matematica.calculos import *
from interfacee.terminal import *
from time import sleep

menuPrincipal()
sleep(1)

while True:

    opcao = menuOpcoes()

    if opcao == "1":
      interfaceOperações()

    if opcao == "2":
      menuFatorial()
      sleep(0.5)
      InterfaceFatorail()
    
    if opcao == "3":
       menuMedia()
       sleep(0.5)
       interfaceMedia()

    if opcao == "0":
       encerramento()
       break       

    if opcao not in "0123":
       print("ERRO: Digite uma opção válida!!!")
       sleep(1)
