import tkinter as tk
from tkinter import ttk  # widget a tema (Themed TKinter): Combobox per i menu a tendina
                         # ->estetica più moderna di tkinter (che ha OptionMenu) (qua serve per il menù a tendina)
class Finestra(tk.Tk):

    def __init__(self):
        super().__init__()  # inizializza la finestra base di Tk

        # impostazioni della finestra principale
        self.title("To-do list Pro")
        self.geometry("650x850")
        self.configure(bg="white")

        self.content = tk.Frame(self, bg="white")   # contenitore per la sezione input e lista
        self.content.pack(expand=True, fill="both", padx=20, pady=20)  # expand/fill = occupa tutto lo spazio; padx/pady = margini

        self.tasks = []  # ogni attività: {"frame": ..., "importanza": 1|2|3} (frame = contenitore della card)

        self.priorita = {          #dizionario per importanza
            1: {"text": "Bassa", "color": "#4caf50"},
            2: {"text": "Media", "color": "#ff9800"},
            3: {"text": "Alta", "color": "#f44336"}
        }

        # campi in alto da inserire: titolo, scadenza, importanza, ripetizione
        self.v_titolo = tk.StringVar()  # variabile collegata al testo del campo
        titolo = tk.Entry(self.content, textvariable=self.v_titolo, # campo per il titolo
                          font=("Arial", 18), borderwidth=5, bg="white")  # font = stile del testo; borderwidth = bordo; bg = colore di fondo
        titolo.pack(fill="x", pady=(10, 0))  # fill="x" = larghezza piena (occupa tutta la larghezza del contenitore)

        tk.Label(self.content, text="Scadenza (es. 15:30)", bg="white", # label per la scadenza
                 fg="#9aa0a6", font=("Arial", 9)).pack(anchor="w", pady=(8, 2))  # anchor="w" = allinea a sinistra; pady = margini verticali (8, 2) = 8px in alto, 2px in basso

        self.v_ora = tk.StringVar()  # contenitore collegato al testo del campo
        scadenza = tk.Entry(self.content, textvariable=self.v_ora, # campo per la scadenza
                            font=("Arial", 12), bg="#e8eaed")  # font = stile del testo; bg = colore di fondo
        scadenza.pack(fill="x", ipady=6)  # ipady = padding interno verticale (6px)

        options_frame = tk.Frame(self.content, bg="white") # contenitore per le opzioni (importanza e ripetizione)
        options_frame.pack(pady=5, fill="x")

        tk.Label(options_frame, text="Importanza:", bg="white").pack(side="left", padx=5)
        self.vImportance = tk.IntVar(value=1)  # 1, 2 o 3
        tk.OptionMenu(options_frame, self.vImportance, 1, 2, 3).pack(side="left", padx=5)  # tk.OptionMenu = menu a tendina 

        self.v_ripeti = tk.StringVar(value="Non si ripete")
        combo_ripeti = ttk.Combobox(self.content, textvariable=self.v_ripeti, state="readonly")  # ttk.Combobox = menu a tendina con valori predefiniti (readonly = solo scelta, no digitazione)
        combo_ripeti["values"] = ("Non si ripete", "Ogni giorno", "Ogni settimana", "Ogni mese") 
        combo_ripeti.pack(fill="x", pady=10)

        row_desc = tk.Frame(self.content, bg="white") # contenitore per la descrizione
        row_desc.pack(fill="x", pady=10) # posizionamento del contenitore nel contenitore principale
        tk.Label(row_desc, text="≡", bg="white", fg="gray", font=("Arial", 14)).pack(side="left", padx=(0, 15), anchor="n") # label per la descrizione

        self.txt_desc = tk.Text(row_desc, height=3, bg="#e8eaed", font=("Arial", 10), padx=10, pady=10)  # Text ≠ Entry: più righe (Text = più righe, Entry = una riga)
        self.txt_desc.pack(fill="x", expand=True) # posizionamento del campo nel contenitore

        self.btn_salva = tk.Button(self.content, text="Salva", bg="#1a73e8", fg="white", # bg = colore di fondo; fg = colore del testo
                                   font=("Arial", 10, "bold"), padx=25, pady=8, # font = stile del testo; padx = padding orizzontale; pady = padding verticale
                                   command=self.aggiungi) 
        self.btn_salva.pack(anchor="e", pady=10)  # anchor="e" = allinea a destra (east); pady = padding verticale (10px) 

        # bottone per riordinare per importanza
        self.btnSort = tk.Button(self.content, text="Riordina per Priorità", command=self.riordina, bg="#fff9c4")
        self.btnSort.pack(pady=5) #pack=posizionamento del bottone nel contenitore principale

        self.task_list_container = tk.LabelFrame(self.content, text="Le tue Task", bg="white")  # LabelFrame = cornice con titolo (contenitore per la lista delle task) 
        self.task_list_container.pack(fill="both", expand=True, pady=15)

    def aggiungi(self):
        testo = self.v_titolo.get().strip() # get() = ottiene il testo del campo; strip() = rimuove gli spazi bianchi iniziali e finali
        if not testo:  # non salvare task senza titolo
            return
        ora = self.v_ora.get().strip()
        ripetizione = self.v_ripeti.get() 
        descrizione = self.txt_desc.get("1.0", tk.END).strip()  # "1.0" = prima riga, primo carattere; END = fine testo (Le righe partono da 1 (non da 0). Le colonne da 0.)
        i_val = self.vImportance.get()                          # -> è come dire "prendi tutto il testo dal primo carattere della prima riga fino alla fine del testo")
                                                                # -> da ricordarsi che text e entry sono due widget diversi (Text = più righe, Entry = una riga)
        #Card della singola task nella lista
        frame_task = tk.Frame(self.task_list_container, bg="white")  # contenitore "card": spostandolo si sposta tutta la riga  
        frame_task.pack(fill="x", anchor="w", pady=5, padx=5)  # fill="x" = larghezza piena nel LabelFrame

        content_frame = tk.Frame(frame_task, bg="white")
        content_frame.pack(side="left", fill="x", expand=True, padx=10, pady=5)  # expand=True = occupa lo spazio a sinistra della checkbox

        title_row = tk.Frame(content_frame, bg="white")
        title_row.pack(fill="x")

        ora_mostra = f"({ora}) "  # mostra l'orario
        label_titolo = tk.Label(title_row, text=f"{ora_mostra}{testo}",
                                font=("Arial", 11, "bold"), bg="white", anchor="w")
        label_titolo.pack(side="left")

        badge_row = tk.Frame(content_frame, bg="white")
        badge_row.pack(fill="x", pady=2)

        i_info = self.priorita[i_val]  # dizionario con testo ("Alta"/"Media"/"Bassa") e colore del badge
        lbl_i = tk.Label(badge_row, text=f"Importanza: {i_info['text']}", font=("Arial", 7, "bold"),
                         fg="white", bg=i_info["color"], padx=5, pady=0)
        lbl_i.pack(side="left")

        lbl_rep = None  # inizializzato a None: serve per sapere in segna_come_completato se il label esiste
        if ripetizione != "Non si ripete":
            lbl_rep = tk.Label(content_frame, text=f"{ripetizione}",
                               font=("Arial", 8), fg="#1a73e8", bg="white", anchor="w")
            lbl_rep.pack(fill="x")

        lbl_desc = None
        if descrizione:
            lbl_desc = tk.Label(content_frame, text=descrizione,
                                font=("Arial", 9, "italic"), fg="gray", bg="white",
                                anchor="w", justify="left", wraplength=400)  # wraplength = a capo automatico dopo ~400 pixel
            lbl_desc.pack(fill="x")

        def segna_come_completato(): #messa dentro la def aggiungi perché deve agire solo su una sola task, non su tutte
            #richiamata della checkbox (la casella quadrata): rende lo stile 'completato' (grigio) e blocca ulteriori click.
            label_titolo.config(fg="gray", font=("Arial", 11, "overstrike"))  # overstrike = testo barrato
            lbl_i.config(bg="lightgray")
            if lbl_rep:  # controlla prima se il label ripetizione è stato creato
                lbl_rep.config(fg="lightgray")
            if lbl_desc:
                lbl_desc.config(fg="lightgray") 
            cb.config(state=tk.DISABLED)  # disabilita la checkbox dopo il completamento

        var = tk.IntVar()  # 0 = non spuntato, 1 = spuntato (collegato alla Checkbutton)
        cb = tk.Checkbutton(frame_task, text="Fatto", variable=var,
                            command=segna_come_completato, bg="white")
        # command viene chiamato al click; la funzione interna "vede" label_titolo, lbl_i, ecc.
        cb.pack(side="right", padx=10)  # side="right" = checkbox allineata a destra della card

        self.tasks.append({"frame": frame_task, "importanza": i_val})  # salva riferimento per riordino successivo

        # Svuota i campi input dopo il salvataggio (pronto per la prossima task)
        self.v_titolo.set("")
        self.v_ora.set("")
        self.txt_desc.delete("1.0", tk.END)  # il widget Text richiede delete esplicito (non basta .set("") come per Entry)

    def riordina(self):
        # ordina le card per importanza decrescente (3 in alto, 1 in basso) e aggiorna il layout.
        # l'importanza 1,2,3
        ordinate = []
        for t in self.tasks:
            if t["importanza"] == 3:
                ordinate.append(t)
        for t in self.tasks:
            if t["importanza"] == 2:
                ordinate.append(t)
        for t in self.tasks:
            if t["importanza"] == 1:
                ordinate.append(t)
        self.tasks = ordinate

        # Tkinter non riordina da solo: togli e rimetti ogni card nell'ordine della lista
        for t in self.tasks:            # rimuovi e riaggiungi le task nella lista self.tasks per aggiornare l'ordine (Stai spostando il contenitore della card, non il testo da solo:         
            t["frame"].pack_forget()    # -> titolo, badge e checkbox si muovono insieme perché sono tutti figli di quel frame_task)
        for t in self.tasks:                                        # pack_forget() toglie il widget dal layout senza distruggerlo
            t["frame"].pack(fill="x", anchor="w", pady=5, padx=5)   # pack rimette l'oggetto nell'ordine della lista (la lista self.tasks)

def main():
    f = Finestra()
    f.mainloop()  
    
main()
