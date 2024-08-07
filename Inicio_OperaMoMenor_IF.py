# Hacer un programa que el usuario ingrese el nombre y edad 
# Hay una montaña rusa, el guardía preguntará si el nombre es hijo 
# del dueño se utilizará los operadores lógicos y el if.

# Se crean las variables y el usuario ingresa el nombre y edad
nombre = input('¿Cómo te llamas?: ')
print('Hola ' + nombre)

# El usuario ingresa la edad
edad = int(input('¿Cuántos años tienes?: '))
print(' Ha Tienes ' + str(edad) + ' Años ')
#Utilizaremos el operador lógico >= Mayor o Igual.
masDe14 = edad >= 18
#El guardía pregunta si eres Mayor de edad.
preguntaElguardia = input('¿Eres Mayor de Edad? ')
#Si tu respuesta es 'si' pasarás, si tu respuesta es 'no', No pasarás.
mayorDeEdad = preguntaElguardia == 'si'
#Aquí utilizamos la variable creada en el if para 
#que cumpla lo establecido con la edad y si es mayor de edad.
puedesPasar = masDe14 or mayorDeEdad

# Utilizamos if y creamos la varible puedesPasar
# si la condición creada en la linea 20 se cumple 'si' pasará
# si la respuesta es 'no', no lo hará.
if puedesPasar:
    print('Sí, puedes pasar a la Montaña Rusa')
    print('Diviertéte ' + nombre)
else:
    print('No Puedes Pasar ')
    print('Lo sentimos ' + nombre)