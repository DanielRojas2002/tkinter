
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

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ")
        self.txt0.place(x=250,y=30,width=100,height=30)
        self.txt1=tk.Label(self.ventana,text="Nombre : ",bg="yellow")
        self.txt1.place(x=40,y=100,width=100,height=30)
        self.ventana.mainloop()

app=Aplicacion()
