## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

from tkinter import *
from tkinter import ttk

app = Tk()
app.configure(background="white")
app.title("Lista de Ciudades")
app.geometry("200x300")
app.resizable(False, False)


def createControls():
    treeView = ttk.Treeview(app, show="tree")
    treeView.pack(fill="both", expand=True)
    item = treeView.insert("", END, text="Ciudades")
    subitem = treeView.insert(item, END, text="Armstrong")
    treeView.insert(subitem, END, text="CP 2508")
    subitem = treeView.insert(item, END, text="Buenos Aires")
    treeView.insert(subitem, END, text="CP 1000")
    subitem = treeView.insert(item, END, text="Córdoba")
    treeView.insert(subitem, END, text="CP 5000")
    subitem = treeView.insert(item, END, text="La Plata")
    treeView.insert(subitem, END, text="CP 1900")
    subitem = treeView.insert(item, END, text="Mar del Plata")
    treeView.insert(subitem, END, text="CP 7600")
    subitem = treeView.insert(item, END, text="Rosario")
    treeView.insert(subitem, END, text="CP 2000")


if __name__ == "__main__":
    createControls()
    app.mainloop()
