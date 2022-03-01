
#Escribir una función que simule una calculadora científica que permita calcular el seno,
#  coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor 
# y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
# y el resultado de aplicar la función a esos enteros.

import math

menu= """
Bienvenido a la calculadora de funciones trigronometricas de Santiago
Selecciona una función que quieras usar:
1- Seno
2- Coseno
3- Tangente
4- Exponencial
5- Logaritmo neperiano
"""
option= int(input (menu))

def functions ():
    value = int (input(" ingrese el valor a calcular: "))
    assert value>0, "ingresa un numero positivo" 
    if    option==1:
     answer = math.sin (value)
    elif  option==2:
     answer = math.cos (value)
    elif  option==3:
     answer = math.tan (value)
    elif  option==4: 
     answer = math.exp (value)
    elif  option==5:
     answer= math.log (value)
    else:
        print ("ingresa un valor valido ")
    answer= round(answer,2)
    print (" tu función escogida fue: ")
    print (option)
    print (" y  el valor de tu función fue: ")
    print (answer)

functions ()
