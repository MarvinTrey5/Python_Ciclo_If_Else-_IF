# Variable para ingresar el nombre.
nombre = input("Escribe tu nombre: ")
# Variable para la edad.
edad = int (input("Escribe tu edad: "))
print("-------------------")
# Mostramos el resultado con concatenación.
print(nombre,"tu edad es:", edad," años")
print("-------------------")
# Verificamos si es mayoe a 18 años.
if edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")