import sqlite3
from tkinter import *
from tkinter import messagebox


def accueil():
    for i in optionframe2.winfo_children():
        i.destroy()

    label_acc = Label(optionframe2,
                      text='BIENVENNUE \n Description :  Notre programme permet aux utilisateurs d\' ajouter,\n supprimer, modifier et rechercher des éléments dans une base de donnée',
                      width=55, height=5)
    label_acc.place(x=65, y=45)

    btn_create_db = Button(optionframe2, text="Créer une base de Données", command=create_database, cursor='hand2')
    btn_create_db.place(x=160, y=150)

    btn_create_af = Button(optionframe2, text="Afficher Ma Base de Donnée", command=select_database, cursor='hand2')
    btn_create_af.place(x=158, y=200)


def create_database():
    try:
        conn = sqlite3.connect('ventes.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS ventes_clean (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date DATE,
                    Product TEXT,
                    Price REAL,
                    Quantity INTEGER,
                    Region TEXT
                )''')
        conn.commit()
        messagebox.showinfo("Information", "Base de données créée avec succès")
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de la création de la base de données: {e}")
    finally:
        conn.close()


def select_database():
    for i in optionframe2.winfo_children():
        i.destroy()
    listbox = Listbox(optionframe2, height=15, width=60)
    listbox.place(x=65, y=45)
    listbox.insert('end', 'ID          Date                 Product    Price     Quantity        Region          ')

    conn = sqlite3.connect('ventes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ventes_clean")
    rows = c.fetchall()

    for row in rows:
        listbox.insert('end',
                       f'{row[0]}          {row[1]}          {row[2]}          {row[3]}          {row[4]}          {row[5]}')
    conn.close()


def ajouter():
    for i in optionframe2.winfo_children():
        i.destroy()

    Label(optionframe2, text="Date :").place(x=130, y=45)
    entry_date = Entry(optionframe2)
    entry_date.place(x=200, y=45)

    Label(optionframe2, text="Produit :").place(x=130, y=85)
    entry_produit = Entry(optionframe2)
    entry_produit.place(x=200, y=85)

    Label(optionframe2, text="Prix :").place(x=130, y=125)
    entry_prix = Entry(optionframe2)
    entry_prix.place(x=200, y=125)

    Label(optionframe2, text="Quantité :").place(x=130, y=165)
    entry_quantite = Entry(optionframe2)
    entry_quantite.place(x=200, y=165)

    Label(optionframe2, text="Région :").place(x=130, y=205)
    entry_region = Entry(optionframe2)
    entry_region.place(x=200, y=205)

    btn = Button(optionframe2, text="Confirmer",
                 command=lambda: Insertion(entry_date.get(), entry_produit.get(), entry_prix.get(),
                                           entry_quantite.get(), entry_region.get()))
    btn.place(x=200, y=255)


def Insertion(date, product, price, quantity, region):
    try:
        conn = sqlite3.connect('ventes.db')
        c = conn.cursor()
        c.execute("INSERT INTO ventes_clean (Date, Product, Price, Quantity, Region) VALUES (?, ?, ?, ?, ?)",
                  (date, product, price, quantity, region))
        conn.commit()
        messagebox.showinfo("Information", "Données insérées avec succès")
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'insertion des données: {e}")
    finally:
        conn.close()


def supprimer():
    for i in optionframe2.winfo_children():
        i.destroy()

    Label(optionframe2, text="Entrez l'ID du produit à supprimer : ").place(x=90, y=85)
    entry_id = Entry(optionframe2)
    entry_id.place(x=300, y=85)

    def confirmer_supression():
        element_id = entry_id.get()
        if not element_id.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")
            return

        conn = sqlite3.connect('ventes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ventes_clean WHERE ID = ?", (element_id,))
        element = c.fetchone()

        if element:
            info = f"ID: {element[0]}\nDate: {element[1]}\nProduit: {element[2]}\nPrix: {element[3]}\nQuantité: {element[4]}\nRégion: {element[5]}"
            confirmation = messagebox.askyesno("Confirmation",
                                               f"Produit trouvé:\n{info}\nVoulez-vous vraiment supprimer ce produit ?")
            if confirmation:
                c.execute("DELETE FROM ventes_clean WHERE ID = ?", (element_id,))
                conn.commit()
                messagebox.showinfo("Information", "Produit supprimé avec succès.")
        else:
            messagebox.showerror("Erreur", "Aucun produit trouvé avec cet ID.")

        conn.close()

    btn_confirm = Button(optionframe2, text="Confirmer", command=confirmer_supression)
    btn_confirm.place(x=200, y=150)


def rechercher():
    for i in optionframe2.winfo_children():
        i.destroy()

    Label(optionframe2, text="Entrez l'ID du produit à rechercher : ").place(x=90, y=85)
    entry_id = Entry(optionframe2)
    entry_id.place(x=300, y=85)

    def recherche_produit():
        element_id = entry_id.get()
        if not element_id.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")
            return

        conn = sqlite3.connect('ventes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ventes_clean WHERE ID = ?", (element_id,))
        element = c.fetchone()

        if element:
            inf = f"ID: {element[0]}\nDate: {element[1]}\nProduit: {element[2]}\nPrix: {element[3]}\nQuantité: {element[4]}\nRégion: {element[5]}\n"
            conf = messagebox.askyesno("Confirmation",
                                       f"Produit trouvé:\n{inf}, Est-ce bien le produit que vous rechercher ?")
            if conf:
                messagebox.showinfo("Information", "Parfait.")
            else:
                messagebox.showinfo("Information", "Veuillez réssayer avec un autre identifiant.")
        else:
            messagebox.showwarning("Produit non trouvé", "Aucun produit trouvé avec cet ID.")

        conn.close()

    btn_recherche = Button(optionframe2, text="Rechercher", command=recherche_produit)
    btn_recherche.place(x=200, y=150)


def mettre_a_jour():
    for i in optionframe2.winfo_children():
        i.destroy()

    Label(optionframe2, text="Entrez l'ID du produit à modifier:").place(x=50, y=45)
    entry_id = Entry(optionframe2)
    entry_id.place(x=250, y=45)

    Label(optionframe2, text="Nouvelle Date").place(x=50, y=85)
    entry_date = Entry(optionframe2)
    entry_date.place(x=250, y=85)

    Label(optionframe2, text="Nouveau Produit").place(x=50, y=125)
    entry_produit = Entry(optionframe2)
    entry_produit.place(x=250, y=125)

    Label(optionframe2, text="Nouveau Prix").place(x=50, y=165)
    entry_prix = Entry(optionframe2)
    entry_prix.place(x=250, y=165)

    Label(optionframe2, text="Nouvelle Quantité").place(x=50, y=205)
    entry_quantite = Entry(optionframe2)
    entry_quantite.place(x=250, y=205)

    Label(optionframe2, text="Nouvelle Région").place(x=50, y=245)
    entry_region = Entry(optionframe2)
    entry_region.place(x=250, y=245)

    def confirm_maj():
        element_id = entry_id.get()
        date = entry_date.get()
        product = entry_produit.get()
        price = entry_prix.get()
        quantity = entry_quantite.get()
        region = entry_region.get()

        if not element_id.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")
            return

        try:
            conn = sqlite3.connect('ventes.db')
            c = conn.cursor()
            c.execute("UPDATE ventes_clean SET Date = ?, Product = ?, Price = ?, Quantity = ?, Region = ? WHERE ID = ?",
                      (date, product, price, quantity, region, element_id))
            conn.commit()

            if c.rowcount == 0:
                messagebox.showerror("Erreur", "Aucun produit trouvé avec cet ID.")
            else:
                messagebox.showinfo("Information", "Produit mis à jour avec succès.")
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la mise à jour des données: {e}")
        finally:
            conn.close()

    btn_confirm = Button(optionframe2, text="Confirmer", command=confirm_maj)
    btn_confirm.place(x=250, y=285)


root = Tk()
root.geometry('500x400')

optionframe = Frame(root, width=500, height=50, bg='lightblue')
optionframe.pack(side='top')

acc = Button(optionframe, bg='lightblue', font='bold', text='Accueil', bd=0, cursor='hand2', command=accueil)
acc.place(x=25, y=5)

ajt = Button(optionframe, text='Ajouter', font=('bold', 10), bd=0, bg='lightblue', cursor='hand2', command=ajouter)
ajt.place(x=180, y=12)

spp = Button(optionframe, text='Supprimer', font=('bold', 10), bd=0, bg='lightblue', cursor='hand2', command=supprimer)
spp.place(x=240, y=12)

rch = Button(optionframe, text='Rechercher', font=('bold', 10), bd=0, bg='lightblue', cursor='hand2',
             command=rechercher)
rch.place(x=320, y=12)

maj = Button(optionframe, text='Mettre à Jour', font=('bold', 10), bd=0, bg='lightblue', cursor='hand2',
             command=mettre_a_jour)
maj.place(x=400, y=12)

optionframe2 = Frame(root, width=500, height=350, bg='black')
optionframe2.pack(side='bottom')

label_acc = Label(optionframe2,
                  text='BIENVENNUE \n Description :  Notre programme permet aux utilisateurs d\' ajouter,\n supprimer, modifier et rechercher des éléments dans une base de donnée',
                  width=55, height=5)
label_acc.place(x=60, y=45)

btn_create_db = Button(optionframe2, text="Créer une base de Données", command=create_database, cursor='hand2')
btn_create_db.place(x=160, y=180)

btn_create_af = Button(optionframe2, text="Afficher Ma Base de Donnée", command=select_database, cursor='hand2')
btn_create_af.place(x=158, y=230)

root.mainloop()
