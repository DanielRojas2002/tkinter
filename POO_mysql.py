
import sys 
import datetime
import tkinter as tk

class Aplicacion():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Registro de Empleados : ")
        self.ventana.geometry("600x600")

        self.frame=tk.Frame(self.ventana,bg="lightblue")
        self.frame.pack(expand=True,fill="both")
        self.frame.config(cursor="pirate")
        

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ")
        self.txt0.place(x=250,y=30,width=100,height=40)

        self.txt1=tk.Label(self.frame,text="Matricula : ",bg="yellow")
        self.txt1.place(x=40,y=110,width=100,height=40)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=250,y=110,width=100,height=40)

        self.txt2=tk.Label(self.frame,text="Nombre : ",bg="yellow")
        self.txt2.place(x=40,y=170,width=100,height=40)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=250,y=170,width=100,height=40)

        self.txt3=tk.Label(self.frame,text="Apellidos : ",bg="yellow")
        self.txt3.place(x=40,y=230,width=100,height=40)

        self.caja3=tk.Entry(self.frame)
        self.caja3.place(x=250,y=230,width=100,height=40)

        self.txt4=tk.Label(self.frame,text="Edad : ",bg="yellow")
        self.txt4.place(x=40,y=290,width=100,height=40)

        self.caja4=tk.Entry(self.frame)
        self.caja4.place(x=250,y=290,width=100,height=40)

        self.txt5=tk.Label(self.frame,text="Telefono : ",bg="yellow")
        self.txt5.place(x=40,y=350,width=100,height=40)

        self.caja5=tk.Entry(self.frame)
        self.caja5.place(x=250,y=350,width=100,height=40)

        self.ventana.mainloop()

app=Aplicacion()
