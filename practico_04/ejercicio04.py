## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

from tkinter import *
from tkinter import ttk
from enum import Enum


# Creación de la ventana raíz.
root = Tk()
root.configure(background="white")
root.title("Lista de Ciudades")
root.geometry("200x300")
root.resizable(False, False)
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(root))


class Opciones(Enum):
    ALTA = 1
    BAJA = 2
    MODIFICACION = 3


def closeWindow(window):
    window.destroy()
    window.quit()


def createControls():
    global treeView
    treeView = ttk.Treeview(root, show="tree")
    treeView.pack(fill="both", expand=True)
    global firstItem
    firstItem = treeView.insert("", END, text="Ciudades")

    btnAlta = Button(
        root,
        text="Alta",
        bg="white",
        command=lambda: newWindow(None, Opciones.ALTA),
        height=1,
        width=8,
    ).pack(side=LEFT, expand=True)

    btnBaja = Button(
        root,
        text="Baja",
        bg="white",
        command=lambda: deleteCity(treeView.focus()),
        height=1,
        width=8,
    ).pack(side=LEFT, expand=True, after=btnAlta)

    btnModificar = Button(
        root,
        text="Modificar",
        bg="white",
        command=lambda: newWindow(treeView.focus(), Opciones.MODIFICACION),
        height=1,
        width=8,
    ).pack(side=LEFT, expand=True, after=btnBaja)


def newWindow(item, opcion):
    if item != '' and item != firstItem:
        root.withdraw()
        win = Toplevel()
        win.configure(background="white")
        win.title("Ciudad")
        win.geometry("240x100")
        win.resizable(False, False)
        win.geometry(
            "+{}+{}".format(
                int(win.winfo_screenwidth() / 2 - win.winfo_reqwidth() / 2),
                int(win.winfo_screenheight() / 2 - win.winfo_reqheight() / 2),
            )
        )

        nombreCiudad = StringVar()
        codigoPostal = StringVar()

        itemCiudad = [""]
        itemCP = [""]

        if opcion == Opciones.MODIFICACION:
            obtenerNroItems(item, itemCiudad, itemCP)
            nombreCiudad.set(treeView.item(itemCiudad)["text"])
            codigoPostal.set(treeView.item(itemCP)["text"])

        lblCiudad = Label(win, text="Nombre Ciudad", bg="white").grid(
            sticky=W + N + S, column=0, row=0, padx=5, pady=5
        )
        txtCiudad = Entry(win, textvariable=nombreCiudad, bg="white").grid(
            sticky=E + N + S, column=1, columnspan=2, row=0, padx=5, pady=5
        )
        lblCodigoPostal = Label(win, text="Código Postal", bg="white").grid(
            sticky=W + N + S, column=0, row=1, padx=5, pady=5
        )
        txtCodigoPostal = Entry(win, textvariable=codigoPostal, bg="white").grid(
            sticky=E + N + S, column=1, columnspan=2, row=1, padx=5, pady=5
        )
        bntAceptar = Button(
            win,
            text="Aceptar",
            bg="white",
            command=lambda: aceptar(opcion),
            height=1,
            width=5,
        ).grid(column=1, row=2, padx=5, pady=5, sticky=W + E + N + S)
        btnCancelar = Button(
            win,
            text="Cancelar",
            bg="white",
            command=lambda: cancelar(),
            height=1,
            width=5,
        ).grid(column=2, row=2, padx=5, pady=5, sticky=W + E + N + S)

    def aceptar(opcion):
        if opcion == Opciones.ALTA:
            createCity(nombreCiudad.get(), codigoPostal.get())
        else:
            updateCity(itemCiudad, itemCP, nombreCiudad.get(), codigoPostal.get())
        win.destroy()
        root.deiconify()

    def cancelar():
        win.destroy()
        root.deiconify()


def obtenerNroItems(item, itemCiudad, itemCP):
    if treeView.parent(item) == firstItem:
        itemCiudad[0] = item
        itemCP[0] = treeView.get_children(item)[0]
    else:
        itemCiudad[0] = treeView.parent(item)
        itemCP[0] = item


def createCity(nombreCiudad, codigoPostal):
    subitem = treeView.insert(firstItem, END, text=nombreCiudad)
    treeView.insert(subitem, END, text=codigoPostal)


def updateCity(itemCiudad, itemCP, nombreCiudad, codigoPostal):
    treeView.item(itemCiudad, text=nombreCiudad)
    treeView.item(itemCP, text=codigoPostal)


def deleteCity(item):
    if item != '' and item != firstItem:
        itemCiudad = [""]
        itemCP = [""]
        obtenerNroItems(item, itemCiudad, itemCP)
        treeView.delete(itemCP)
        treeView.delete(itemCiudad)


if __name__ == "__main__":
    createControls()
    root.mainloop()
