
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
        self.txt0.place(x=250,y=30,width=120,height=40)

        self.txt1=tk.Label(self.frame,text="Matricula : ",bg="sky blue")
        self.txt1.place(x=40,y=110,width=100,height=40)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=250,y=110,width=120,height=40)

        self.txt2=tk.Label(self.frame,text="Nombre : ",bg="sky blue")
        self.txt2.place(x=40,y=170,width=100,height=40)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=250,y=170,width=120,height=40)

        self.txt3=tk.Label(self.frame,text="Apellidos : ",bg="sky blue")
        self.txt3.place(x=40,y=230,width=100,height=40)

        self.caja3=tk.Entry(self.frame)
        self.caja3.place(x=250,y=230,width=120,height=40)

        self.txt4=tk.Label(self.frame,text="Edad : ",bg="sky blue")
        self.txt4.place(x=40,y=290,width=100,height=40)

        self.caja4=tk.Entry(self.frame)
        self.caja4.place(x=250,y=290,width=120,height=40)

        self.txt5=tk.Label(self.frame,text="Telefono : ",bg="sky blue")
        self.txt5.place(x=40,y=350,width=100,height=40)

        self.caja5=tk.Entry(self.frame)
        self.caja5.place(x=250,y=350,width=120,height=40)

        self.txt6=tk.Label(self.frame,text="Domicilio : ",bg="sky blue")
        self.txt6.place(x=40,y=410,width=100,height=40)

        self.caja6=tk.Entry(self.frame)
        self.caja6.place(x=250,y=410,width=120,height=40)

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
        clave=(self.caja1.get() )
        nombre=(self.caja2.get())
        apellido=(self.caja3.get())
        edad=(self.caja4.get())
        telefono=(self.caja5.get())
        domicilio=(self.caja6.get())
        contador=0
        
   
        try:
            clave1=int(clave)
            edad1=int(edad)
            telefono1=int(telefono)

            if len(nombre)==0 or nombre.isdigit():
                x="z"+1

            if len(apellido)==0 or apellido.isdigit():
                x="z"+1

            if len(domicilio)==0 or domicilio.isdigit():
                x="z"+1

            try:
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS registro (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL,edad INTEGER NOT NULL,telefono INTEGER NOT null,domicilio TEXT NOT NULL );")
                    valores={"clave":clave1,"nombre":nombre,"apellido":apellido,"edad":edad1,"telefono":telefono1,"domicilio":domicilio}
                    c.execute("INSERT INTO registro VALUES (:clave,:nombre,:apellido,:edad,:telefono,:domicilio)",valores)
                lista=[]
                lista.append(clave)
                lista.append(nombre)
                lista.append(apellido)
                lista.append(edad)
                lista.append(telefono)
                lista.append(domicilio)
                self.ventana=tk.Tk()
                self.ventana.title("Registro Datos : ")
                self.ventana.geometry("500x500")
                self.txt00=tk.Label(self.ventana,text="Registro Completado Satisfactoriamente: ",bg="peach puff")
                self.txt00.place(x=120,y=20,width=250,height=40)

                self.txt01=tk.Label(self.ventana,text="Datos del Empleado : ",bg="peach puff")
                self.txt01.place(x=120,y=80,width=250,height=40)

                self.txt02=tk.Label(self.ventana,text="Matricula : ",bg="peach puff")
                self.txt02.place(x=30,y=140,width=100,height=30)

                self.txt03=tk.Label(self.ventana,text="Nombre : ",bg="peach puff")
                self.txt03.place(x=30,y=190,width=100,height=30)

                self.txt04=tk.Label(self.ventana,text="Apellidos : ",bg="peach puff")
                self.txt04.place(x=30,y=240,width=100,height=30)

                self.txt04=tk.Label(self.ventana,text="Edad : ",bg="peach puff")
                self.txt04.place(x=30,y=290,width=100,height=30)

                self.txt04=tk.Label(self.ventana,text="Telefono : ",bg="peach puff")
                self.txt04.place(x=30,y=340,width=100,height=30)

                self.txt04=tk.Label(self.ventana,text="Domicilio : ",bg="peach puff")
                self.txt04.place(x=30,y=390,width=100,height=30)

                lugar=140
                for elemento in lista:
                    self.txt02=tk.Label(self.ventana,text=elemento,bg="peach puff")
                    self.txt02.place(x=200,y=lugar,width=100,height=30)
                    lugar=lugar+50
                self.ventana.mainloop()
                    
            except Error as e:
                self.ventana2=tk.Tk()
                self.ventana2.title("Error: ")
                self.ventana2.geometry("500x250")
                self.txt00=tk.Label(self.ventana2,text="No se pudo registrar el registro: ",bg="peach puff")
                self.txt00.place(x=150,y=20,width=200,height=40)

                self.txt01=tk.Label(self.ventana2,text="Motivos: ",bg="peach puff")
                self.txt01.place(x=150,y=80,width=200,height=40)

                self.txt02=tk.Label(self.ventana2,text=" - Clave Repetida ",bg="peach puff")
                self.txt02.place(x=150,y=150,width=200,height=50)
        except:

            self.ventana3=tk.Tk()
            self.ventana3.title("Error: ")
            self.ventana3.geometry("500x250")
            self.txt00=tk.Label(self.ventana3,text="No se pudo registrar el registro: ",bg="peach puff")
            self.txt00.place(x=150,y=20,width=200,height=40)

            self.txt01=tk.Label(self.ventana3,text="Motivos: ",bg="peach puff")
            self.txt01.place(x=150,y=80,width=200,height=40)

            self.txt02=tk.Label(self.ventana3,text="- Introdujo valores no permitidos\n - No llenaste todos los datos ",bg="peach puff")
            self.txt02.place(x=150,y=150,width=200,height=50)
            

        
        
            
        

    def Borrar(self):
        pass

    def Checar(self):
        pass

app=Aplicacion()
