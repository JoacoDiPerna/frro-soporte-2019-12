## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *

concatenacion = ""

def concatenar(num):
    global concatenacion
    concatenacion = concatenacion + str(num)
    calculo.set(concatenacion)


# calculo del total y manejo de error
def error():
    try:
        global concatenacion
        total = str(eval(concatenacion))
        calculo.set(total)
        concatenacion = ""
    except:
        calculo.set(" error ")
        concatenacion = ""


# Borrar datos de entrada del text box
def borrar():
    global concatenacion
    concatenacion = ""
    calculo.set("")


if __name__ == "__main__":
    #Configuración de la ventana
    app = Tk()
    app.configure(background="white")
    app.title("Calculadora")
    app.geometry("270x200")

    #variable de entrada
    calculo = StringVar()

    # Text box de entrada
    txtbox_concat = Entry(app, textvariable=calculo,bg='light grey')
    txtbox_concat.grid(columnspan=4, ipadx=70,padx=2, pady=5)


    # botones
    btn1 = Button(app, text=' 1 ', bg='white',command=lambda: concatenar(1), height=1, width=5)
    btn1.grid(row=3, column=0,padx=5, pady=5)

    btn2 = Button(app, text=' 2 ', bg='white',command=lambda: concatenar(2), height=1, width=5)
    btn2.grid(row=3, column=1,padx=5, pady=5)

    btn3 = Button(app, text=' 3 ', bg='white',command=lambda: concatenar(3), height=1, width=5)
    btn3.grid(row=3, column=2,padx=5, pady=5)

    btn4 = Button(app, text=' 4 ', bg='white',command=lambda: concatenar(4), height=1, width=5)
    btn4.grid(row=5, column=0,padx=5, pady=5)

    btn5 = Button(app, text=' 5 ', bg='white',command=lambda: concatenar(5), height=1, width=5)
    btn5.grid(row=5, column=1,padx=5, pady=5)

    btn6 = Button(app, text=' 6 ', bg='white',command=lambda: concatenar(6), height=1, width=5)
    btn6.grid(row=5, column=2,padx=5, pady=5)

    btn7 = Button(app, text=' 7 ', bg='white',command=lambda: concatenar(7), height=1, width=5)
    btn7.grid(row=7, column=0,padx=5, pady=5)

    btn8 = Button(app, text=' 8 ', bg='white',command=lambda: concatenar(8), height=1, width=5)
    btn8.grid(row=7, column=1,padx=5, pady=5)

    btn9 = Button(app, text=' 9 ', bg='white',command=lambda: concatenar(9), height=1, width=5)
    btn9.grid(row=7, column=2,padx=5, pady=5)

    button0 = Button(app, text=' 0 ', bg='white',command=lambda: concatenar(0), height=1, width=5)
    button0.grid(row=9, column=0,padx=5, pady=5)

    suma = Button(app, text=' + ', bg='white',command=lambda: concatenar("+"), height=1, width=5)
    suma.grid(row=3, column=3,padx=5, pady=5)

    resta = Button(app, text=' - ', bg='white',command=lambda: concatenar("-"), height=1, width=5)
    resta.grid(row=5, column=3,padx=5, pady=5)

    divide = Button(app, text=' / ', bg='white',command=lambda: concatenar("/"), height=1, width=5)
    divide.grid(row=7, column=3,padx=5, pady=5)

    multip = Button(app, text=' x ', bg='white',command=lambda: concatenar("*"), height=1, width=5)
    multip.grid(row=9, column=3,padx=5, pady=5)

    igual = Button(app, text=' = ', bg='white',command=error, height=1, width=5)
    igual.grid(row=9, column=1,padx=5, pady=5)

    borrar = Button(app, text='CE', bg='white',command=borrar, height=1, width=5)
    borrar.grid(row=9, column=2,padx=5, pady=5)

    app.mainloop()
