
# Creación de varios botones con funciones
# Autor: Katherine Montoya
# Fecha: 20-12-2016

from tkinter import *

class Application(Frame):
    def saludo(self):
        print("Bienvenido!!")

    def numeros(self):
        for i in range (10):
            print (i)

    def vocales(self):
        for i in ("a e i o u"):
            print (i)

    def crearWidgets(self):
        self.SALIR = Button(self)
        self.SALIR["text"] = "SALIR"
        self.SALIR["fg"]   = "red"
        self.SALIR["bg"] = "black"
        self.SALIR["font"] = "Arial 30 bold"
        self.SALIR["command"] =  self.quit

        self.SALIR.pack({"side": "left"})

        self.hola = Button(self)
        self.hola["text"] = "HOLA",
        self.hola["fg"] = "blue"
        self.hola["bg"] = "black"
        self.hola["font"] = "Arial 30 bold"
        self.hola["command"] = self.saludo
        
        self.hola.pack({"side": "left"})

        self.num = Button(self)
        self.num["text"] = "NUMEROS",
        self.num["fg"] = "purple"
        self.num["bg"] = "black"
        self.num["font"] = "Arial 25 bold"
        self.num["command"] = self.numeros
        
        self.num.pack({"side": "top"})

        self.vocal = Button(self)
        self.vocal["text"] = "VOCALES",
        self.vocal["fg"] = "yellow"
        self.vocal["bg"] = "black"
        self.vocal["font"] = "Arial 25 bold"
        self.vocal["command"] = self.vocales
        
        self.vocal.pack({"side": "bottom"})

        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.crearWidgets()

v1 = Tk()
v1.geometry("600x200")
v1.title ("Mi Ventana")
v1.configure(bg='skyblue')
app = Application(master=v1)
app.mainloop()
v1.destroy()

