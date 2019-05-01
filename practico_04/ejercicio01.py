## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import *


def clear_widget_text(widget):
    widget['text'] = ""


def resul(op):
    Label(app, text='                                                ',background='light grey').place(x=100, y=147)
    x = var1.get()
    y = var2.get()
    if op == 1:
        Label(app, text='%s + %s = %s' % (x, y, x+y),background='light grey').place(x=100, y=147)
    elif op == 2:
        Label(app, text='%s - %s = %s' % (x, y, x-y),background='light grey').place(x=100, y=147)
    elif op == 3:
        try:
            Label(app, text='%s / %s = %s' % (x, y, x/y),background='light grey').place(x=100, y=147)
        except:
            Label(app, text='ERROR',background='light grey').place(x=100, y=147)
    elif op == 4:
        Label(app, text='%s * %s = %s' % (x, y, x*y),background='light grey').place(x=100, y=147)
    return 0

app = Tk()
app.configure(background="white")
app.title("Calculadora")
app.geometry("270x200")

#variable de entrada
var1 = IntVar()
var2 = IntVar()


# Text box de entrada
lbl1 = Label(app, text= 'Primer valor').place(x=5, y=5)
txtbx1 = Entry(app, textvariable=var1,bg='light grey').place(x=100, y=5)
lbl2 = Label(app, text= 'Segundo valor').place(x=5, y=30)
txtbx2 = Entry(app, textvariable=var2,bg='light grey').place(x=100, y=32)


# Text box de salida
lbl3 = Label(app, text= 'Resultado: ').place(x=5, y=147)
#txtbox_resul = Entry(app, textvariable=resultado,bg='light grey').place(x=100, y=150)

Button(app, text=' + ', bg='white',command= lambda: resul(1), width=5).place(x=5, y=85)

Button(app, text=' - ', bg='white',command= lambda: resul(2), height=1, width=5).place(x=65, y=85)

Button(app, text=' / ', bg='white',command=lambda: resul(3), height=1, width=5).place(x=120, y=85)

Button(app, text=' x ', bg='white',command=lambda: resul(4), height=1, width=5).place(x=175, y=85)

app.mainloop()
