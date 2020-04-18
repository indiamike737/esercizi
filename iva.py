def iva():
    p = int(input())
    prod = (p/122)*100
    imposta = (p/122)*22
    print(prod)
    print(imposta)



def iva2():
    p = int(input())
    prod = (p/122)*100
    imposta = (p/122)*22
    return (prod, imposta) # scrivo i due valori che voglio far ritornare


if __name__ == "__main__": # pseudo-funzione per far sì che venga distinto
    #iva() # le funzioni(che non partono) ed i comandi che le fanno partire
    x, y = iva2() # per non far partire le funzioni non scrivo niente
    print(x)
    print(y)
