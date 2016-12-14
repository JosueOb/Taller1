from tkinter import *

root = Tk()
etiqueta1= Label(root, text="Bienvenido a mi programa")
etiqueta1.config(bg='yellow',font=('times', 12, 'italic'))
etiqueta1.pack()

mensaje = "Integrantes: \nKatherine Montoya\nLizeth Toasa\nJosue Cando\nBryan Pilatuña"
msg = Message(root, text = mensaje)
msg.config(bg='lightgreen',font=('times', 12, 'italic'))
msg.pack( )

v = IntVar()
v.set(1)
e1 = Entry(root)
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
def ShowChoice():
    print (v.get())
Label(root, text="""Selecciona tu lenguaje favorito""",
          justify = LEFT,
          padx = 20).pack()
for txt, val in languages:
        Radiobutton(root,
                    text=txt,
                    padx = 30,
                    variable=v,
                    command=ShowChoice,
                    value=val).pack(anchor=W)



etiqueta2= Label(root, text="Selecciono")
etiqueta2.pack
e1.pack()


root.mainloop()
