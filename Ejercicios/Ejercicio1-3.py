#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS

#Integrantes: Josue Cando-Katherine Montoya-Bryan Pilatuña-Lizeth Toasa
#Fecha:14/12/2016

from tkinter import *

#EJERCICIO 1
root = Tk()
etiqueta1= Label(root, text="Hello Tkinter!")
etiqueta1.pack()
root.mainloop()

#EJERCICIO 2
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen',font=('times', 24, 'italic'))
msg.pack( )
mainloop( )

#EJERCICIO 3
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SALIR",
fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,text="ENTRAR",command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        print ("Estamos aprendiendo a usar Tkinter!")

root = Tk()
app = App(root)
root.mainloop()

