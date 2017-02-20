def mcd(m,n):
	if n==0:
		return m
	return mcd(n,m%n)
