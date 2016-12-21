#Programa de Widgets Tkinter.py
#Autor:Toasa Lizeth
#Fecha:20-Dic-2016

from tkinter import *

v1 = Tk()
v1.title("Widgets")
##v1.geometry("300x300")
v1.configure(bg = "Misty Rose")
v2 = Toplevel(v1)
v2.resizable(0,0)
#v1.protocol("WM_DELETE_WINDOW", "onexit")

#funciones
def mostrar(ventana):ventana.deiconify()
def ocultar(ventana):ventana.withdraw()
def ejecutar(f):v1.after(200,f)

#widgets
boton1 = Button(v1, text="Abrir Ventana",bg="Deep Pink",
                font = "Batang 10 bold",
                command=lambda:ejecutar(mostrar(v2)))

boton2 = Button(v1, text="Ocultar Ventana",bg="orange",
                font = "Batang 10 bold",
                command=lambda:ejecutar(ocultar(v2)))

#et1: el nombre
nombre = Label(v2,text="Nombre:",bg="Peach Puff",relief=RIDGE,borderwidth=2.5)
nombre_str=StringVar()
nombre_entry = Entry(v2,text=nombre_str)

#et2: el apellido
apellido = Label(v2,text="Apellido:",bg="Lavender",relief=RIDGE,borderwidth=2.5)
apellido_str=StringVar()
apellido_entry = Entry(v2,text=apellido_str)

#et3: la edad
edad = Label(v2,text="Edad:",bg="Azure",relief=RIDGE,borderwidth=2.5)
edad_str=StringVar()
edad_entry = Entry(v2,text=edad_str)

#et4: la direccion
direccion = Label(v2,text="Direccion:",bg="Seashell",relief=RIDGE,borderwidth=2.5)
direccion_str=StringVar()
direccion_entry = Entry(v2,text=direccion_str)

#et5: el email
mail = Label(v2,text="Email:",bg="Lemon Chiffon",relief=RIDGE,borderwidth=2.5)
mail_str=StringVar()
mail_entry = Entry(v2,text=mail_str)

#et6: terminar
finish = Button(v2,text="Finalizar",font = "Batang 10 bold",
                relief=SOLID,command = v2.destroy)


boton1.grid(row=1,column=1)
boton2.grid(row=1,column=3)
nombre.grid(row=1,column=1)
nombre_entry.grid(row=1,column=2)
apellido.grid(row=2,column=1)
apellido_entry.grid(row=2,column=2)
edad.grid(row=3,column=1)
edad_entry.grid(row=3,column=2)
direccion.grid(row=4,column=1)
direccion_entry.grid(row=4,column=2)
mail.grid(row=5,column=1)
mail_entry.grid(row=5,column=2)
finish.grid(row=6,column=2)

v2.geometry("200x200")
v2.title("Formulario")
v2.configure(bg = "Light Cyan")
v2.withdraw()
v1.mainloop()
