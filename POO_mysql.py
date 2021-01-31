
import sys 
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

import pandas as pd
import os

import matplotlib.pyplot as plt 

from tabulate import tabulate
class Aplicacion():
    def __init__(self):

        self.ventanai=tk.Tk()
        self.ancho_ventana = 600
        self.alto_ventana = 600

        self.x_ventana = self.ventanai.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventanai.geometry(self.posicion)
        self.ventanai.title("BIENVENIDO AL GESTOR DE EMPLEADOS : ")
        self.ventanai.geometry("600x600")
        self.ventanai.maxsize(600, 600)
        self.ventanai.minsize(600, 600)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.ventanai.iconbitmap("icono.ico")

        self.frame=tk.Frame(self.ventanai,bg="slate gray")
        self.frame.pack(expand=True,fill="both")

        self.framee=tk.Frame(self.ventanai,bg="royal blue")
        self.framee.place(x=0,y=0,width=600,height=120)

        self.txt0101=tk.Label(self.framee,text="GESTOR DE EMPLEADOS",background="gold",font=self.fontStyle)
        self.txt0101.place(x=40,y=10,width=500,height=100)

    
        self.image=tk.PhotoImage(file="base.gif")
        self.txt=tk.Label(image=self.image)
        self.txt.place(x=85,y=150)


        self.frame2=tk.Frame(self.ventanai,bg="deep sky blue")
        self.frame2.place(x=0,y=480,width=600,height=130)
        self.frame2.config(cursor="hand1")

        self.botonAlta=tk.Button(self.frame2,text="ALTA",command=self.Alta,bd=5)
        self.botonAlta.place(x=10,y=20,width=100,height=30)

        self.boton2=tk.Button(self.frame2,text="BAJA",command=self.Borrar_Registro,bd=5)
        self.boton2.place(x=10,y=70,width=100,height=30)

        self.boton3=tk.Button(self.frame2,text="MODIFICACION",command=self.Modificacion,bd=5)
        self.boton3.place(x=140,y=20,width=100,height=30)

        self.boton4=tk.Button(self.frame2,text="CONSULTA",command=self.Buscar_Registros,bd=5)
        self.boton4.place(x=140,y=70,width=100,height=30)

        self.boton5=tk.Button(self.frame2,text="TXT",command=self.TXT,bd=5)
        self.boton5.place(x=350,y=20,width=100,height=30)

        self.boton6=tk.Button(self.frame2,text="GMAIL",command=self.GMAIL,bd=5)
        self.boton6.place(x=350,y=70,width=100,height=30)

        self.boton7=tk.Button(self.frame2,text="GRAFICAR",command=self.GRAFICAR,bd=5)
        self.boton7.place(x=480,y=20,width=100,height=30)

        self.boton8=tk.Button(self.frame2,text="EXCEL",command=self.excel,bd=5)
        self.boton8.place(x=480,y=70,width=100,height=30)

        self.boton9=tk.Button(self.frame2,text=" + ",command=self.MAS,bd=5,font=self.fontStyle)
        self.boton9.place(x=270,y=30,width=50,height=60)

        self.ventanai.mainloop()



    def MAS(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 200
        self.ventana.iconbitmap("filtro.ico")

        self.x_ventana = self.ventana.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("OPCIONES")
        self.ventana.maxsize(200, 200)
        self.ventana.minsize(200, 200)
        self.ventana.geometry("200x200")

        self.frame=tk.Frame(self.ventana,bg="red2")
        self.frame.pack(expand=True,fill="both")

        self.label=tk.Label(self.frame,text="Filtros",bg="gold2")
        self.label.place(x=50,y=20,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=100)
        self.combo["values"]=("Informacion","Contar Registros","Empiece con ","Termine con ")

        self.boton01=tk.Button(self.frame,text="CHECAR",command=self.CHECAR,bd=5)
        self.boton01.place(x=30,y=160,width=140,height=30)
        self.ventana.mainloop()

    def CHECAR(self):
        if self.combo.get()=="Informacion":
            messagebox.showinfo(message="Para poder ejecutar este programa con todos sus botones tienes que : \n\n *Instalar la libreria tabulate (pip install tabulate (en el cmd)) \n *Tener instalado la base de datos llamada sqlite", title="Cosas Necesarias")
        elif self.combo.get()=="Contar_Registros":
            pass

        elif self.combo.get()=="Contar Registros":
            pass

        elif self.combo.get()=="Empiece con ":
            pass

        elif self.combo.get()=="Termine con ":
            pass




    def TXT(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 200
        self.ventana.iconbitmap("filtro.ico")

        self.x_ventana = self.ventana.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("OPCIONES")
        self.ventana.maxsize(200, 200)
        self.ventana.minsize(200, 200)
        self.ventana.geometry("200x200")

        self.frame=tk.Frame(self.ventana,bg="gray22")
        self.frame.pack(expand=True,fill="both")

        self.label=tk.Label(self.frame,text="Filtros",bg="snow")
        self.label.place(x=50,y=20,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=100)
        self.combo["values"]=("Nombre","Apellido","Edad","Domicilio","Inscripcion","Fecha_Modificacion","Todos")

        self.boton01=tk.Button(self.frame,text="BUSCAR",command=self.BUSCAR,bd=5)
        self.boton01.place(x=30,y=160,width=140,height=30)
        self.ventana.mainloop()


    def titulo(self):
        archivoA=open("C:\\comun\\Reporte.txt" , 'a')
        self.datos=[]
        self.datos2=[]
        self.datos.append(self.datos2)
        self.datos2.append("ID")
        self.datos2.append("NOMBRE")
        self.datos2.append("APELLIDO")
        self.datos2.append("EDAD")
        self.datos2.append("TELEFONO")
        self.datos2.append("DOMICILIO")
        self.datos2.append("INSCRIPCION")
        self.datos2.append("ULTIMA_MODIFICACION")
        archivoA.close()

    def BUSCAR(self):
        if self.combo.get()=="Nombre":
            self.ventana5=tk.Tk()
            self.ventana5.title("TXT : ")
            self.ventana5.iconbitmap("txt.ico")
            self.ancho_ventana = 300
            self.alto_ventana = 300

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Nombre: : ",bg="snow")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A TXT",command=self.NOMBRETXT,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()

        elif self.combo.get()=="Apellido":
            self.ventana5=tk.Tk()
            self.ventana5.title("TXT : ")
            self.ventana5.iconbitmap("txt.ico")
            self.ancho_ventana = 300
            self.alto_ventana = 300

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Apellido : ",bg="snow")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A TXT",command=self.APELLIDOTXT,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()
        
        elif self.combo.get()=="Edad":
            self.ventana5=tk.Tk()
            self.ventana5.title("TXT : ")
            self.ventana5.iconbitmap("txt.ico")
            self.ancho_ventana = 300
            self.alto_ventana = 300

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Edad : ",bg="snow")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A TXT",command=self.EDADTXT,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()
        
        elif self.combo.get()=="Domicilio":
            self.ventana5=tk.Tk()
            self.ventana5.title("TXT : ")
            self.ventana5.iconbitmap("txt.ico")
            self.ancho_ventana = 300
            self.alto_ventana = 300

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Domicilio : ",bg="snow")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A TXT",command=self.DOMICILIOTXT,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()

        elif self.combo.get()=="Inscripcion":
            self.ventana5=tk.Tk()
            self.ventana5.title("EXCEL : ")
            self.ventana5.iconbitmap("excel.ico")
            self.ancho_ventana = 600
            self.alto_ventana = 200

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("600x200")
            self.ventana5.maxsize(600, 200)
            self.ventana5.minsize(600, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Inscripcion: : ",bg="medium spring green")
            self.txt001.place(x=250,y=10,width=100,height=30)


            self.txt001=tk.Label(self.frame4,text="DIA : ",bg="snow")
            self.txt001.place(x=50,y=50,width=100,height=30)

            self.cajadia=tk.Entry(self.frame4)
            self.cajadia.place(x=50,y=90,width=100,height=30)

            self.txt001=tk.Label(self.frame4,text="MES : ",bg="snow")
            self.txt001.place(x=250,y=50,width=100,height=30)

            self.cajames=tk.Entry(self.frame4)
            self.cajames.place(x=250,y=90,width=100,height=30)

            self.txt001=tk.Label(self.frame4,text="AÑO : ",bg="snow")
            self.txt001.place(x=450,y=50,width=100,height=30)

            self.cajaaño=tk.Entry(self.frame4)
            self.cajaaño.place(x=450,y=90,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.INSCRIPCIONTXT,bd=5)
            self.boton11.place(x=245,y=150,width=120,height=30)
            self.ventana5.mainloop()

        elif self.combo.get()=="Fecha_Modificacion":
            self.ventana5=tk.Tk()
            self.ventana5.title("TXT : ")
            self.ventana5.iconbitmap("excel.ico")
            self.ancho_ventana = 600
            self.alto_ventana = 200

            self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("600x200")
            self.ventana5.maxsize(600, 200)
            self.ventana5.minsize(600, 200)

            self.frame4=tk.Frame(self.ventana5,bg="gray22")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Fecha_Modificacion : ",bg="medium spring green")
            self.txt001.place(x=230,y=10,width=140,height=30)


            self.txt001=tk.Label(self.frame4,text="DIA : ",bg="snow")
            self.txt001.place(x=50,y=50,width=100,height=30)

            self.cajadia=tk.Entry(self.frame4)
            self.cajadia.place(x=50,y=90,width=100,height=30)

            self.txt001=tk.Label(self.frame4,text="MES : ",bg="snow")
            self.txt001.place(x=250,y=50,width=100,height=30)

            self.cajames=tk.Entry(self.frame4)
            self.cajames.place(x=250,y=90,width=100,height=30)

            self.txt001=tk.Label(self.frame4,text="AÑO : ",bg="snow")
            self.txt001.place(x=450,y=50,width=100,height=30)

            self.cajaaño=tk.Entry(self.frame4)
            self.cajaaño.place(x=450,y=90,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="PASARLO A TXT",command=self.FECHA_MODIFICACIONTXT,bd=5)
            self.boton11.place(x=245,y=150,width=120,height=30)
            self.ventana5.mainloop()
        
        elif self.combo.get()=="Todos":
            try:
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT * FROM registro ")
                    registros=c.fetchall()

                    self.titulo()
                    archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"TODOS los Registros :"+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        self.datos.append(conjunto)
                    archivoA.write(tabulate(self.datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    self.datos=[]
                    messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")

            except:
                print("No creo que pase ")



    def NOMBRETXT(self):
        try:
            contador=0
            nom=str(self.caja000.get())
            nombre=nom.capitalize()
        
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"nombre":nombre}
                c.execute("SELECT * FROM registro WHERE nombre = :nombre" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                
                else:
                    self.titulo()
                    archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"Nombre : "+str(nombre)+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        self.datos.append(conjunto)
                    archivoA.write(tabulate(self.datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    self.datos=[]
                    messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")
        except:
            print("ERROR")


    def APELLIDOTXT(self):
        try:
            contador=0
            ape=str(self.caja000.get())
            apellido=ape.capitalize()
        
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"apellido":apellido}
                c.execute("SELECT * FROM registro WHERE apellido = :apellido" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                
                else:
                    self.titulo()
                    archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"Apellido : "+str(apellido)+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        self.datos.append(conjunto)
                    archivoA.write(tabulate(self.datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    self.datos=[]
                    messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")
        except:
            print("ERROR")


        


    def EDADTXT(self):
        try:
            contador=0
            edad=int(self.caja000.get())
        
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"edad":edad}
                c.execute("SELECT * FROM registro WHERE edad = :edad" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")
                
                else:
                    self.titulo()
                    archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"Edad : "+str(edad)+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        self.datos.append(conjunto)
                    archivoA.write(tabulate(self.datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    self.datos=[]
                    messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")
        except:
            messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")
        

    def DOMICILIOTXT(self):
        try:
            contador=0
            dom=str(self.caja000.get())
            domicilio=dom.capitalize()
        
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"domicilio":domicilio}
                c.execute("SELECT * FROM registro WHERE domicilio = :domicilio" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                
                else:
                    self.titulo()
                    archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"Domcilio : "+str(domicilio)+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        self.datos.append(conjunto)
                    archivoA.write(tabulate(self.datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    self.datos=[]
                    messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")
        except:
            print("ERROR")
        

    def INSCRIPCIONTXT(self):
        try:
            contador=0
            dia=self.cajadia.get()
            mes=self.cajames.get()
            año=self.cajaaño.get()
            d=int(dia)
            m=int(mes)
            a=int(año)
            
            if len(dia)!=2:
                x="kk"+2

            if len(mes)!=2:
                x="kk"+2

            if len(año)!=4:
                x="kk"+2

            try:
                inscripcion=(dia+"/"+mes+"/"+año)
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    valor={"inscripcion":inscripcion}
                    c.execute("SELECT * FROM registro WHERE inscripcion = :inscripcion" , valor)
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro ",title="ERROR")

                    else:
                        self.titulo()
                        archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                        archivoA.write("\n")
                        archivoA.write("-"*20+"Buscado por : "+"Inscripcion : "+str(inscripcion)+"-"*20)
                        archivoA.write("\n")
                        for conjunto in registros:
                            self.datos.append(conjunto)
                        archivoA.write(tabulate(self.datos))
                        archivoA.write("\n")
                        archivoA.write("-"*100)
                        archivoA.close()
                        self.datos=[]
                        messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")

            except:
                messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")
        except:
            messagebox.showerror(message="Ingreso mal el dia,mes o año",title="ERROR")
            

    def FECHA_MODIFICACIONTXT(self):
        try:
            contador=0
            dia=self.cajadia.get()
            mes=self.cajames.get()
            año=self.cajaaño.get()
            d=int(dia)
            m=int(mes)
            a=int(año)
            
            if len(dia)!=2:
                x="kk"+2

            if len(mes)!=2:
                x="kk"+2

            if len(año)!=4:
                x="kk"+2

            try:
                fecha_Modificacion=(dia+"/"+mes+"/"+año)
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    valor={"fecha_Modificacion":fecha_Modificacion}
                    c.execute("SELECT * FROM registro WHERE fecha_Modificacion = :fecha_Modificacion" , valor)
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro ",title="ERROR")

                    else:
                        self.titulo()
                        archivoA=open("C:\\comun\\Reporte.txt" , 'a')
                        archivoA.write("\n")
                        archivoA.write("-"*20+"Buscado por : "+"Fecha_Modificacion : "+str(fecha_Modificacion)+"-"*20)
                        archivoA.write("\n")
                        for conjunto in registros:
                            self.datos.append(conjunto)
                        archivoA.write(tabulate(self.datos))
                        archivoA.write("\n")
                        archivoA.write("-"*100)
                        archivoA.close()
                        self.datos=[]
                        messagebox.showinfo(message="Su Archivo TXT fue generado en C:comun",title=":)")

            except:
                messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")
        except:
            messagebox.showerror(message="Ingreso mal el dia,mes o año",title="ERROR")

        
        

    def GMAIL(self):
        pass

    def GRAFICAR(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 200
        self.ventana.iconbitmap("filtro.ico")

        self.x_ventana = self.ventana.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("OPCIONES")
        self.ventana.maxsize(200, 200)
        self.ventana.minsize(200, 200)
        self.ventana.geometry("200x200")

        self.frame=tk.Frame(self.ventana,bg="gray22")
        self.frame.pack(expand=True,fill="both")

        self.label=tk.Label(self.frame,text="Filtros",bg="snow")
        self.label.place(x=50,y=20,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=100)
        self.combo["values"]=("Nombre","Apellido","Edad","Domicilio")

        self.boton01=tk.Button(self.frame,text="BUSCAR",command=self.BUSCAR2,bd=5)
        self.boton01.place(x=30,y=160,width=140,height=30)
        self.ventana.mainloop()

    def BUSCAR2(self):
        contador=0
        listaNom=[]
        if self.combo.get()=="Nombre":
            try:
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT distinct (nombre) from registro")
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                    
                    else:
                        for elemento in registros:
                            for x in elemento:
                                listaNom.append(x)

            except:
                print("sss")

            try:
                listaContador=[]
                for x in listaNom:
                    with sqlite3.connect("Empleados.db") as conn:
                        c = conn.cursor()
                        nombre=str(x)
                        valor={"nombre":nombre}
                        c.execute("SELECT count(nombre) from registro WHERE nombre = :nombre", valor)
                        registros=c.fetchall()

                    for elemento in registros:
                            for x in elemento:
                                listaContador.append(x)

                
            except Error as e:
                print(e)
            plt.pie(listaContador,labels=listaNom,autopct="%0.1f %%")
            plt.title("NOMBRES : ")
            plt.show()

        elif self.combo.get()=="Apellido":
            try:
                contador=0
                listaNom=[]
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT distinct (apellido) from registro")
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                    
                    else:
                        for elemento in registros:
                            for x in elemento:
                                listaNom.append(x)

            except:
                print("sss")

            try:
                listaContador=[]
                for x in listaNom:
                    with sqlite3.connect("Empleados.db") as conn:
                        c = conn.cursor()
                        apellido=str(x)
                        valor={"apellido":apellido}
                        c.execute("SELECT count(apellido) from registro WHERE apellido = :apellido", valor)
                        registros=c.fetchall()

                    for elemento in registros:
                            for x in elemento:
                                listaContador.append(x)

                
            except Error as e:
                print(e)
            plt.pie(listaContador,labels=listaNom,autopct="%0.1f %%")
            plt.title("APELLIDOS : ")
            plt.show()

        elif self.combo.get()=="Edad":
            try:
                contador=0
                listaNom=[]
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT distinct (edad) from registro")
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                    
                    else:
                        for elemento in registros:
                            for x in elemento:
                                listaNom.append(x)

            except:
                print("sss")

            try:
                listaContador=[]
                for x in listaNom:
                    with sqlite3.connect("Empleados.db") as conn:
                        c = conn.cursor()
                        edad=str(x)
                        valor={"edad":edad}
                        c.execute("SELECT count(edad) from registro WHERE edad = :edad", valor)
                        registros=c.fetchall()

                    for elemento in registros:
                            for x in elemento:
                                listaContador.append(x)

                
            except Error as e:
                print(e)
            plt.pie(listaContador,labels=listaNom,autopct="%0.1f %%")
            plt.title("EDAD : ")
            plt.show()
        
        elif self.combo.get()=="Domicilio":
            try:
                contador=0
                listaNom=[]
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT distinct (domicilio) from registro")
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                    
                    else:
                        for elemento in registros:
                            for x in elemento:
                                listaNom.append(x)

            except:
                print("sss")

            try:
                listaContador=[]
                for x in listaNom:
                    with sqlite3.connect("Empleados.db") as conn:
                        c = conn.cursor()
                        domicilio=str(x)
                        valor={"domicilio":domicilio}
                        c.execute("SELECT count(domicilio) from registro WHERE domicilio = :domicilio", valor)
                        registros=c.fetchall()

                    for elemento in registros:
                            for x in elemento:
                                listaContador.append(x)

                
            except Error as e:
                print(e)
            plt.pie(listaContador,labels=listaNom,autopct="%0.1f %%")
            plt.title("DOMICILIO : ")
            plt.show()




        #select distinct (Nombre) from Registros;
    

    def excel(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 300
        self.alto_ventana = 300
        self.ventana.iconbitmap("filtro.ico")

        self.x_ventana = self.ventana.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("OPCIONES")
        self.ventana.maxsize(300, 300)
        self.ventana.minsize(300, 300)
        self.ventana.geometry("300x300")

        self.frame=tk.Frame(self.ventana,bg="springgreen4")
        self.frame.pack(expand=True,fill="both")

        self.label=tk.Label(self.frame,text="Filtros",bg="olivedrab1")
        self.label.place(x=100,y=20,width=100,height=30)

        self.boton01=tk.Button(self.frame,text="Nombre",command=self.NomEx,bd=5)
        self.boton01.place(x=80,y=60,width=140,height=30)

        self.boton02=tk.Button(self.frame,text="Apellido",command=self.ApeEx,bd=5)
        self.boton02.place(x=80,y=100,width=140,height=30)

        self.boton03=tk.Button(self.frame,text="Edad",command=self.EdadEx,bd=5)
        self.boton03.place(x=80,y=140,width=140,height=30)

        self.boton04=tk.Button(self.frame,text="Inscripcion",command=self.InsEx,bd=5)
        self.boton04.place(x=80,y=180,width=140,height=30)

        self.boton05=tk.Button(self.frame,text="Fecha_Modificacion",command=self.FechaEx,bd=5)
        self.boton05.place(x=80,y=220,width=140,height=30)

        self.boton06=tk.Button(self.frame,text="Todos los Registros",command=self.TodoEx,bd=5)
        self.boton06.place(x=80,y=260,width=140,height=30)

        self.ventana.mainloop()

    def NomEx(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("EXCEL : ")
        self.ventana5.iconbitmap("excel.ico")
        self.ancho_ventana = 300
        self.alto_ventana = 300

        self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("200x200")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="springgreen4")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Nombre: : ",bg="olivedrab1")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja000=tk.Entry(self.frame4)
        self.caja000.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.NOMEXCEL,bd=5)
        self.boton11.place(x=40,y=130,width=120,height=30)
        self.ventana5.mainloop()

    def NOMEXCEL(self):
        contador=0
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        nomb=self.caja000.get()
        nombre=nomb.capitalize()
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"nombre":nombre}
                c.execute("SELECT * FROM registro WHERE nombre = :nombre" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                
                else:
                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        listaid.append(clave)
                        listanom.append(nombre)
                        listaape.append(apellido)
                        listaedad.append(edad)
                        listatel.append(telefono)
                        listadom.append(domicilio)
                        listains.append(inscripcion)
                        listamod.append(fecha_Modificacion)
                    diccionariov={}
                    diccionariov["MATRICULA"]=listaid
                    diccionariov["NOMBRE"]=listanom
                    diccionariov["APELLIDO"]=listaape
                    diccionariov["EDAD"]=listaedad
                    diccionariov["TELEFONO"]=listatel
                    diccionariov["DOMICILIO"]=listadom
                    diccionariov["INSCRIPCION"]=listains
                    diccionariov["FECHA_MODIFICACION"]=listamod
                    diccionario2=pd.DataFrame(diccionariov)
                    
                    
                    fecha=datetime.datetime.now()
                    fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                    a="Reporte_"+nombre+"_"+str(fecha2)
                    b=".xlsx"
                    c=a+b
                    ruta = "C:\\comun\\"+c
                    diccionario2.to_excel(ruta, index=None)
                    messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")

        except:
            print("error")

        
    def ApeEx(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("EXCEL : ")
        self.ventana5.iconbitmap("excel.ico")
        self.ancho_ventana = 300
        self.alto_ventana = 300

        self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("200x200")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="springgreen4")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Apellido: : ",bg="olivedrab1")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja0001=tk.Entry(self.frame4)
        self.caja0001.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.APEEXCEL,bd=5)
        self.boton11.place(x=40,y=130,width=120,height=30)
        self.ventana5.mainloop()

    def APEEXCEL(self):
        contador=0
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        ape=self.caja0001.get()
        apellido=ape.capitalize()
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                valor={"apellido":apellido}
                c.execute("SELECT * FROM registro WHERE apellido = :apellido" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \n Ingreso un dato Incorrecto",title="ERROR")
                
                else:
                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        listaid.append(clave)
                        listanom.append(nombre)
                        listaape.append(apellido)
                        listaedad.append(edad)
                        listatel.append(telefono)
                        listadom.append(domicilio)
                        listains.append(inscripcion)
                        listamod.append(fecha_Modificacion)
                    diccionariov={}
                    diccionariov["MATRICULA"]=listaid
                    diccionariov["NOMBRE"]=listanom
                    diccionariov["APELLIDO"]=listaape
                    diccionariov["EDAD"]=listaedad
                    diccionariov["TELEFONO"]=listatel
                    diccionariov["DOMICILIO"]=listadom
                    diccionariov["INSCRIPCION"]=listains
                    diccionariov["FECHA_MODIFICACION"]=listamod
                    diccionario2=pd.DataFrame(diccionariov)
                    
                    
                    fecha=datetime.datetime.now()
                    fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                    a="Reporte_"+apellido+"_"+str(fecha2)
                    b=".xlsx"
                    c=a+b
                    ruta = "C:\\comun\\"+c
                    diccionario2.to_excel(ruta, index=None)
                    messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")

        except:
            print("error")


    def EdadEx(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("EXCEL : ")
        self.ventana5.iconbitmap("excel.ico")
        self.ancho_ventana = 300
        self.alto_ventana = 300

        self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("200x200")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="springgreen4")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Edad: : ",bg="olivedrab1")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja00011=tk.Entry(self.frame4)
        self.caja00011.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.EDADEXCEL,bd=5)
        self.boton11.place(x=40,y=130,width=120,height=30)
        self.ventana5.mainloop()



    def EDADEXCEL(self):
        contador=0
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        eda=self.caja00011.get()
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                edad=int(eda)
                valor={"edad":edad}
                c.execute("SELECT * FROM registro WHERE edad = :edad" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")
                
                else:
                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        listaid.append(clave)
                        listanom.append(nombre)
                        listaape.append(apellido)
                        listaedad.append(edad)
                        listatel.append(telefono)
                        listadom.append(domicilio)
                        listains.append(inscripcion)
                        listamod.append(fecha_Modificacion)
                    diccionariov={}
                    diccionariov["MATRICULA"]=listaid
                    diccionariov["NOMBRE"]=listanom
                    diccionariov["APELLIDO"]=listaape
                    diccionariov["EDAD"]=listaedad
                    diccionariov["TELEFONO"]=listatel
                    diccionariov["DOMICILIO"]=listadom
                    diccionariov["INSCRIPCION"]=listains
                    diccionariov["FECHA_MODIFICACION"]=listamod
                    diccionario2=pd.DataFrame(diccionariov)
                    
                    
                    fecha=datetime.datetime.now()
                    fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                    a="Reporte_"+str(edad)+"_"+str(fecha2)
                    b=".xlsx"
                    c=a+b
                    ruta = "C:\\comun\\"+c
                    diccionario2.to_excel(ruta, index=None)
                    messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")

        except:
             messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")


    def InsEx(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("EXCEL : ")
        self.ventana5.iconbitmap("excel.ico")
        self.ancho_ventana = 600
        self.alto_ventana = 200

        self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("600x200")
        self.ventana5.maxsize(600, 200)
        self.ventana5.minsize(600, 200)

        self.frame4=tk.Frame(self.ventana5,bg="springgreen4")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Inscripcion: : ",bg="medium spring green")
        self.txt001.place(x=250,y=10,width=100,height=30)


        self.txt001=tk.Label(self.frame4,text="DIA : ",bg="olivedrab1")
        self.txt001.place(x=50,y=50,width=100,height=30)

        self.cajadia=tk.Entry(self.frame4)
        self.cajadia.place(x=50,y=90,width=100,height=30)

        self.txt001=tk.Label(self.frame4,text="MES : ",bg="olivedrab1")
        self.txt001.place(x=250,y=50,width=100,height=30)

        self.cajames=tk.Entry(self.frame4)
        self.cajames.place(x=250,y=90,width=100,height=30)

        self.txt001=tk.Label(self.frame4,text="AÑO : ",bg="olivedrab1")
        self.txt001.place(x=450,y=50,width=100,height=30)

        self.cajaaño=tk.Entry(self.frame4)
        self.cajaaño.place(x=450,y=90,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.INCRIPCIONEXCEL,bd=5)
        self.boton11.place(x=245,y=150,width=120,height=30)
        self.ventana5.mainloop()


    def INCRIPCIONEXCEL(self):
        contador=0
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        try:
            dia=self.cajadia.get()
            mes=self.cajames.get()
            año=self.cajaaño.get()
            d=int(dia)
            m=int(mes)
            a=int(año)
            
            if len(dia)!=2:
                x="kk"+2

            if len(mes)!=2:
                x="kk"+2

            if len(año)!=4:
                x="kk"+2

            try:
                inscripcion=(dia+"/"+mes+"/"+año)
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    valor={"inscripcion":inscripcion}
                    c.execute("SELECT * FROM registro WHERE inscripcion = :inscripcion" , valor)
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro ",title="ERROR")
                    
                    else:
                        for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                            listaid.append(clave)
                            listanom.append(nombre)
                            listaape.append(apellido)
                            listaedad.append(edad)
                            listatel.append(telefono)
                            listadom.append(domicilio)
                            listains.append(inscripcion)
                            listamod.append(fecha_Modificacion)
                        diccionariov={}
                        diccionariov["MATRICULA"]=listaid
                        diccionariov["NOMBRE"]=listanom
                        diccionariov["APELLIDO"]=listaape
                        diccionariov["EDAD"]=listaedad
                        diccionariov["TELEFONO"]=listatel
                        diccionariov["DOMICILIO"]=listadom
                        diccionariov["INSCRIPCION"]=listains
                        diccionariov["FECHA_MODIFICACION"]=listamod
                        diccionario2=pd.DataFrame(diccionariov)
                        
                        
                        fecha=datetime.datetime.now()
                        fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                        a="Reporte_"+"fecha"+str(dia)+"_"+str(fecha2)
                        b=".xlsx"
                        c=a+b
                        ruta = "C:\\comun\\"+c
                        diccionario2.to_excel(ruta, index=None)
                        messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")
    
            except:
                messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")

        

        except:
            messagebox.showerror(message="Ingreso mal el dia,mes o año",title="ERROR")

    def FechaEx(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("EXCEL : ")
        self.ventana5.iconbitmap("excel.ico")
        self.ancho_ventana = 600
        self.alto_ventana = 200

        self.x_ventana = self.ventana5.winfo_screenwidth() - 810 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("600x200")
        self.ventana5.maxsize(600, 200)
        self.ventana5.minsize(600, 200)

        self.frame4=tk.Frame(self.ventana5,bg="springgreen4")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Fecha_Modificacion: ",bg="medium spring green")
        self.txt001.place(x=240,y=10,width=120,height=30)


        self.txt001=tk.Label(self.frame4,text="DIA : ",bg="olivedrab1")
        self.txt001.place(x=50,y=50,width=100,height=30)

        self.cajadia2=tk.Entry(self.frame4)
        self.cajadia2.place(x=50,y=90,width=100,height=30)

        self.txt001=tk.Label(self.frame4,text="MES : ",bg="olivedrab1")
        self.txt001.place(x=250,y=50,width=100,height=30)

        self.cajames2=tk.Entry(self.frame4)
        self.cajames2.place(x=250,y=90,width=100,height=30)

        self.txt001=tk.Label(self.frame4,text="AÑO : ",bg="olivedrab1")
        self.txt001.place(x=450,y=50,width=100,height=30)

        self.cajaaño2=tk.Entry(self.frame4)
        self.cajaaño2.place(x=450,y=90,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="PASARLO A EXCEL",command=self.FECHAEX,bd=5)
        self.boton11.place(x=245,y=150,width=120,height=30)
        self.ventana5.mainloop()


    def FECHAEX(self):
        contador=0
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        try:
            dia=self.cajadia2.get()
            mes=self.cajames2.get()
            año=self.cajaaño2.get()
            d=int(dia)
            m=int(mes)
            a=int(año)
            
            if len(dia)!=2:
                x="kk"+2

            if len(mes)!=2:
                x="kk"+2

            if len(año)!=4:
                x="kk"+2

            try:
                Fecha_Modificacion=(dia+"/"+mes+"/"+año)
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    valor={"Fecha_Modificacion":Fecha_Modificacion}
                    c.execute("SELECT * FROM registro WHERE Fecha_Modificacion = :Fecha_Modificacion" , valor)
                    registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        messagebox.showerror(message="No se encontro el Registro ",title="ERROR")
                    
                    else:
                        for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                            listaid.append(clave)
                            listanom.append(nombre)
                            listaape.append(apellido)
                            listaedad.append(edad)
                            listatel.append(telefono)
                            listadom.append(domicilio)
                            listains.append(inscripcion)
                            listamod.append(fecha_Modificacion)
                        diccionariov={}
                        diccionariov["MATRICULA"]=listaid
                        diccionariov["NOMBRE"]=listanom
                        diccionariov["APELLIDO"]=listaape
                        diccionariov["EDAD"]=listaedad
                        diccionariov["TELEFONO"]=listatel
                        diccionariov["DOMICILIO"]=listadom
                        diccionariov["INSCRIPCION"]=listains
                        diccionariov["FECHA_MODIFICACION"]=listamod
                        diccionario2=pd.DataFrame(diccionariov)
                        
                        
                        fecha=datetime.datetime.now()
                        fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                        a="Reporte_"+"fecha"+str(dia)+"_"+str(fecha2)
                        b=".xlsx"
                        c=a+b
                        ruta = "C:\\comun\\"+c
                        diccionario2.to_excel(ruta, index=None)
                        messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")
    
            except:
                messagebox.showerror(message="Ingreso un dato Incorrecto",title="ERROR")

        

        except:
            messagebox.showerror(message="Ingreso mal el dia,mes o año",title="ERROR")
    

    def TodoEx(self):
        listaid=[]
        listanom=[]
        listaape=[]
        listaedad=[]
        listadom=[]
        listatel=[]
        listains=[]
        listamod=[]
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM registro ")
                registros=c.fetchall()

                for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                    listaid.append(clave)
                    listanom.append(nombre)
                    listaape.append(apellido)
                    listaedad.append(edad)
                    listatel.append(telefono)
                    listadom.append(domicilio)
                    listains.append(inscripcion)
                    listamod.append(fecha_Modificacion)
                diccionariov={}
                diccionariov["MATRICULA"]=listaid
                diccionariov["NOMBRE"]=listanom
                diccionariov["APELLIDO"]=listaape
                diccionariov["EDAD"]=listaedad
                diccionariov["TELEFONO"]=listatel
                diccionariov["DOMICILIO"]=listadom
                diccionariov["INSCRIPCION"]=listains
                diccionariov["FECHA_MODIFICACION"]=listamod
                diccionario2=pd.DataFrame(diccionariov)
                
                
                fecha=datetime.datetime.now()
                fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
                a="Reporte_"+"TodosR"+"_"+str(fecha2)
                b=".xlsx"
                c=a+b
                ruta = "C:\\comun\\"+c
                diccionario2.to_excel(ruta, index=None)
                messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")

        except:
            print("error")


    def Alta(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 600
        self.alto_ventana = 600

        self.x_ventana = self.ventanai.winfo_screenwidth() - 310 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("Registro de Empleados : ")
        self.ventana.geometry("600x600")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.maxsize(600, 600)
        self.ventana.minsize(600, 600)

        self.frame=tk.Frame(self.ventana,bg="slate gray")
        self.frame.pack(expand=True,fill="both")
        

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ",bg="gold",font=self.fontStyle)
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
        self.frame2.place(x=380,y=510,width=230,height=100)
        self.frame2.config(cursor="pencil")

        self.boton0=tk.Button(self.frame,text="Borrar Datos",command=self.Borrar_Todo,bd=5)
        self.boton0.place(x=440,y=300,width=100,height=30)

        self.boton1=tk.Button(self.frame2,text="Registrar",command=self.Registrar,bd=5)
        self.boton1.place(x=60,y=30,width=100,height=30)

        

        self.ventana.mainloop()

    def Modificacion(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("Actualizacion : ")
        self.ancho_ventana = 200
        self.alto_ventana = 200

        self.x_ventana = self.ventana5.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)
        self.ventana5.geometry("200x200")
        self.ventana5.iconbitmap("icono.ico")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="steel blue")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="MATRICULA : ",bg="dark turquoise")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja000=tk.Entry(self.frame4)
        self.caja000.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="Checar Dato",command=self.Modificar,bd=5)
        self.boton11.place(x=50,y=130,width=100,height=30)
        self.ventana5.mainloop()

    def Modificar(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                mat=self.caja000.get()
                matricula=int(mat)
                valor={"clave":matricula}
                c.execute("SELECT * FROM registro WHERE clave = :clave" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")

                else:
                    self.ventana6=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana6.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana6.winfo_screenheight() // 2 - self.alto_ventana // 2

                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana6.geometry(self.posicion)
                    self.ventana6.title("Matricula : ")
                    self.ventana6.geometry("790x200")
                    self.ventana6.iconbitmap("icono.ico")
                    self.ventana6.maxsize(790, 200)
                    self.ventana6.minsize(790, 200)

                    self.frame5=tk.Frame(self.ventana6,bg="steel blue")
                    self.frame5.pack(expand=True,fill="both")
                    self.frame5.config(cursor="exchange")

                    
                    self.txt000=tk.Label(self.frame5,text="Matricula",bg="peach puff")
                    self.txt000.place(x=10,y=20,width=80,height=30)

                    self.txt001=tk.Label(self.frame5,text="Nombre",bg="peach puff")
                    self.txt001.place(x=100,y=20,width=80,height=30)

                    self.txt002=tk.Label(self.frame5,text="Apellidos",bg="peach puff")
                    self.txt002.place(x=190,y=20,width=80,height=30)

                    self.txt002=tk.Label(self.frame5,text="Edad",bg="peach puff")
                    self.txt002.place(x=280,y=20,width=80,height=30)

                    self.txt003=tk.Label(self.frame5,text="Telefono",bg="peach puff")
                    self.txt003.place(x=370,y=20,width=80,height=30)

                    self.txt004=tk.Label(self.frame5,text="Domicilio",bg="peach puff")
                    self.txt004.place(x=460,y=20,width=80,height=30)

                    self.txt005=tk.Label(self.frame5,text="Inscripcion",bg="peach puff")
                    self.txt005.place(x=550,y=20,width=80,height=30)

                    self.txt006=tk.Label(self.frame5,text="Ultimo Cambio",bg="peach puff")
                    self.txt006.place(x=640,y=20,width=100,height=30)

                    self.boton01=tk.Button(self.frame5,text="MODIFICAR",command=self.modificar_ya,bd=5)
                    self.boton01.place(x=350,y=150,width=100,height=30)

                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        self.txt002=tk.Label(self.frame5,text=clave,bg="orange")
                        self.txt002.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                        

                        self.txt003=tk.Label(self.frame5,text=nombre,bg="orange")
                        self.txt003.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                       

                        self.txt004=tk.Label(self.frame5,text=apellido,bg="orange")
                        self.txt004.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                     

                        self.txt005=tk.Label(self.frame5,text=edad,bg="orange")
                        self.txt005.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                        

                        self.txt006=tk.Label(self.frame5,text=telefono,bg="orange")
                        self.txt006.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                      

                        self.txt007=tk.Label(self.frame5,text=domicilio,bg="orange")
                        self.txt007.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90

                        self.txt008=tk.Label(self.frame5,text=inscripcion,bg="orange")
                        self.txt008.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90

                        self.txt009=tk.Label(self.frame5,text=fecha_Modificacion,bg="orange")
                        self.txt009.place(x=xl,y=lugar,width=100,height=30)
                        xl=xl+90
                        lugar=lugar+30
                        
                        self.ventana6.mainloop()
        except:
            messagebox.showerror(message="Ingreso un dato incorrecto",title="ERROR")
    
    def modificar_ya(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 600
        self.alto_ventana = 600

        self.x_ventana = self.ventana.winfo_screenwidth() - 1070 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)
        self.ventana.title("Actualizacion del Empleado : ")
        self.ventana.geometry("600x600")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.maxsize(600, 600)
        self.ventana.minsize(600, 600)

        self.frame=tk.Frame(self.ventana,bg="slate gray")
        self.frame.pack(expand=True,fill="both")
        self.frame.config(cursor="exchange")
        

        self.txt0=tk.Label(self.frame,text="EMPLEADO : ",bg="gold",font=self.fontStyle)
        self.txt0.place(x=250,y=30,width=120,height=40)

        self.txt1=tk.Label(self.frame,text="Nombre : ",bg="sky blue")
        self.txt1.place(x=40,y=110,width=100,height=40)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=250,y=110,width=120,height=40)

        self.txt2=tk.Label(self.frame,text="Apellidos :",bg="sky blue")
        self.txt2.place(x=40,y=170,width=100,height=40)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=250,y=170,width=120,height=40)

        self.txt3=tk.Label(self.frame,text="Edad :  ",bg="sky blue")
        self.txt3.place(x=40,y=230,width=100,height=40)

        self.caja3=tk.Entry(self.frame)
        self.caja3.place(x=250,y=230,width=120,height=40)

        self.txt4=tk.Label(self.frame,text="Telefono : ",bg="sky blue")
        self.txt4.place(x=40,y=290,width=100,height=40)

        self.caja4=tk.Entry(self.frame)
        self.caja4.place(x=250,y=290,width=120,height=40)

        self.txt5=tk.Label(self.frame,text="Domicilio : ",bg="sky blue")
        self.txt5.place(x=40,y=350,width=100,height=40)

        self.caja5=tk.Entry(self.frame)
        self.caja5.place(x=250,y=350,width=120,height=40)

        self.boton011=tk.Button(self.frame,text="MODIFICAR",command=self.modificar_yaa,bd=5)
        self.boton011.place(x=400,y=490,width=100,height=30)

        self.ventana.mainloop()
        
    def modificar_yaa(self):
        clave=self.caja000.get()
        nomb=(self.caja1.get())
        nombre=nomb.capitalize()
        apell=(self.caja2.get())
        apellido=apell.capitalize()
        edad=(self.caja3.get())
        telefono=(self.caja4.get())
        domi=(self.caja5.get())
        domicilio=domi.capitalize()
        fecha=datetime.datetime.now()
        fecha_Modificacion=fecha.strftime('%d/%m/%Y')


        try:
            clave1=int(clave)
            edad1=int(edad)
            telefono1=int(telefono)

            if len(edad)>2:
                x="z"+1

            if len(nombre)==0 or nombre.isdigit():
                x="z"+1

            if len(apellido)==0 or apellido.isdigit():
                x="z"+1

            if len(domicilio)==0 or domicilio.isdigit():
                x="z"+1

            
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                tupla=(nombre,apellido,edad1,telefono1,domicilio,fecha_Modificacion,clave1)
                sql="UPDATE registro SET nombre = ?, apellido = ? , edad = ? , telefono = ? , domicilio = ? , fecha_Modificacion = ? WHERE clave = ?;"
                c.execute(sql,tupla)
                messagebox.showinfo(message="EL registro se actualizo Satisfactoriamente",title=":)")

        except:
            messagebox.showerror(message="Ingreso un dato Incorrecto ",title="ERROR")
            

        


    def Borrar_Todo(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")
        self.caja3.delete(0,"end")
        self.caja4.delete(0,"end")
        self.caja5.delete(0,"end")
        self.caja6.delete(0,"end")



    def Registrar(self):
        clave=(self.caja1.get() )
        nombr=(self.caja2.get())
        nombre=nombr.capitalize()
        apell=(self.caja3.get())
        apellido=apell.capitalize()
        edad=(self.caja4.get())
        telefono=(self.caja5.get())
        domicil=(self.caja6.get())
        domicilio=domicil.capitalize()
        contador=0
        
   
        try:
            clave1=int(clave)
            edad1=int(edad)
            telefono1=int(telefono)

            if len(edad)>2:
                x="z"+1

            if len(nombre)==0 or nombre.isdigit():
                x="z"+1

            if len(apellido)==0 or apellido.isdigit():
                x="z"+1

            if len(domicilio)==0 or domicilio.isdigit():
                x="z"+1

            insc=datetime.datetime.now()
            inscripcion=insc.strftime('%d/%m/%Y')
            try:
                with sqlite3.connect("Empleados.db") as conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS registro (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL,edad INTEGER NOT NULL,telefono INTEGER NOT null,domicilio TEXT NOT NULL,inscripcion DATE NOT null,fecha_Modificacion DATE NOT null );")
                    valores={"clave":clave1,"nombre":nombre,"apellido":apellido,"edad":edad1,"telefono":telefono1,"domicilio":domicilio,"inscripcion":inscripcion,"fecha_Modificacion":inscripcion}
                    c.execute("INSERT INTO registro VALUES (:clave,:nombre,:apellido,:edad,:telefono,:domicilio,:inscripcion,:fecha_Modificacion)",valores)
                lista=[]
                lista.append(clave)
                lista.append(nombre)
                lista.append(apellido)
                lista.append(edad)
                lista.append(telefono)
                lista.append(domicilio)
                self.ventana=tk.Tk()
                self.ancho_ventana = 500
                self.alto_ventana = 500

                self.x_ventana = self.ventanai.winfo_screenwidth() - 310 - self.ancho_ventana // 2
                self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

                self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                self.ventana.geometry(self.posicion)

                self.ventana.title("Registro Datos : ")
                self.ventana.geometry("500x500")
                self.ventana.iconbitmap("icono.ico")
                self.ventana.maxsize(500, 500)
                self.ventana.minsize(500, 500)
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
                messagebox.showerror(message="Clave Repetida",title="ERROR")

        except:
            messagebox.showerror(message="Ingreso valores no permitidos o \nNo llenaste todos los datos",title="ERROR")
            

        
        
            
        

    def Borrar_Registro(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("Borrar Registro : ")
        self.ventana5.geometry("200x200")
        self.ancho_ventana = 200
        self.alto_ventana = 200

        self.x_ventana = self.ventana5.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.iconbitmap("icono.ico")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="steel blue")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="MATRICULA A BORRAR : ",bg="dark turquoise")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja000=tk.Entry(self.frame4)
        self.caja000.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="Checar Dato",command=self.ChecarDato,bd=5)
        self.boton11.place(x=50,y=130,width=100,height=30)
        self.ventana5.mainloop()

    def ChecarDato(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                mat=self.caja000.get()
                clave=int(mat)
                valor={"clave":clave}
                c.execute("SELECT * FROM registro WHERE clave = :clave" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")

                else:
                    self.ventana=tk.Tk()
                    self.ancho_ventana = 500
                    self.alto_ventana = 600

                    self.x_ventana = self.ventana.winfo_screenwidth() - 310 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana.geometry(self.posicion)

                    self.ventana.title("DATOS A BORRAR : ")
                    self.ventana.geometry("500x600")
                    self.ventana.iconbitmap("icono.ico")
                    self.ventana.maxsize(500, 600)
                    self.ventana.minsize(500, 600)
                    self.txt00=tk.Label(self.ventana,text="Registro a Borrar: ",bg="peach puff")
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

                    self.txt005=tk.Label(self.ventana,text="Inscripcion",bg="peach puff")
                    self.txt005.place(x=30,y=440,width=100,height=30)

                    self.txt006=tk.Label(self.ventana,text="Ultimo Cambio",bg="peach puff")
                    self.txt006.place(x=30,y=490,width=100,height=30)

                    
                    self.frame=tk.Frame(self.ventana,bg="orange")
                    self.frame.place(x=320,y=530,width=200,height=200)
                    self.frame.config(cursor="X_cursor")

                    self.boton00=tk.Button(self.frame,text="BORRAR",command=self.Borrar_REGISTRO,bd=5)
                    self.boton00.place(x=40,y=20,width=100,height=30)
                    

                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        self.txt002=tk.Label(self.ventana,text=clave,bg="orange")
                        self.txt002.place(x=200,y=140,width=80,height=30)
            
                        
                        self.txt003=tk.Label(self.ventana,text=nombre,bg="orange")
                        self.txt003.place(x=200,y=190,width=80,height=30)
                        
                        

                        self.txt004=tk.Label(self.ventana,text=apellido,bg="orange")
                        self.txt004.place(x=200,y=240,width=80,height=30)
                        
                        

                        self.txt005=tk.Label(self.ventana,text=edad,bg="orange")
                        self.txt005.place(x=200,y=290,width=80,height=30)
                        
                        

                        self.txt006=tk.Label(self.ventana,text=telefono,bg="orange")
                        self.txt006.place(x=200,y=340,width=80,height=30)
                    
                        

                        self.txt007=tk.Label(self.ventana,text=domicilio,bg="orange")
                        self.txt007.place(x=200,y=390,width=80,height=30)

                        self.txt008=tk.Label(self.ventana,text=inscripcion,bg="orange")
                        self.txt008.place(x=200,y=440,width=80,height=30)
                        xl=xl+90

                        self.txt009=tk.Label(self.ventana,text=fecha_Modificacion,bg="orange")
                        self.txt009.place(x=200,y=490,width=80,height=30)
                        xl=xl+90
                        
                        
                    self.ventana.mainloop()

        except:
            messagebox.showerror(message="Ingreso un Dato Incorrecto",title="ERROR")
            


    def Borrar_REGISTRO(self):
        with sqlite3.connect("Empleados.db") as conn:
            c = conn.cursor()
            mat=self.caja000.get()
            clave=int(mat)
            valor={"clave":clave}
            c.execute("DELETE  FROM registro WHERE clave = :clave" , valor)
            conn.commit()

        messagebox.showinfo(message="Registro borrado Satisfactoriamente",title="ERROR")

   
    def Buscar_Registros(self):
        self.ventana4=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana4.winfo_screenwidth() - 1200 - self.ancho_ventana // 2
        self.y_ventana = self.ventana4.winfo_screenheight() - 600 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana4.geometry(self.posicion)

        self.ventana4.title("Buscador : ")
        self.ventana4.geometry("250x350")
        self.ventana4.iconbitmap("filtro.ico")
        self.ventana4.maxsize(250, 350)
        self.ventana4.minsize(250, 350)

        self.frame3=tk.Frame(self.ventana4,bg="steel blue")
        self.frame3.pack(expand=True,fill="both")
        self.frame3.config(cursor="gumby")

        self.txt7=tk.Label(self.frame3,text="Buscar por: ",bg="dark turquoise")
        self.txt7.place(x=60,y=30,width=120,height=30)

        self.boton10=tk.Button(self.frame3,text="Matricula",command=self.BuscMatri,bd=5)
        self.boton10.place(x=70,y=70,width=100,height=30)

        self.boton11=tk.Button(self.frame3,text="Nombre",command=self.BuscNom,bd=5)
        self.boton11.place(x=70,y=110,width=100,height=30)

        self.boton12=tk.Button(self.frame3,text="Apellido",command=self.BuscApe,bd=5)
        self.boton12.place(x=70,y=150,width=100,height=30)

        self.boton13=tk.Button(self.frame3,text="Edad",command=self.BuscEd,bd=5)
        self.boton13.place(x=70,y=190,width=100,height=30)

        self.boton13=tk.Button(self.frame3,text="Telefono",command=self.BuscTel,bd=5)
        self.boton13.place(x=70,y=230,width=100,height=30)

        self.boton13=tk.Button(self.frame3,text="Domicilio",command=self.BuscDom,bd=5)
        self.boton13.place(x=70,y=270,width=100,height=30)

        self.boton13=tk.Button(self.frame3,text="TODOS",command=self.BuscarTodos,bd=5)
        self.boton13.place(x=70,y=310,width=100,height=30)

        self.ventana4.mainloop()

    def BuscMatri(self):
        self.ventana5=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana5.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.title("Buscador por Matricula : ")
        self.ventana5.geometry("150x160")
        self.ventana5.iconbitmap("icono.ico")
        self.ventana5.maxsize(150, 160)
        self.ventana5.minsize(150, 160)

        self.frame4=tk.Frame(self.ventana5,bg="steel blue")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="MATRICULA: ",bg="dark turquoise")
        self.txt001.place(x=20,y=30,width=100,height=30)

        self.caja001=tk.Entry(self.frame4)
        self.caja001.place(x=20,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="Buscar",command=self.BuscarMatricula,bd=5)
        self.boton11.place(x=20,y=120,width=100,height=30)
        self.ventana5.mainloop()

    def BuscarMatricula(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                mat=self.caja001.get()
                matricula=int(mat)
                valor={"clave":matricula}
                c.execute("SELECT * FROM registro WHERE clave = :clave" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")

                else:
                    self.ventana6=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana6.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana6.winfo_screenheight() // 2 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana6.geometry(self.posicion)

                    self.ventana6.title("Matricula : ")
                    self.ventana6.geometry("790x200")
                    self.ventana6.iconbitmap("icono.ico")
                    self.ventana6.maxsize(790, 200)
                    self.ventana6.minsize(790, 200)

                    self.frame5=tk.Frame(self.ventana6,bg="steel blue")
                    self.frame5.pack(expand=True,fill="both")

                    
                    self.txt000=tk.Label(self.frame5,text="Matricula",bg="peach puff")
                    self.txt000.place(x=10,y=20,width=80,height=30)

                    self.txt001=tk.Label(self.frame5,text="Nombre",bg="peach puff")
                    self.txt001.place(x=100,y=20,width=80,height=30)

                    self.txt002=tk.Label(self.frame5,text="Apellidos",bg="peach puff")
                    self.txt002.place(x=190,y=20,width=80,height=30)

                    self.txt002=tk.Label(self.frame5,text="Edad",bg="peach puff")
                    self.txt002.place(x=280,y=20,width=80,height=30)

                    self.txt003=tk.Label(self.frame5,text="Telefono",bg="peach puff")
                    self.txt003.place(x=370,y=20,width=80,height=30)

                    self.txt004=tk.Label(self.frame5,text="Domicilio",bg="peach puff")
                    self.txt004.place(x=460,y=20,width=80,height=30)

                    self.txt005=tk.Label(self.frame5,text="Inscripcion",bg="peach puff")
                    self.txt005.place(x=550,y=20,width=80,height=30)

                    self.txt006=tk.Label(self.frame5,text="Ultimo Cambio",bg="peach puff")
                    self.txt006.place(x=640,y=20,width=100,height=30)

                    for clave,nombre,apellido,edad,telefono,domicilio,inscripcion,fecha_Modificacion in registros:
                        self.txt002=tk.Label(self.frame5,text=clave,bg="orange")
                        self.txt002.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                        

                        self.txt003=tk.Label(self.frame5,text=nombre,bg="orange")
                        self.txt003.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                       

                        self.txt004=tk.Label(self.frame5,text=apellido,bg="orange")
                        self.txt004.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                     

                        self.txt005=tk.Label(self.frame5,text=edad,bg="orange")
                        self.txt005.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                        

                        self.txt006=tk.Label(self.frame5,text=telefono,bg="orange")
                        self.txt006.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90
                      

                        self.txt007=tk.Label(self.frame5,text=domicilio,bg="orange")
                        self.txt007.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90

                        self.txt008=tk.Label(self.frame5,text=inscripcion,bg="orange")
                        self.txt008.place(x=xl,y=lugar,width=80,height=30)
                        xl=xl+90

                        self.txt009=tk.Label(self.frame5,text=fecha_Modificacion,bg="orange")
                        self.txt009.place(x=xl,y=lugar,width=100,height=30)
                        xl=xl+90
                        lugar=lugar+30
                        
                        self.ventana6.mainloop()

        except:
            messagebox.showerror(message="Ingreso un Dato Incorrecto\n o No existen ningun registro ",title="ERROR")


    def BuscNom(self):
        self.ventana7=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana7.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana7.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana7.geometry(self.posicion)

        self.ventana7.title("Buscador por Nombre : ")
        self.ventana7.geometry("150x160")
        self.ventana7.iconbitmap("icono.ico")
        self.ventana7.maxsize(150, 160)
        self.ventana7.minsize(150, 160)

        self.frame7=tk.Frame(self.ventana7,bg="steel blue")
        self.frame7.pack(expand=True,fill="both")

        self.txt77=tk.Label(self.frame7,text="NOMBRE: ",bg="dark turquoise")
        self.txt77.place(x=20,y=30,width=100,height=30)

        self.caja77=tk.Entry(self.frame7)
        self.caja77.place(x=20,y=80,width=100,height=30)

        self.boton77=tk.Button(self.frame7,text="Buscar",command=self.BuscarNombre,bd=5)
        self.boton77.place(x=20,y=120,width=100,height=30)
        self.ventana7.mainloop()


    def BuscarNombre(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                nom=self.caja77.get()
                nomb=str(nom)
                nombre=nomb.capitalize()
                valor={"nombre":nombre}
                c.execute("SELECT * FROM registro WHERE nombre = :nombre" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \nIngreso un dato incorrecto",title="ERROR")

                else:
                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("Matricula : ")
                    self.ventana9.geometry("800x500")
                    self.ventana9.iconbitmap("icono.ico")
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    self.Empleado_Tabla.heading("matricula",text="Matricula")
                    self.Empleado_Tabla.heading("nombre",text="Nombre")
                    self.Empleado_Tabla.heading("apellido",text="Apellido")
                    self.Empleado_Tabla.heading("edad",text="Edad")
                    self.Empleado_Tabla.heading("telefono",text="Telefono")
                    self.Empleado_Tabla.heading("domicilio",text="Domicilio")
                    self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
                    self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
                    self.Empleado_Tabla.pack(fill="both",expand=1)

                    self.Empleado_Tabla['show']='headings'
                    self.Empleado_Tabla.column("matricula",width=100)
                    self.Empleado_Tabla.column("nombre",width=100)
                    self.Empleado_Tabla.column("apellido",width=100)
                    self.Empleado_Tabla.column("edad",width=50)
                    self.Empleado_Tabla.column("telefono",width=90)
                    self.Empleado_Tabla.column("domicilio",width=120)
                    self.Empleado_Tabla.column("inscripcion",width=100)
                    self.Empleado_Tabla.column("fecha_Modificacion",width=120)
                    
    
                    index = iid = 0
                    for elemento in registros:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1
    
                        
                    self.ventana9.mainloop()

        except :
            messagebox.showerror(message="No Existe ningun dato \nLlena la tabla ",title="ERROR")

    def BuscApe(self):
        self.ventana5=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana5.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.title("Buscador por Apellido : ")
        self.ventana5.geometry("150x160")
        self.ventana5.iconbitmap("icono.ico")
        self.ventana5.maxsize(150, 160)
        self.ventana5.minsize(150, 160)

        self.frame4=tk.Frame(self.ventana5,bg="steel blue")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="APELLIDO: ",bg="dark turquoise")
        self.txt001.place(x=20,y=30,width=100,height=30)

        self.caja001=tk.Entry(self.frame4)
        self.caja001.place(x=20,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="Buscar",command=self.BuscarApellido,bd=5)
        self.boton11.place(x=20,y=120,width=100,height=30)
        self.ventana5.mainloop()
    
    def BuscarApellido(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                ape=self.caja001.get()
                apell=str(ape)
                apellido=apell.capitalize()
                valor={"apellido":apellido}
                c.execute("SELECT * FROM registro WHERE apellido = :apellido" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \nIngreso un dato incorrecto",title="ERROR")

                else:
                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("Apellido : ")
                    self.ventana9.geometry("800x500")
                    self.ventana9.iconbitmap("icono.ico")
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    self.Empleado_Tabla.heading("matricula",text="Matricula")
                    self.Empleado_Tabla.heading("nombre",text="Nombre")
                    self.Empleado_Tabla.heading("apellido",text="Apellido")
                    self.Empleado_Tabla.heading("edad",text="Edad")
                    self.Empleado_Tabla.heading("telefono",text="Telefono")
                    self.Empleado_Tabla.heading("domicilio",text="Domicilio")
                    self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
                    self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
                    self.Empleado_Tabla.pack(fill="both",expand=1)

                    self.Empleado_Tabla['show']='headings'
                    self.Empleado_Tabla.column("matricula",width=100)
                    self.Empleado_Tabla.column("nombre",width=100)
                    self.Empleado_Tabla.column("apellido",width=100)
                    self.Empleado_Tabla.column("edad",width=50)
                    self.Empleado_Tabla.column("telefono",width=90)
                    self.Empleado_Tabla.column("domicilio",width=120)
                    self.Empleado_Tabla.column("inscripcion",width=100)
                    self.Empleado_Tabla.column("fecha_Modificacion",width=120)
                    
    
                    index = iid = 0
                    for elemento in registros:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1
    
                        
                    self.ventana9.mainloop()
        except :
            messagebox.showerror(message="No Existe ningun dato \nLlena la tabla ",title="ERROR")
    
    def BuscEd(self):
        self.ventana7=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana7.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana7.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana7.geometry(self.posicion)

        self.ventana7.title("Buscador por Edad : ")
        self.ventana7.geometry("150x160")
        self.ventana7.iconbitmap("icono.ico")
        self.ventana7.maxsize(150, 160)
        self.ventana7.minsize(150, 160)

        self.frame7=tk.Frame(self.ventana7,bg="steel blue")
        self.frame7.pack(expand=True,fill="both")

        self.txt77=tk.Label(self.frame7,text="Edad: ",bg="dark turquoise")
        self.txt77.place(x=20,y=30,width=100,height=30)

        self.caja777=tk.Entry(self.frame7)
        self.caja777.place(x=20,y=80,width=100,height=30)

        self.boton77=tk.Button(self.frame7,text="Buscar",command=self.BuscarEdad,bd=5)
        self.boton77.place(x=20,y=120,width=100,height=30)
        self.ventana7.mainloop()

    def BuscarEdad(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                eda=self.caja777.get()
                edad=int(eda)
                valor={"edad":edad}
                c.execute("SELECT * FROM registro WHERE edad = :edad" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")

                else:
                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("Edad : ")
                    self.ventana9.geometry("800x500")
                    self.ventana9.iconbitmap("icono.ico")
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    self.Empleado_Tabla.heading("matricula",text="Matricula")
                    self.Empleado_Tabla.heading("nombre",text="Nombre")
                    self.Empleado_Tabla.heading("apellido",text="Apellido")
                    self.Empleado_Tabla.heading("edad",text="Edad")
                    self.Empleado_Tabla.heading("telefono",text="Telefono")
                    self.Empleado_Tabla.heading("domicilio",text="Domicilio")
                    self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
                    self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
                    self.Empleado_Tabla.pack(fill="both",expand=1)

                    self.Empleado_Tabla['show']='headings'
                    self.Empleado_Tabla.column("matricula",width=100)
                    self.Empleado_Tabla.column("nombre",width=100)
                    self.Empleado_Tabla.column("apellido",width=100)
                    self.Empleado_Tabla.column("edad",width=50)
                    self.Empleado_Tabla.column("telefono",width=90)
                    self.Empleado_Tabla.column("domicilio",width=120)
                    self.Empleado_Tabla.column("inscripcion",width=100)
                    self.Empleado_Tabla.column("fecha_Modificacion",width=120)
                    
    
                    index = iid = 0
                    for elemento in registros:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1
    
                        
                    self.ventana9.mainloop()
        except :
            messagebox.showerror(message="Ingreso un Dato Incorrecto\n o No existen ningun registro ",title="ERROR")
    
    def BuscTel(self):
        self.ventana7=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana7.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana7.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana7.geometry(self.posicion)

        self.ventana7.title("Buscador por Telefono : ")
        self.ventana7.geometry("150x160")
        self.ventana7.iconbitmap("icono.ico")
        self.ventana7.maxsize(150, 160)
        self.ventana7.minsize(150, 160)

        self.frame7=tk.Frame(self.ventana7,bg="steel blue")
        self.frame7.pack(expand=True,fill="both")

        self.txt77=tk.Label(self.frame7,text="Telefono: ",bg="dark turquoise")
        self.txt77.place(x=20,y=30,width=100,height=30)

        self.caja777=tk.Entry(self.frame7)
        self.caja777.place(x=20,y=80,width=100,height=30)

        self.boton77=tk.Button(self.frame7,text="Buscar",command=self.BuscarTelefono,bd=5)
        self.boton77.place(x=20,y=120,width=100,height=30)
        self.ventana7.mainloop()

    def BuscarTelefono(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                tel=self.caja777.get()
                telefono=int(tel)
                valor={"telefono":telefono}
                c.execute("SELECT * FROM registro WHERE telefono = :telefono" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro",title="ERROR")

                else:
                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("Telefono : ")
                    self.ventana9.geometry("800x500")
                    self.ventana9.iconbitmap("icono.ico")
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    self.Empleado_Tabla.heading("matricula",text="Matricula")
                    self.Empleado_Tabla.heading("nombre",text="Nombre")
                    self.Empleado_Tabla.heading("apellido",text="Apellido")
                    self.Empleado_Tabla.heading("edad",text="Edad")
                    self.Empleado_Tabla.heading("telefono",text="Telefono")
                    self.Empleado_Tabla.heading("domicilio",text="Domicilio")
                    self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
                    self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
                    self.Empleado_Tabla.pack(fill="both",expand=1)

                    self.Empleado_Tabla['show']='headings'
                    self.Empleado_Tabla.column("matricula",width=100)
                    self.Empleado_Tabla.column("nombre",width=100)
                    self.Empleado_Tabla.column("apellido",width=100)
                    self.Empleado_Tabla.column("edad",width=50)
                    self.Empleado_Tabla.column("telefono",width=90)
                    self.Empleado_Tabla.column("domicilio",width=120)
                    self.Empleado_Tabla.column("inscripcion",width=100)
                    self.Empleado_Tabla.column("fecha_Modificacion",width=120)
                    
    
                    index = iid = 0
                    for elemento in registros:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1
    
                        
                    self.ventana9.mainloop()
        except :
            messagebox.showerror(message="Ingreso un Dato Incorrecto\n o No existen ningun registro ",title="ERROR")
    
    def BuscDom(self):
        self.ventana7=tk.Tk()
        self.ancho_ventana = 150
        self.alto_ventana = 160

        self.x_ventana = self.ventana7.winfo_screenwidth() - 850 - self.ancho_ventana // 2
        self.y_ventana = self.ventana7.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana7.geometry(self.posicion)

        self.ventana7.title("Buscador por Domicilio : ")
        self.ventana7.geometry("150x160")
        self.ventana7.iconbitmap("icono.ico")
        self.ventana7.maxsize(150, 160)
        self.ventana7.minsize(150, 160)

        self.frame7=tk.Frame(self.ventana7,bg="steel blue")
        self.frame7.pack(expand=True,fill="both")

        self.txt77=tk.Label(self.frame7,text="Domicilio: ",bg="dark turquoise")
        self.txt77.place(x=20,y=30,width=100,height=30)

        self.caja7777=tk.Entry(self.frame7)
        self.caja7777.place(x=20,y=80,width=100,height=30)

        self.boton77=tk.Button(self.frame7,text="Buscar",command=self.BuscarDomicilio,bd=5)
        self.boton77.place(x=20,y=120,width=100,height=30)
        self.ventana7.mainloop()

    def BuscarDomicilio(self):
        try:
            contador=0
            lugar=80
            xl=10
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                dom=self.caja7777.get()
                domici=str(dom)
                domicilio=domici.capitalize()
                valor={"domicilio":domicilio}
                c.execute("SELECT * FROM registro WHERE domicilio = :domicilio" , valor)
                registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    messagebox.showerror(message="No se encontro el Registro o \nIngreso un dato incorrecto",title="ERROR")

                else:
                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("Domicilio : ")
                    self.ventana9.geometry("800x500")
                    self.ventana9.iconbitmap("icono.ico")
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    self.Empleado_Tabla.heading("matricula",text="Matricula")
                    self.Empleado_Tabla.heading("nombre",text="Nombre")
                    self.Empleado_Tabla.heading("apellido",text="Apellido")
                    self.Empleado_Tabla.heading("edad",text="Edad")
                    self.Empleado_Tabla.heading("telefono",text="Telefono")
                    self.Empleado_Tabla.heading("domicilio",text="Domicilio")
                    self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
                    self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
                    self.Empleado_Tabla.pack(fill="both",expand=1)

                    self.Empleado_Tabla['show']='headings'
                    self.Empleado_Tabla.column("matricula",width=100)
                    self.Empleado_Tabla.column("nombre",width=100)
                    self.Empleado_Tabla.column("apellido",width=100)
                    self.Empleado_Tabla.column("edad",width=50)
                    self.Empleado_Tabla.column("telefono",width=90)
                    self.Empleado_Tabla.column("domicilio",width=120)
                    self.Empleado_Tabla.column("inscripcion",width=100)
                    self.Empleado_Tabla.column("fecha_Modificacion",width=120)
                    
    
                    index = iid = 0
                    for elemento in registros:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1
    
                        
                    self.ventana9.mainloop()
        except :
            messagebox.showerror(message="No Existe ningun dato \nLlena la tabla ",title="ERROR")

    def BuscarTodos(self):
        try:
            with sqlite3.connect("Empleados.db") as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM registro ")
                registros=c.fetchall()
                
            self.ventana9=tk.Tk()

            self.ancho_ventana = 800
            self.alto_ventana = 500

            self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
            self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana9.geometry(self.posicion)

            self.ventana9.title("Todos los Registros: ")
            self.ventana9.geometry("800x500")
            self.ventana9.maxsize(800, 500)
            self.ventana9.minsize(800, 500)
            self.ventana9.iconbitmap("icono.ico")
            self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
            self.frame09.pack(expand=True,fill="both")

            self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
            self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

            self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=("matricula","nombre","apellido","edad","telefono","domicilio","inscripcion","fecha_Modificacion"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
            self.scroll_x.pack(side="bottom",fill="x")
            self.scroll_y.pack(side="right",fill="y")
            self.scroll_x.config(command=self.Empleado_Tabla.xview)
            self.scroll_y.config(command=self.Empleado_Tabla.yview)

            self.Empleado_Tabla.heading("matricula",text="Matricula")
            self.Empleado_Tabla.heading("nombre",text="Nombre")
            self.Empleado_Tabla.heading("apellido",text="Apellido")
            self.Empleado_Tabla.heading("edad",text="Edad")
            self.Empleado_Tabla.heading("telefono",text="Telefono")
            self.Empleado_Tabla.heading("domicilio",text="Domicilio")
            self.Empleado_Tabla.heading("inscripcion",text="Inscripcion")
            self.Empleado_Tabla.heading("fecha_Modificacion",text="Fecha_Modificacion")
            self.Empleado_Tabla.pack(fill="both",expand=1)

            self.Empleado_Tabla['show']='headings'
            self.Empleado_Tabla.column("matricula",width=100)
            self.Empleado_Tabla.column("nombre",width=100)
            self.Empleado_Tabla.column("apellido",width=100)
            self.Empleado_Tabla.column("edad",width=50)
            self.Empleado_Tabla.column("telefono",width=90)
            self.Empleado_Tabla.column("domicilio",width=120)
            self.Empleado_Tabla.column("inscripcion",width=100)
            self.Empleado_Tabla.column("fecha_Modificacion",width=120)
            

            index = iid = 0
            for elemento in registros:
                self.Empleado_Tabla.insert("", index, iid, values=elemento)
                index = iid = index + 1

                
            self.ventana9.mainloop()
        except:
            messagebox.showerror(message="No Existe ningun dato \nLlena la tabla ",title="ERROR")




app=Aplicacion()