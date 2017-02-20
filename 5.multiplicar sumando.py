#10/02/2017 Estefany Jaramillo Vera
def mulSumando(x,y):
    
    if y == 0:
        return y
    else:
        return x + mulSumando(x,y-1)

print ('')
x = int(input("Ingrese un numero: "))
print ('Usted ingreso: ', x)
y = int(input("Ingrese un numero: "))
print ('Usted ingreso: ', y)


print ("el resultado es:", mulSumando(x,y))


