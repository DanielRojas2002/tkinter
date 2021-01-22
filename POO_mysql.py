
import sys 
import datetime
import tkinter as tk

class Aplicacion():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Registro de Empleados : ")
        self.ventana.geometry("600x600")

        self.frame=tk.Frame(self.ventana,bg="DarkOliveGreen3")
        self.frame.pack(expand=True,fill="both")
        

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ",bg="olivedrab2")
        self.txt0.place(x=250,y=30,width=100,height=40)

        self.txt1=tk.Label(self.frame,text="Matricula : ",bg="gold3")
        self.txt1.place(x=40,y=110,width=100,height=40)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=250,y=110,width=100,height=40)

        self.txt2=tk.Label(self.frame,text="Nombre : ",bg="yellow")
        self.txt2.place(x=40,y=170,width=100,height=40)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=250,y=170,width=100,height=40)

        self.txt3=tk.Label(self.frame,text="Apellidos : ",bg="gold3")
        self.txt3.place(x=40,y=230,width=100,height=40)

        self.caja3=tk.Entry(self.frame)
        self.caja3.place(x=250,y=230,width=100,height=40)

        self.txt4=tk.Label(self.frame,text="Edad : ",bg="yellow")
        self.txt4.place(x=40,y=290,width=100,height=40)

        self.caja4=tk.Entry(self.frame)
        self.caja4.place(x=250,y=290,width=100,height=40)

        self.txt5=tk.Label(self.frame,text="Telefono : ",bg="gold3")
        self.txt5.place(x=40,y=350,width=100,height=40)

        self.caja5=tk.Entry(self.frame)
        self.caja5.place(x=250,y=350,width=100,height=40)

        self.txt6=tk.Label(self.frame,text="Domicilio : ",bg="yellow")
        self.txt6.place(x=40,y=410,width=100,height=40)

        self.caja6=tk.Entry(self.frame)
        self.caja6.place(x=250,y=410,width=100,height=40)

        self.frame2=tk.Frame(self.ventana,bg="chartreuse3")
        self.frame2.place(x=380,y=410,width=230,height=200)
        self.frame2.config(cursor="heart")

        self.boton1=tk.Button(self.frame2,text="Registrar",command=self.Registrar)
        self.boton1.place(x=60,y=10,width=100,height=30)

        self.boton2=tk.Button(self.frame2,text="Borrar Registro",command=self.Borrar)
        self.boton2.place(x=60,y=80,width=100,height=30)

        self.boton3=tk.Button(self.frame2,text="Checar Datos",command=self.Checar)
        self.boton3.place(x=60,y=150,width=100,height=30)

        self.ventana.mainloop()



    def Registrar(self):
        pass

    def Borrar(self):
        pass

    def Checar(self):
        pass

app=Aplicacion()
