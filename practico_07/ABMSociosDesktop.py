from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio
from tkinter import *
from tkinter import ttk
from enum import Enum

# Creación de la ventana raíz.
root = Tk()
root.configure(background="white")
root.title("Gestión de socios")
root.geometry("550x500")
root.resizable(False, False)
# Creación del frame.
frame_grid = Frame(root)
frame_grid.grid(column=0, row=0, padx=(10,10), pady=(1,1))
frame_buttons = Frame(root, width=52)
frame_buttons.grid(column=0, row=1, padx=(10,10), pady=(1,1))
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: close_window(root))

class Opciones(Enum):
    ALTA = 1
    BAJA = 2
    MODIFICACION = 3

id_socio_seleccionado = IntVar()

def close_window(window):
    window.destroy()
    window.quit()

def create_controls():
    get_socios()    

def get_socios():
    add_data_to_table()

def add_data_to_table():
    delete_frame_grid_controls()
    ns = NegocioSocio()
    global socios
    global id_socio_seleccionado
    socios = ns.todos()
    cont = 0
    Label(frame_grid,text="", width=4, anchor="center", relief="ridge", font=("Helvetica", 12,)).grid(row=cont,column=0)
    Label(frame_grid,text="DNI", width=10, anchor="center", relief="ridge", font=("Helvetica", 12,)).grid(row=cont,column=1)
    Label(frame_grid,text="Nombre", width=20, anchor="center", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=2)
    Label(frame_grid,text="Apellido", width=20, anchor="center", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=3)
    cont +=1
    for socio in socios:
        Radiobutton(frame_grid, width=2, anchor="center", bg="white", relief="ridge", variable=id_socio_seleccionado, value=socio.id_socio).grid(row=cont,column=0)
        Label(frame_grid,text=socio.dni, width=10, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=1)
        Label(frame_grid,text=socio.nombre, width=20, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=2)
        Label(frame_grid,text=socio.apellido, width=20, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=3)   
        cont +=1     
    create_buttons(cont)

def delete_frame_grid_controls():
    list = frame_grid.grid_slaves()
    for l in list:
        l.destroy()

def create_buttons(cont):
    Button(frame_buttons, text="Crear", width=10, anchor="center", padx=5, command=lambda:add_or_update_socio(Opciones.ALTA)).grid(row=0,column=0)
    Button(frame_buttons, text="Modificar", width=10, anchor="center", padx=5, command=lambda:add_or_update_socio(Opciones.MODIFICACION)).grid(row=0,column=1)
    Button(frame_buttons, text="Eliminar", width=10, anchor="center", padx=5, command=delete_socio).grid(row=0,column=2)
    Button(frame_buttons, text="Actualizar", width=10, anchor="center", padx=5, command=add_data_to_table).grid(row=0,column=3)

def add_or_update_socio(opcion):
    win = Toplevel()
    win.configure(background="white")
    win.geometry("240x130")
    win.resizable(False, False)
    win.geometry(
        "+{}+{}".format(
            int(win.winfo_screenwidth() / 2 - win.winfo_reqwidth() / 2),
            int(win.winfo_screenheight() / 2 - win.winfo_reqheight() / 2),
        )
    )

    def aceptar(opcion):
        if opcion == Opciones.ALTA:
            add_socio(dni_socio.get(), nombre_socio.get(), apellido_socio.get())
        else:
            update_socio(socio, dni_socio.get(), nombre_socio.get(), apellido_socio.get())
        win.destroy()
        add_data_to_table()
        root.deiconify()

    def cancelar():
        win.destroy()
        root.deiconify()

    dni_socio = IntVar()
    nombre_socio= StringVar()
    apellido_socio = StringVar()

    if opcion == Opciones.MODIFICACION:
        ns = NegocioSocio()
        socio = ns.buscar(id_socio_seleccionado.get())
        if socio == None:
            cancelar()
        win.title("Modificar socio")
        dni_socio.set(socio.dni)
        nombre_socio.set(socio.nombre)
        apellido_socio.set(socio.apellido)
    elif opcion == Opciones.ALTA:
        win.title("Crear socio")        

    Label(win, text="DNI", bg="white").grid(
        sticky=W + N + S, column=0, row=0, padx=5, pady=5
    )
    Entry(win, textvariable=dni_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=0, padx=5, pady=5
    )
    Label(win, text="Nombre", bg="white").grid(
        sticky=W + N + S, column=0, row=1, padx=5, pady=5
    )
    Entry(win, textvariable=nombre_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=1, padx=5, pady=5
    )
    Label(win, text="Apellido", bg="white").grid(
        sticky=W + N + S, column=0, row=2, padx=5, pady=5
    )
    Entry(win, textvariable=apellido_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=2, padx=5, pady=5
    )
    Button(
        win,
        text="Aceptar",
        bg="white",
        command=lambda: aceptar(opcion),
        height=1,
        width=5,
    ).grid(column=1, row=3, padx=5, pady=5, sticky=W + E + N + S)
    Button(
        win,
        text="Cancelar",
        bg="white",
        command=lambda: cancelar(),
        height=1,
        width=5,
    ).grid(column=2, row=3, padx=5, pady=5, sticky=W + E + N + S)

def add_socio(dni, nombre, apellido):
    socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
    ns = NegocioSocio()
    ns.alta(socio)

def update_socio(socio, dni, nombre, apellido):
    socio.dni = dni
    socio.nombre = nombre
    socio.apellido = apellido
    ns = NegocioSocio()
    ns.modificacion(socio)

def delete_socio():
       ns = NegocioSocio()
       global id_socio_seleccionado
       ns.baja(id_socio_seleccionado.get())
       add_data_to_table()

if __name__ == "__main__":
    create_controls()
    root.mainloop()