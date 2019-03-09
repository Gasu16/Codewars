from math import sqrt
from itertools import count, islice

# isPrime ritorna True se il numero dato come argomento e' primo, altrimenti ritorna False
def isPrime(num):
    return num > 1 and all(num%i for i in islice(count(2), int(sqrt(num)-1)))

def gap(g, m, n):
    lstart = [] # Lista dove andremo a mettere la coppia di numeri primi
    lend = []
    gapesiste = False
    for i in range(m, n):
        if isPrime(i):
            lstart.append(i)
    for j in range(len(lstart)-1):
        if lstart[j+1] - lstart[j] == g:
            gapesiste = True
            #lend.append(lstart[j+1], lstart[j])
            lend.append(lstart[j])
            lend.append(lstart[j+1])
            break
            #lend.extend([lstart[j], lstart[j+1]])


    if gapesiste == False:
        return None
    print(lend)
    return lend


def main(args):
    gap(6, 100, 110) # Cerchiamo la prima coppia di numeri primi dove ci sia un gap di 2 nell'intervallo di numeri tra 100 e 110
    #print(isPrime(7))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))