def sumatoriaDigitos(x):
    if x<10:
        return x
    else:
        return x%10 + sumatoriaDigitos(x/10)


x = int(input("Ingrese un numero: "))

print ('Resultado sumatoria: ',sumatoriaDigitos(x))




"REVISAR PORQUE NO ESTÁ FUNCIONANDO BIEN"
