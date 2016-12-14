print("Bryan Pilatuña")
print("Ejercicio 7")
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="Hombre",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master, text="Mujer",variable=var2).grid(row=1,sticky=W)
mainloop()
print ("Ejercicio 8")

from tkinter import *
master = Tk()

def var_states():
    print (" male: ",var1.get())
    print ("Female: ", var2.get())

Label(master, text="Indicar el sexo: ").grid(row=0,sticky=W)
var1 = IntVar()
Checkbutton(master,text="male", variable=var1).grid(row=1,
sticky=W)
var2 = IntVar()
Checkbutton(master, text="Female", variable=var2).grid(row=2,
sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3,
sticky=W, padx=4)
Button(master, text='Show', command=var_states).grid(row=4,
sticky=W,pady=4)
mainloop()
