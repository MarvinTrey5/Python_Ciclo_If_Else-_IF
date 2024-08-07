Extras = 20
horas = int(input("Ingrese las horas trabajadas: "))
if ( horas > 40):
    SalarioSemanal = horas * 16
    print("Tu Salario Semanal es de: ", SalarioSemanal)
elif(horas <= 40):
    SalarioSemanal = horas * 16 + Extras
    print("Tu Salario Semanal es de: ", SalarioSemanal)