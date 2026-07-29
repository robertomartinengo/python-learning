import tkinter as tk
from Banca_classe_init import *

class Finestra(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("600x450")
        self.master.title("Banca")
        self.grid()

        self.nome = tk.Label()
        self.nome.grid(row=0,column=0)
        self.nome.configure(background="#d9d9d9")
        self.nome.configure(foreground="#000000")
        self.nome.configure(text="Nome")
        
        self.vnome=tk.StringVar()
        self.txtnome = tk.Entry(textvariable=self.vnome)
        self.txtnome.grid(row=1, column=0)
        self.txtnome.configure(background="white")
        self.txtnome.configure(foreground="#000000")

        self.cognome = tk.Label()
        self.cognome.grid(row=0,column=1)
        self.cognome.configure(background="#d9d9d9")
        self.cognome.configure(foreground="#000000")
        self.cognome.configure(text="Cognome")

        self.vcognome=tk.StringVar()
        self.txtcognome = tk.Entry(textvariable=self.vcognome)
        self.txtcognome.grid(row=1, column=1)
        self.txtcognome.configure(background="white")
        self.txtcognome.configure(foreground="#000000")

        self.saldoinizio = tk.Label()
        self.saldoinizio.grid(row=0,column=2)
        self.saldoinizio.configure(background="#d9d9d9")
        self.saldoinizio.configure(foreground="#000000")
        self.saldoinizio.configure(text="Saldo iniziale")

        self.vsaldoinizio=tk.StringVar()
        self.txtsaldoinizio = tk.Entry(textvariable=self.vsaldoinizio)
        self.txtsaldoinizio.grid(row=1, column=2)
        self.txtsaldoinizio.configure(background="yellow")
        self.txtsaldoinizio.configure(foreground="#000000")

        self.btncrea = tk.Button()
        self.btncrea.grid(row=1,column=3)
        self.btncrea.configure(background="#d9d9d9")
        self.btncrea.configure(foreground="#000000")
        self.btncrea.configure(text="Crea")
        self.btncrea.configure(command=self.crea)

        #self.lblconto = tk.Label()
        #self.conto.grid(row=2,column=0)
        #self.lblconto.configure(background="#d9d9d9")
        #self.lblconto.configure(foreground="#000000")
        #self.lblconto.configure(text="Conto Corrente")

        #self.vconto=tk.StringVar()
        #self.txtconto = tk.Entry(textvariable=self.vconto)
        #self.txtconto.grid(row=3, column=0)
        #self.txtconto.configure(background="white")
        #self.txtconto.configure(foreground="#000000")

        self.cifra = tk.Label()
        #self.cifra.grid(row=0,column=2)
        self.cifra.configure(background="#d9d9d9")
        self.cifra.configure(foreground="#000000")
        self.cifra.configure(text="Cifra da versare/prelevare")
        
        self.vcifra=tk.IntVar()
        self.txtcifra = tk.Entry(textvariable=self.vcifra)
        #self.txt3.grid(row=4, column=0)
        self.txtcifra.configure(background="white")
        self.txtcifra.configure(foreground="#000000")

        self.vR=tk.IntVar()
        self.rdbVersa=tk.Radiobutton(text="Versa", variable=self.vR, value=1)
        #self.rdbVersa.grid(row=1, column=0, sticky=tk.W)
        self.rdbpreleva=tk.Radiobutton(text="Preleva", variable=self.vR, value=2)
        #self.rdbpreleva.grid(row=2, column=0, sticky=tk.W)

        self.btnesegui = tk.Button()
        #self.btnesegui.grid(row=8,column=0)
        self.btnesegui.configure(background="#d9d9d9")
        self.btnesegui.configure(foreground="#000000")
        self.btnesegui.configure(text="Esegui")
        self.btnesegui.configure(command=self.operazione)

        self.lblsaldofine = tk.Label()
        #self.lblsaldofine.grid(row=9,column=0)
        self.lblsaldofine.configure(background="#d9d9d9")
        self.lblsaldofine.configure(foreground="#000000")
        self.lblsaldofine.configure(text="Saldo finale")

        self.vsaldofine=tk.IntVar()
        self.txtsaldofine = tk.Entry(textvariable=self.vsaldofine)
        #self.txtsaldofine.grid(row=10, column=0)
        self.txtsaldofine.configure(background="cyan")
        self.txtsaldofine.configure(foreground="#000000")

        self.btnchiudi = tk.Button()
        #self.btnchiudi.grid(row=8,column=0)
        self.btnchiudi.configure(background="#d9d9d9")
        self.btnchiudi.configure(foreground="#000000")
        self.btnchiudi.configure(text="Esegui")
        self.btnchiudi.configure(command=self.chiudi_banca)

 
    def crea(self):
        n=self.vnome.get()
        c=self.vcognome.get()
        si=int(self.vsaldoinizio.get())
        self.conto=Conto(n,c,si)
        #account=self.conto.Utente()
        #self.vconto.set(account)
        #self.txtconto.configure(width=len(account))
        
        self.btncrea.grid_forget()
        #self.lblconto.grid(row=2,column=0)
        #self.txtconto.grid(row=3,column=0)
        self.cifra.grid(row=4,column=0)
        self.txtcifra.grid(row=5, column=0)
        self.rdbVersa.grid(row=6, column=0, sticky=tk.W)
        self.rdbpreleva.grid(row=7, column=0, sticky=tk.W)
        self.btnesegui.grid(row=8,column=0)
        self.lblsaldofine.grid(row=9,column=0)
        self.txtsaldofine.grid(row=10, column=0)
        
    def operazione(self):
        cifra=self.vcifra.get()
        a=self.vR.get()
        if a==1:
            op=self.conto.Versamento(cifra)
        elif a==2:
            op=self.conto.Prelievo(cifra)
        self.vsaldofine.set(op)

    def chiudi_banca(self):
        Finestra.destroy()


        

def main():
    f = Finestra()
    f.mainloop()

main()
