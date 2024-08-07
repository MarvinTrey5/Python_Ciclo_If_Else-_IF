#Hacer  un  programa  en  Python  que  determine  
# por  rangos  si  un  valor  está 
#contenido en cada rango, por ejemplo:  de 1 a 10 el numero 7 está contenido, 
#del 11 al 20 el 15 está contenido.

import random

print("------------------------")

num = random.randrange(1,10)
if num == 7:
    print("Número aleatorio: ",num)
else:
    print("El número 7 está contenido en el rango: ",num)

print("----------------------------------")

num2= random.randrange(11,20)
if num2 == 15:
    print("Número aleatorio: ",num2)
else:
    print("El número 15 está contenido en el rango: ",num2)

print("Fin del programa")