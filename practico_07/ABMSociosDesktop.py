from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio
from tkinter import *
from tkinter import ttk

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
    Button(frame_buttons, text="Crear", width=10, anchor="center", padx=5, command="callback").grid(row=0,column=0)
    Button(frame_buttons, text="Modificar", width=10, anchor="center", padx=5, command="callback").grid(row=0,column=1)
    Button(frame_buttons, text="Eliminar", width=10, anchor="center", padx=5, command=delete_socio).grid(row=0,column=2)
    Button(frame_buttons, text="Actualizar", width=10, anchor="center", padx=5, command=add_data_to_table).grid(row=0,column=3)

def delete_socio():
       ns = NegocioSocio()
       global id_socio_seleccionado
       ns.baja(id_socio_seleccionado.get())

if __name__ == "__main__":
    create_controls()
    root.mainloop()