import math
def piano():
    px = int(input())
    py = int(input())
    d = math.sqrt(px**2+py**2)
    return d

#x = piano()  # nella variabile x inserisco la funzione piano
#print(x)     # stampo x e stampo così anche il valore della funzione


def piano2(px,py):
    d = math.sqrt(px**2+py**2)
    return d

#x = piano2(0,3)  # la funzione piano viene direttamente stampata perché ho già assegnato i valori
#print(x)

def piano3():
    px = int(input())
    py = int(input())
    d = math.sqrt(px**2+py**2)
    print(d)

piano3() #chiamo la funzione  per stampare d
