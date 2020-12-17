def __Perfect(numbr):
    Sum = 0
    for i in range(1, numbr):
        if(numbr % i == 0):
            Sum = Sum + i

    if (Sum == numbr):
        return True
    else:
        return False

def __main__():
    print("Numeros perfeitos:")
    for i in range(1, 10000):
        if(__Perfect(i)):
             print(" %d é um número Perfeito:" %i)
    
        
__main__()