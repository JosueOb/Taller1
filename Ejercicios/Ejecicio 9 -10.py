from tkinter import*
master = Tk()
master.title("Ejercicio 9")
master1 =Tk()
master1.title("Ejercicio 10")
## Ejercicio 9
Label(master, text="Nombre").grid(row=0)
Label(master, text="Apellido").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
##mainloop( )

## Ejercicio 10
def nombre():
    print("Primer Nombre: %s\nSegundo Nombre: %s" % (e1.get(),e2.get()))
    print("Primer Nombre:" )
Label(master1,text = "Nombre").grid(row=0)
Label(master1,text = "Apellido").grid(row=1)
e1 = Entry(master1)
e2 = Entry(master1)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(master1,text="Salir",command = master.destroy).grid(row=3,column=0,sticky=W,pady=4)
Button(master1,text="Imprimir",command =nombre).grid(row=3,column=1,sticky=W,pady=4)

mainloop()
