# Hacer un ejercicio en Python que determine el mayor de 4 tres números.
print("--------------------")
# Ingresamos los 4 números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))
n4 = int(input("Ingresa el cuarto número: "))
# Utilizamos el if para establecer condiciones 
# de los 4 números ingresados para saber cual
# es el Mayor.
# Ciclos de manera anidada.
if n1 > n2 and n1 > n3 and n1 > n4:
    print("El número mayor es: ",n1)
elif n2 > n1 and n2 > n3 and n2 > n4:
    print("El número mayor es: ",n2)
elif n3 > n1 and n3 > n2 and n3 > n4:
    print("El número mayor es: ",n3)
elif n4 > n1 and n4 > n2 and n4 >n3:
    print("El número mayor es: ",n4)
else:
    print("No se establece el mayor")

print("Fin del ejercicio")