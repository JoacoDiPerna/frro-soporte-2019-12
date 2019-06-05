## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import *
from tkinter import messagebox

root = Tk()
root.configure(background="white")
root.title("Calculadora")
root.geometry("210x170")
root.resizable(False, False)
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(root))

frame = Frame(root, relief=FLAT, background="white")
frame.grid(column=0, row=0, padx=5, pady=5)

# variable de entrada
resultado = StringVar()


def closeWindow(window):
    window.destroy()
    window.quit()


def createControls():
    txtResultado = Entry(
        frame, textvariable=resultado, bg="white", state="disabled"
    ).grid(column=0, columnspan=3, row=0, padx=0, pady=0)

    btnCE = Button(
        frame, text="CE", bg="white", command=borrar, height=1, width=5
    ).grid(column=3, row=0, padx=3, pady=3)

    btnNum1 = Button(
        frame, text=" 1 ", bg="white", command=lambda: concatenar(1), height=1, width=5
    ).grid(column=0, row=1, padx=3, pady=3)

    btnNum2 = Button(
        frame, text=" 2 ", bg="white", command=lambda: concatenar(2), height=1, width=5
    ).grid(column=1, row=1, padx=3, pady=3)

    btnNum3 = Button(
        frame, text=" 3 ", bg="white", command=lambda: concatenar(3), height=1, width=5
    ).grid(column=2, row=1, padx=3, pady=3)

    btnSuma = Button(
        frame,
        text=" + ",
        bg="white",
        command=lambda: concatenar("+"),
        height=1,
        width=5,
    ).grid(column=3, row=1, padx=3, pady=3)

    btnNum4 = Button(
        frame, text=" 4 ", bg="white", command=lambda: concatenar(4), height=1, width=5
    ).grid(column=0, row=2, padx=3, pady=3)

    btnNum5 = Button(
        frame, text=" 5 ", bg="white", command=lambda: concatenar(5), height=1, width=5
    ).grid(column=1, row=2, padx=3, pady=3)

    btnNum6 = Button(
        frame, text=" 6 ", bg="white", command=lambda: concatenar(6), height=1, width=5
    ).grid(column=2, row=2, padx=3, pady=3)

    btnResta = Button(
        frame,
        text=" - ",
        bg="white",
        command=lambda: concatenar("-"),
        height=1,
        width=5,
    ).grid(column=3, row=2, padx=3, pady=3)

    btnNum7 = Button(
        frame, text=" 7 ", bg="white", command=lambda: concatenar(7), height=1, width=5
    ).grid(column=0, row=3, padx=3, pady=3)

    btnNum8 = Button(
        frame, text=" 8 ", bg="white", command=lambda: concatenar(8), height=1, width=5
    ).grid(column=1, row=3, padx=3, pady=3)

    btnNum9 = Button(
        frame, text=" 9 ", bg="white", command=lambda: concatenar(9), height=1, width=5
    ).grid(column=2, row=3, padx=3, pady=3)

    btnDivide = Button(
        frame,
        text=" / ",
        bg="white",
        command=lambda: concatenar("/"),
        height=1,
        width=5,
    ).grid(column=3, row=3, padx=3, pady=3)

    btnDot = Button(
        frame, text=". ", bg="white", command=lambda: concatenar("."), height=1, width=5
    ).grid(column=0, row=4, padx=3, pady=3)

    btnNum0 = Button(
        frame, text=" 0 ", bg="white", command=lambda: concatenar(0), height=1, width=5
    ).grid(column=1, row=4, padx=3, pady=3)

    btnIgual = Button(
        frame, text=" = ", bg="white", command=error, height=1, width=5
    ).grid(column=2, row=4, padx=3, pady=3)

    btnMultiplica = Button(
        frame,
        text=" x ",
        bg="white",
        command=lambda: concatenar("*"),
        height=1,
        width=5,
    ).grid(column=3, row=4, padx=3, pady=3)


def concatenar(num):
    resultado.set(resultado.get() + str(num))


# Borrar datos de entrada del text box
def borrar():
    resultado.set("")


# Calculo del total y manejo de error.
def error():
    try:
        resultado.set(str(eval(resultado.get())))
    except:
        messagebox.showerror(
            "Error", "Se ha producido un error al realizar la operación."
        )
        resultado.set("")


if __name__ == "__main__":
    createControls()
    root.mainloop()
