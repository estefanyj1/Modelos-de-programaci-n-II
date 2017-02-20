def dividir(n,m):
    if (m>n):
        return 0
    else:
        return dividir (n-m,m)+1
