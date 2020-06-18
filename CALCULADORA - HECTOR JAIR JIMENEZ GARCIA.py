# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:49:33 2020

@author: JAIR JIMENEZ
"""

import sys 
print("MENÚ")
print("1  SUMAR")
print("2  RESTAR")
print("3  MULTIPLICAR")
print("4  DIVIDIR")
print("5  SALIR DE PROGRAMA") 

proceso = input("¿QUE QUIERES HACER?")

while proceso == "SUMAR":
    print("INGRESA DOS NUMEROS")
    X1 = input("1° NUMERO")
    Y1 = input("2° NUMERO")
    x = float(X1)
    y = float(Y1)
    print("SU RESULTADO ES")
    print(x+y)
    break
    
while proceso == "RESTAR":
    print("INGRESA DOS NUMEROS")
    X1 = input("1° NUMERO")
    Y1 = input("2° NUMERO")
    x = float(X1)
    y = float(Y1)
    print("SU RESULTADO ES")
    print(x-y)
    break
  
while proceso == "DIVIDIR":
    print("INGRESA DOS NUMEROS")
    X1 = input("1° NUMERO")
    Y1 = input("2° NUMERO")
    x = float(X1)
    y = float(Y1)
    if y!=0:
        print("SU RESULTADO ES")
        print(x/y)
    while y==0:
        print("Porfavor ingrese otro divisor")
        y1 = input("2° NUMERO")
        Y = float(y1)
        if Y !=0:
            break
    print("TU RESULTADO ES")
    print(x/Y)
    break
    
while proceso == "MULTIPLICAR":
    print("INGRESA DOS NUMEROS")
    X1 = input("1° NUMERO")
    Y1 = input("2° NUMERO")
    x = float(X1)
    y = float(Y1)
    print("SU RESULTADO ES")
    print(x*y)
    break
while proceso == "SALIR":
    sys.exit(0)
    
print("MENÚ")
print("1  SUMAR")
print("2  RESTAR")
print("3  MULTIPLICAR")
print("4  DIVIDIR")
print("5  SALIR DE PROGRAMA") 

proceso = input("¿QUIERES SALIR?")
if proceso == "SI":
    sys.exit(0)