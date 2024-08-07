''' 
    1. Un error que tenemos cuando inicializamos es donde se ejecuta
    la acción del if es decir, una línea de código debe ejecutarse
    cuando se cumple. Pero cuando no debe mostrar lo contrario.
    Ejemplo 3 usaremos nada más if
    En el cuál si es diferente o igual a 0.
    entonces hará una división.
    y mostraremos un mensaje. 
    Mostraremos un mensaje cuando este fuera de la condición.
'''
x = 8
z = 4
if x != 0:
    total = (x/z)
    print("dentro del if: ", total)
print("Fuera del if") 