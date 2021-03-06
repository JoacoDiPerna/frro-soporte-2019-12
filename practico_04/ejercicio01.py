## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *
from tkinter import messagebox
from math import *
from enum import Enum

# Definición de la aplicación Tkinter.
root = Tk()
root.configure(background="white")
root.title("Calculadora")
root.geometry("295x100")
root.resizable(False, False)
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(root))

# Variables de entrada.
valor1 = IntVar()
valor2 = IntVar()

# Variable de salida.
resultado = StringVar()


class Opciones(Enum):
    SUMA = 1
    RESTA = 2
    DIVISION = 3
    MULTIPLICACION = 4


def closeWindow(window):
    window.destroy()
    window.quit()


def createControls():
    # Widgets de entrada.
    lblValor1 = Label(root, text="Primer valor", bg="white").place(x=5, y=10)
    txtValor1 = Entry(root, textvariable=valor1, bg="light grey").place(x=100, y=10)
    lblValor2 = Label(root, text="Segundo valor", bg="white").place(x=5, y=40)
    txtValor2 = Entry(root, textvariable=valor2, bg="light grey").place(x=100, y=40)

    # Widgets de salida
    lblResultado = Label(
        root, text="Resultado: ", background="white", font=("arial", 10, "bold")
    ).place(x=5, y=70)
    txtResultado = Label(root, textvariable=resultado, background="white").place(
        x=100, y=70
    )

    # Botones.
    Button(
        root,
        text=" + ",
        bg="white",
        command=lambda: resul(Opciones.SUMA.value),
        height=1,
        width=2,
    ).place(x=230, y=6)

    Button(
        root,
        text=" - ",
        bg="white",
        command=lambda: resul(Opciones.RESTA.value),
        height=1,
        width=2,
    ).place(x=260, y=6)

    Button(
        root,
        text=" / ",
        bg="white",
        command=lambda: resul(Opciones.DIVISION.value),
        height=1,
        width=2,
    ).place(x=230, y=34)

    Button(
        root,
        text=" x ",
        bg="white",
        command=lambda: resul(Opciones.MULTIPLICACION.value),
        height=1,
        width=2,
    ).place(x=260, y=34)


# Resultado operación.
def resul(op):
    try:
        auxRes = ""
        x = valor1.get()
        y = valor2.get()
        if op == Opciones.SUMA.value:
            auxRes = "%s + %s = %s" % (x, y, x + y)
        elif op == Opciones.RESTA.value:
            auxRes = "%s - %s = %s" % (x, y, x - y)
        elif op == Opciones.DIVISION.value:
            try:
                auxRes = "%s / %s = %s" % (x, y, x / y)
            except:
                auxRes = "Error"
        elif op == Opciones.MULTIPLICACION.value:
            auxRes = "%s * %s = %s" % (x, y, x * y)
        resultado.set(auxRes)
    except:
        messagebox.showerror(
            "Error", "Se ha producido un error al realizar la operación."
        )
        resultado.set("")


if __name__ == "__main__":
    createControls()
    root.mainloop()
