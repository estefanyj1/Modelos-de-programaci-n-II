#10/02/2017 Estefany Jaramillo Vera
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci (x-1) + fibonacci (x-2)


x = int(input("Ingrese un numero: "))

print ('Resultado Fibonacci: ',fibonacci(x))
