# Python Utiizando Operadores lógicos.
# Ejemplo creamos una variable que se llamará
# edad y sabremos si es mayor de edad o menor 
# utilizando los operadores lógicos.
nombre = input('¿Como te llamas?: ')
print('Hola ' + nombre)
# ahora nosotros ingresaremos nuestra edad en la variable de abajo.
edad = int(input('¿Cuántos años tienes: '))
if edad >= 18: # Utilizamos El Mayor igual(">=") para que cuando lo ejecutemos si esa persona es igual a 18 pues será Mayor.
    print('Es mayor de edad')
else:
    print('Es menor de edad')