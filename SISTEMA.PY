from matematica.calculos import *
from interfacee.terminal import *
from time import sleep

menuPrincipal()
sleep(1)

a = float (input("Digite o 1° valor: "))
sleep(0.5)

b = float (input("Digite o 2° valor:"))
sleep(0.5)

InterfaceCalculos(a, b, "+", soma(a,b))
InterfaceCalculos(a, b, "-", sub (a, b))
InterfaceCalculos(a, b, "*", multi (a, b))
InterfaceCalculos(a, b, "/", div(a, b))

menuFatorial()
sleep(1)

InterfaceFatorail()

