
import sys 
import datetime
import tkinter as tk
import sqlite3
from sqlite3 import Error

class Aplicacion():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Registro de Empleados : ")
        self.ventana.geometry("600x600")

        self.frame=tk.Frame(self.ventana,bg="slate gray")
        self.frame.pack(expand=True,fill="both")
        

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ",bg="peach puff")
        self.txt0.place(x=250,y=30,width=100,height=40)

        self.txt1=tk.Label(self.frame,text="Matricula : ",bg="sky blue")
        self.txt1.place(x=40,y=110,width=100,height=40)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=250,y=110,width=100,height=40)

        self.txt2=tk.Label(self.frame,text="Nombre : ",bg="sky blue")
        self.txt2.place(x=40,y=170,width=100,height=40)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=250,y=170,width=100,height=40)

        self.txt3=tk.Label(self.frame,text="Apellidos : ",bg="sky blue")
        self.txt3.place(x=40,y=230,width=100,height=40)

        self.caja3=tk.Entry(self.frame)
        self.caja3.place(x=250,y=230,width=100,height=40)

        self.txt4=tk.Label(self.frame,text="Edad : ",bg="sky blue")
        self.txt4.place(x=40,y=290,width=100,height=40)

        self.caja4=tk.Entry(self.frame)
        self.caja4.place(x=250,y=290,width=100,height=40)

        self.txt5=tk.Label(self.frame,text="Telefono : ",bg="sky blue")
        self.txt5.place(x=40,y=350,width=100,height=40)

        self.caja5=tk.Entry(self.frame)
        self.caja5.place(x=250,y=350,width=100,height=40)

        self.txt6=tk.Label(self.frame,text="Domicilio : ",bg="sky blue")
        self.txt6.place(x=40,y=410,width=100,height=40)

        self.caja6=tk.Entry(self.frame)
        self.caja6.place(x=250,y=410,width=100,height=40)

        self.frame2=tk.Frame(self.ventana,bg="deep sky blue")
        self.frame2.place(x=380,y=410,width=230,height=200)
        self.frame2.config(cursor="heart")

        self.boton0=tk.Button(self.frame,text="Borrar Todo",command=self.Borrar_Todo)
        self.boton0.place(x=440,y=360,width=100,height=30)

        self.boton1=tk.Button(self.frame2,text="Registrar",command=self.Registrar)
        self.boton1.place(x=60,y=10,width=100,height=30)

        self.boton2=tk.Button(self.frame2,text="Borrar Registro",command=self.Borrar)
        self.boton2.place(x=60,y=80,width=100,height=30)

        self.boton3=tk.Button(self.frame2,text="Checar Datos",command=self.Checar)
        self.boton3.place(x=60,y=150,width=100,height=30)

        self.ventana.mainloop()



    def Borrar_Todo(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")
        self.caja3.delete(0,"end")
        self.caja4.delete(0,"end")
        self.caja5.delete(0,"end")
        self.caja6.delete(0,"end")

    def Registrar(self):
        try:
            clave=self.caja1.get()
            nombre=self.caja2.get()
            apellido=self.caja3.get()
            edad=self.caja4.get()
            telefono=self.caja5.get()
            domicilio=self.caja6.get()
        except:
            self.Borrar_Todo()
            self.caja1.insert(0,'Llena todos los Datos :)')
            self.caja2.insert(0,'Llena todos los Datos :)')
            self.caja3.insert(0,'Llena todos los Datos :)')
            self.caja4.insert(0,'Llena todos los Datos :)')
            self.caja5.insert(0,'Llena todos los Datos :)')
            self.caja6.insert(0,'Llena todos los Datos :)')
            
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS registro (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL,edad INTEGER NOT NULL,telefono INTEGER NOT null,domicilio TEXT NOT NULL );")
                valores={"clave":clave,"nombre":nombre,"apellido":apellido,"edad":edad,"telefono":telefono,"domicilio":domicilio}
                c.execute("INSERT INTO registro VALUES (:clave,:nombre,:apellido,:edad,:telefono,:domicilio)",valores)
                
        except Error as e:
            print("-"*30)
            print(f"ERROR :{e}")
            print("No se registro el registro")
            print("-"*30)

    def Borrar(self):
        pass

    def Checar(self):
        pass

app=Aplicacion()
