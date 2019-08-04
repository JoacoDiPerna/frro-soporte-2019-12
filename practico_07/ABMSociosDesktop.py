from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida
from tkinter import *
from enum import Enum


# Creación de la ventana raíz.
root = Tk()
root.configure(background="white")
root.title("Gestión de socios")
root.geometry("600x400")
root.resizable(False, False)
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: close_window(root))

def close_window(window):
    window.destroy()
    window.quit()

def create_controls():
    create_tree_view()

def create_tree_view():
    tree = Treeview(root, columns=('dni', 'nombre', 'apellido'))
    tree.column('dni', width=100, anchor='center')
    tree.heading('dni', text='DNI')
    tree.column('nombre', width=100, anchor='center')
    tree.heading('nombre', text='Nombre')
    tree.column('apellido', width=100, anchor='center')
    tree.heading('apellido', text='Apellido')

if __name__ == "__main__":
    create_controls()
    root.mainloop()