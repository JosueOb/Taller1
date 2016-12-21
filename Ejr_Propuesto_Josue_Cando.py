# EJERCICIO PROPUESTO
# Autor: Josué Ricardo Cando Obaco
# Fecha: 20-12-2016
# Versión 1.2


from tkinter import *
#from tkinter import messagebox
lista = []
ventana = Tk()
ventana.title("Ejercicio Porpuesto")
ventana.geometry("425x305")
ventana.configure(background="black")

def insertar():
    elemento = nombre.get()
    elemento2 =apellido.get()
    if elemento != "" and elemento2 !="":
        lista.append(elemento+" "+elemento2)
        imprimir()
        textnomb.set("")
        textapel.set("")
    else:
        messagebox.showinfo("Error","Falta llenar un campo")

def eliminar():
    if len(lista) != 0:
        lista.pop()
        imprimir()
    else:
        messagebox.showinfo("Error","No hay nada que eliminar")

def imprimir():
    listado=Text(ventana,width=25,height=15)
    listado.place(x=200,y=50)
    listado.insert(INSERT,"\tREGISTRO\n")
    for elemento in lista:
        listado.insert(INSERT,elemento+"\n")
    
Label(ventana,text="Ejercicio Tkinter",bg ="black",fg="white",font =("Ravie",15)).place(x=85,y=10)
Label(ventana,text="Nombre",bg="skyblue",fg="white").place(x=0,y=80)
Label(ventana,text="Apellido",bg="skyblue",fg="white").place(x=0,y=110)

textnomb = StringVar()
textapel = StringVar()

nombre=Entry(ventana,text=textnomb)
apellido=Entry(ventana,text=textapel)

nombre.place(x=60,y=80)
apellido.place(x=60,y=110)

Button(ventana,text="Insertar",command=insertar,bg="skyblue",fg="white").place(x=30,y=150)
Button(ventana,text="Eliminar",command=eliminar,bg="red",fg="white").place(x=100,y=150)

imprimir() 
mainloop()

    
