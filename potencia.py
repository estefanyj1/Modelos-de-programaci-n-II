def potencia(n,m):
	if m==0:
		return 1
	elif m%2==0:
		return potencia(n*n,m/2)
	else:
		return n*potencia(n,m-1)

