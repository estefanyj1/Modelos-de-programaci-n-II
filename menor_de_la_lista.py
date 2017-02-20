def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    elif lista[0] >= lista[1]:
        return minimo(lista[1:])
    else:
        return minimo([lista[0]]+lista[2:])
def ListaFinal(lista):
    if lista==[]:
        return []
    else:
        return [minimo(lista[0])]+ListaFinal(lista[1:])
lista1 = [5,6,7,8,9]
lista2 = [1,2,3,4,5]
lista3 = [25,90,50,11]
listadeListas = [lista1,lista2,lista3]
print (ListaFinal(listadeListas))