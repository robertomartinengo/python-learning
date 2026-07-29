import random

def creazionerecinto(dimensione):
    griglia=[]
    for i in range(dimensione):
        riga=[]
        for j in range(dimensione):
            riga.append('~')
        griglia.append(riga)
    return griglia

def disegnarecinto(griglia,dimensione):
    lettere=["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    
    print('  ',end='')
    for i in range(dimensione):
        print(i+1,end=' ')
    print()

    for i in range(dimensione):
        print(lettere[i],end=' ')
        riga_corrente=griglia[i]
        for simbolo in riga_corrente:
            print(simbolo,end=' ')
        print()

def posiziona_C(dimensione):
    riga=random.randint(0,dimensione-1)
    colonna=random.randint(0,dimensione-1)
    return riga,colonna
