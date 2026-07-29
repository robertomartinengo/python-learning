from funzioni_trova_calogero import *

dimensione=int(input("Scegli la dimensione della griglia (max.9): "))
while dimensione<=0 or dimensione>9:
    dimensione=int(input("Scegli la dimensione della griglia (max.9): "))
tentativi_massimi=((dimensione**2)//2)+1
tentativi_rimasti=tentativi_massimi

griglia=creazionerecinto(dimensione)
C_riga,C_colonna=posiziona_C(dimensione)

lettere=["A","B","C","D","E","F","G","H","I"]

print("Benvenuto a 'Trova Calogero': la pecorella si sta nascondendo nel fienile, il tuo compito è trovarlo con una balestra!")
print("Hai",tentativi_rimasti,"tentativi per scovare Calogero (1x1).")
disegnarecinto(griglia,dimensione)

while tentativi_rimasti>0:
    coordinate_input=input("Inserisci le coordinate del tuo sparo (es. A1, max. I9): ")

    lunghezza=len(coordinate_input)

    while lunghezza!=2:
        print("Il formato dell'input non è valido. Inserisci una lettera e un numero.")
        coordinate_input=input("Inserisci le coordinate del tuo sparo (es.A1): ")
        lunghezza=len(coordinate_input)
    tentativi_rimasti=tentativi_rimasti-1

    lettera=coordinate_input[0]
    numero=int(coordinate_input[1])

    lettere=["A","B","C","D","E","F","G","H","I"]
    riga_tiro=lettere.index(lettera.upper())
    colonna_tiro=numero-1

    if not (0<=riga_tiro<dimensione and 0<=colonna_tiro<dimensione):
        print("Coordinate fuori dal recinto!")

    i=0
    for riga in griglia:
        if i==riga_tiro:
            contenuto_riga_tiro=riga
        i+=1

    j=0
    for simbolo in contenuto_riga_tiro:
        if j==colonna_tiro:
            simbolo_cella=simbolo
        j+=1

    if simbolo_cella != '~':
        print("Hai già sparato in queste coordinate!")
    
    elif riga_tiro==C_riga and colonna_tiro==C_colonna:
        print("Hai colpito Calogero in",tentativi_massimi-tentativi_rimasti,"tentativi!")
        j=0
        for i in contenuto_riga_tiro:
            if j==colonna_tiro:
                contenuto_riga_tiro[j]='X'
            j+=1
        disegnarecinto(griglia,dimensione)
        tentativi_rimasti=0
    else:
        print("Fieno.")
        j=0
        for i in contenuto_riga_tiro:
            if j==colonna_tiro:
                contenuto_riga_tiro[j]='O'
                
            j+=1
        disegnarecinto(griglia,dimensione)
        if tentativi_rimasti!=0:
            print("Ti rimangono",tentativi_rimasti,"tentativi.")
        else:
            print("Hai esaurito i tuoi tentativi!")

lettera_C = lettere[C_riga]
numero_C=C_colonna+1 

print("Calogero era in: "+str(lettera_C)+str(numero_C))
griglia_con_C=creazionerecinto(dimensione)

i=0
for riga in griglia_con_C:
    if i==C_riga:
        riga_finale=riga
    i+=1

j=0
for colonna in riga_finale:
    if j==C_colonna:
        riga_finale[j]='#'
    j+=1
disegnarecinto(griglia_con_C,dimensione)
