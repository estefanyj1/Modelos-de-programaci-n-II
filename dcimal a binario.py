
def decABin(f):
    if (f==1 or f==0):
        return f
    else:
        return decABin(f/2), f%2
