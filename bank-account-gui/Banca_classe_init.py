class Conto(object):
#tolgo l'elenco di attributi perché il costruttore li valorizza tutti
    def __init__(self,n,c,s):
        self.nome=n
        self.cognome=c
        self.IBAN="IT44"
        if s>=50:
            self.__saldo=s
        else:
            self.__saldo=0
    
#tolgo setSaldoIniziale perché si fa solo una volta, dunque non tornerà utile per altro

    def Utente(self):
        return ("L'utente è "+self.nome+" "+self.cognome+" con IBAN "+self.IBAN+" e un saldo iniziale di "+str(self.__saldo)+" euro.")

    def Prelievo(self,x):
        self.__saldo-=x
        return self.__saldo

    def Versamento(self,x):
        self.__saldo+=x
        return self.__saldo
