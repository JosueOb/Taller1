from tkinter import *

root = Tk()
etiqueta1= Label(root, text="DEBER DE PROGRAMACION BRYAN PILATUÑA")
etiqueta1.config(bg='BLUE',font=('times', 16, 'italic'))
etiqueta1.pack()

mensaje = " MULTIPLICACION DE DOS NUMEROS QUEMADOS"
msg = Message(root, text = mensaje)
msg.config(bg='lightBLUE',font=('times', 16, 'italic'))
msg.pack( )
mensaje1 = " VARIABLE1=  \n5"
msg = Message(root, text = mensaje1)
msg.config(bg='lightBLUE',font=('times', 16, 'italic'))
msg.pack( )
mensaje2 = " VARIABLE2= \n10"
msg = Message(root, text = mensaje2)
msg.config(bg='lightBLUE',font=('times', 16, 'italic'))
msg.pack( )
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="FIN",fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,text="MULTIPLICACION",fg="red",command=self.write_slogan)
        self.slogan.pack(side=RIGHT)
    def write_slogan(self):
        mensaje = " MULTIPLICACION= \n 50"
        msg = Message(root, text = mensaje)
        msg.config(bg='lightBLUE',font=('times', 16, 'italic'))
        msg.pack( )

root = Tk()
app = App(root)
root.mainloop()


root.mainloop()
