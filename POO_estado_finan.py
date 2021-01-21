
import sys 
import datetime
import matplotlib.pyplot as plt
import tkinter as tk

class Aplicacion():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Estado Financiero Datos : ")
        self.ventana.geometry("600x600")

        self.txt1=Label(self.ventana,text="INVENTARIO INICIAL",bg="yellow")
        self.txt1.place(x=220,y=10,width=170,height=30)

        self.txt2=Label(self.ventana,text="Materia Prima Directa : ",bg="lightblue")
        self.txt2.place(x=10,y=60,width=170,height=30)

        self.MPDI=Entry(self.ventana,bg="lightblue")
        self.MPDI.place(x=220,y=60,width=170,height=30)

        self.txt3=Label(self.ventana,text="Produccion en Proceso : ",bg="lightblue")
        self.txt3.place(x=10,y=100,width=170,height=30)

        self.PPI=Entry(self.ventana,bg="lightblue")
        self.PPI.place(x=220,y=100,width=170,height=30)

        self.txt4=Label(self.ventana,text="Articulos Terminados : ",bg="lightblue")
        self.txt4.place(x=10,y=140,width=170,height=30)

        self.ATI=Entry(self.ventana,bg="lightblue")
        self.ATI.place(x=220,y=140,width=170,height=30)

        self.txt5=Label(self.ventana,text="INVENTARIO FINAL",bg="yellow")
        self.txt5.place(x=220,y=200,width=170,height=30)

        self.txt6=Label(self.ventana,text="Materia Prima Directa : ",bg="lightblue")
        self.txt6.place(x=10,y=240,width=170,height=30)

        self.MPDF=Entry(self.ventana,bg="lightblue")
        self.MPDF.place(x=220,y=240,width=170,height=30)

        self.txt7=Label(self.ventana,text="Produccion de Procesos : ",bg="lightblue")
        self.txt7.place(x=10,y=280,width=170,height=30)

        self.PPF=Entry(self.ventana,bg="lightblue")
        self.PPF.place(x=220,y=280,width=170,height=30)

        self.txt8=Label(self.ventana,text="Articulos Terminados : ",bg="lightblue")
        self.txt8.place(x=10,y=320,width=170,height=30)

        self.ATF=Entry(self.ventana,bg="lightblue")
        self.ATF.place(x=220,y=320,width=170,height=30)

        self.txt9=Label(self.ventana,text="Mano de Obra Directa : ",bg="lightblue")
        self.txt9.place(x=10,y=360,width=170,height=30)

        self.MODF=Entry(self.ventana,bg="lightblue")
        self.MODF.place(x=220,y=360,width=170,height=30)

        self.txt10=Label(self.ventana,text="Compras de M.P.D : ",bg="lightblue")
        self.txt10.place(x=10,y=400,width=170,height=30)

        self.CMPDF=Entry(self.ventana,bg="lightblue")
        self.CMPDF.place(x=220,y=400,width=170,height=30)

        self.txt12=Label(self.ventana,text="Gasto Indirecto de Fabricacion : ",bg="lightblue")
        self.txt12.place(x=10,y=440,width=170,height=30)

        self.GIDFF=Entry(self.ventana,bg="lightblue")
        self.GIDFF.place(x=220,y=440,width=170,height=30)

        self.txt13=Label(self.ventana,text="Gastos/Compras de M.P.D : ",bg="lightblue")
        self.txt13.place(x=10,y=480,width=170,height=30)

        self.GCMPDF=Entry(self.ventana,bg="lightblue")
        self.GCMPDF.place(x=220,y=480,width=170,height=30)

        self.txt14=Label(self.ventana,text="Devoluciones y Descuentos ",bg="lightblue")
        self.txt14.place(x=10,y=520,width=170,height=30)

        self.txt15=Label(self.ventana,text="/Compras de M.P.D : ",bg="lightblue")
        self.txt15.place(x=10,y=540,width=170,height=30)

        self.DRCMPDF=Entry(self.ventana,bg="lightblue")
        self.DRCMPDF.place(x=220,y=530,width=170,height=30)

        self.boton1=Button(self.ventana,text="Calcular",command=RealizarEF)
        self.boton1.place(x=460,y=530,width=100,height=30)

        self.boton2=Button(self.ventana,text="Graficar",command=Graficar)
        self.boton2.place(x=460,y=480,width=100,height=30)

        self.boton3=Button(self.ventana,text="Borrar Todo",command=Borrar)
        self.boton3.place(x=460,y=430,width=100,height=30)

        self.txt16=Label(self.ventana,text="Hora : ",bg="lightblue")
        self.txt16.place(x=450,y=60,width=80,height=30)

        self.caja4=Entry(self.ventana,bg="lightblue")
        self.caja4.place(x=435,y=100,width=120,height=30)