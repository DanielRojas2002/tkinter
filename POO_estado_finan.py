
import sys 
import datetime
import matplotlib.pyplot as plt
import tkinter as tk

class Aplicacion():

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Estado Financiero Datos : ")
        self.ventana.geometry("600x600")

        self.txt1=tk.Label(self.ventana,text="INVENTARIO INICIAL",bg="yellow")
        self.txt1.place(x=220,y=10,width=170,height=30)

        self.txt2=tk.Label(self.ventana,text="Materia Prima Directa : ",bg="lightblue")
        self.txt2.place(x=10,y=60,width=170,height=30)

        self.MPDI=tk.Entry(self.ventana,bg="lightblue")
        self.MPDI.place(x=220,y=60,width=170,height=30)

        self.txt3=tk.Label(self.ventana,text="Produccion en Proceso : ",bg="lightblue")
        self.txt3.place(x=10,y=100,width=170,height=30)

        self.PPI=tk.Entry(self.ventana,bg="lightblue")
        self.PPI.place(x=220,y=100,width=170,height=30)

        self.txt4=tk.Label(self.ventana,text="Articulos Terminados : ",bg="lightblue")
        self.txt4.place(x=10,y=140,width=170,height=30)

        self.ATI=tk.Entry(self.ventana,bg="lightblue")
        self.ATI.place(x=220,y=140,width=170,height=30)

        self.txt5=tk.Label(self.ventana,text="INVENTARIO FINAL",bg="yellow")
        self.txt5.place(x=220,y=200,width=170,height=30)

        self.txt6=tk.Label(self.ventana,text="Materia Prima Directa : ",bg="lightblue")
        self.txt6.place(x=10,y=240,width=170,height=30)

        self.MPDF=tk.Entry(self.ventana,bg="lightblue")
        self.MPDF.place(x=220,y=240,width=170,height=30)

        self.txt7=tk.Label(self.ventana,text="Produccion de Procesos : ",bg="lightblue")
        self.txt7.place(x=10,y=280,width=170,height=30)

        self.PPF=tk.Entry(self.ventana,bg="lightblue")
        self.PPF.place(x=220,y=280,width=170,height=30)

        self.txt8=tk.Label(self.ventana,text="Articulos Terminados : ",bg="lightblue")
        self.txt8.place(x=10,y=320,width=170,height=30)

        self.ATF=tk.Entry(self.ventana,bg="lightblue")
        self.ATF.place(x=220,y=320,width=170,height=30)

        self.txt9=tk.Label(self.ventana,text="Mano de Obra Directa : ",bg="lightblue")
        self.txt9.place(x=10,y=360,width=170,height=30)

        self.MODF=tk.Entry(self.ventana,bg="lightblue")
        self.MODF.place(x=220,y=360,width=170,height=30)

        self.txt10=tk.Label(self.ventana,text="Compras de M.P.D : ",bg="lightblue")
        self.txt10.place(x=10,y=400,width=170,height=30)

        self.CMPDF=tk.Entry(self.ventana,bg="lightblue")
        self.CMPDF.place(x=220,y=400,width=170,height=30)

        self.txt12=tk.Label(self.ventana,text="Gasto Indirecto de Fabricacion : ",bg="lightblue")
        self.txt12.place(x=10,y=440,width=170,height=30)

        self.GIDFF=tk.Entry(self.ventana,bg="lightblue")
        self.GIDFF.place(x=220,y=440,width=170,height=30)

        self.txt13=tk.Label(self.ventana,text="Gastos/Compras de M.P.D : ",bg="lightblue")
        self.txt13.place(x=10,y=480,width=170,height=30)

        self.GCMPDF=tk.Entry(self.ventana,bg="lightblue")
        self.GCMPDF.place(x=220,y=480,width=170,height=30)

        self.txt14=tk.Label(self.ventana,text="Devoluciones y Descuentos ",bg="lightblue")
        self.txt14.place(x=10,y=520,width=170,height=30)

        self.txt15=tk.Label(self.ventana,text="/Compras de M.P.D : ",bg="lightblue")
        self.txt15.place(x=10,y=540,width=170,height=30)

        self.DRCMPDF=tk.Entry(self.ventana,bg="lightblue")
        self.DRCMPDF.place(x=220,y=530,width=170,height=30)

        self.boton1=tk.Button(self.ventana,text="Calcular",command=self.RealizarEF)
        self.boton1.place(x=460,y=530,width=100,height=30)

        self.boton2=tk.Button(self.ventana,text="Graficar",command=self.Graficar)
        self.boton2.place(x=460,y=480,width=100,height=30)

        self.boton3=tk.Button(self.ventana,text="Borrar Todo",command=self.Borrar)
        self.boton3.place(x=460,y=430,width=100,height=30)

        self.txt16=tk.Label(self.ventana,text="Hora : ",bg="lightblue")
        self.txt16.place(x=450,y=60,width=80,height=30)

        self.caja4=tk.Entry(self.ventana,bg="lightblue")
        self.caja4.place(x=435,y=100,width=120,height=30)

    def Borrar(self):
        self.MPDI.delete(0,"end")
        self.PPI.delete(0,"end")
        self.ATI.delete(0,"end")
        self.MPDF.delete(0,"end")
        self.PPF.delete(0,"end")
        self.ATF.delete(0,"end")
        self.MODF.delete(0,"end")
        self.CMPDF.delete(0,"end")
        self.GIDFF.delete(0,"end")
        self.GCMPDF.delete(0,"end")
        self.DRCMPDF.delete(0,"end")
        ahora = datetime.datetime.now()
        ahora1=ahora.strftime('%d/%m/%Y %H:%M:%S')
        self.caja4.delete(0,"end")
        self.caja4.insert(0,ahora1)

    def RealizarEF(self):
        try:
            a=(self.MPDI.get())
            b=(self.PPI.get())
            c=(self.ATI.get())
            d=(self.MPDF.get())
            e=(self.PPF.get())
            g=(self.ATF.get())
            h=(self.MODF.get())
            i=(self.CMPDF.get())
            j=(self.GIDFF.get())
            k=(self.GCMPDF.get())
            l=(self.DRCMPDF.get())
            ahora = datetime.datetime.now()
            ahora1=ahora.strftime('%d/%m/%Y %H:%M:%S')
            self.caja4.delete(0,"end")
            self.caja4.insert(0,ahora1)

            lista=[]
            ComprasTotales=float(d)+float(k)
            ComprasNetasDeMateriales=ComprasTotales-float(l)
            MaterialesDisponibles=ComprasNetasDeMateriales+float(a)
            MateriaPrimaUtilizada=(MaterialesDisponibles)-float(d)
            CostoPrimo=(MateriaPrimaUtilizada)+float(h)
            CostoIncurrido=(CostoPrimo)+float(j)
            TotalDeProduccionEnProcesos=(CostoIncurrido)+float(b)
            CostoDeProduccion=(TotalDeProduccionEnProcesos)-float(e)
            TotalDeArticulosListosParaLaVenta=(CostoDeProduccion)+float(c)
            CostoDeProduccionDeLoVendido=(TotalDeArticulosListosParaLaVenta)-float(g)



            self.ventana2=tk.Tk()
            self.ventana2.title("Estado Financiero Respuestas : ")
            self.ventana2.geometry("600x600")

            
            
            lista.append("Compras Totales : "+str(ComprasTotales))
            lista.append("Compras Netas De Materiales : "+str(ComprasNetasDeMateriales))
            lista.append("Materiales Disponibles : "+str(MaterialesDisponibles))
            lista.append("Materia Prima Utilizanda"+str(MateriaPrimaUtilizada))
            lista.append("Costo Primo : "+str(CostoPrimo))
            lista.append("Costo Incurrido/Costo Previo : "+str(CostoIncurrido))
            lista.append("Total De Produccion En Procesos : "+str(TotalDeProduccionEnProcesos))
            lista.append("Costo De Produccion : "+str(CostoDeProduccion))
            lista.append("Total De Articulos Listos Para La Venta : "+str(TotalDeProduccionEnProcesos))
            lista.append("Costo De Produccion De Lo Vendido : "+str(CostoDeProduccionDeLoVendido))

            contador=1
            for elemento in lista:
                self.txt16=tk.Label(self.ventana2,text=elemento,bg="yellow")
                self.txt16.grid(row=contador,column=5)
                contador=contador+1
            self.ventana2.mainloop()
        except:
            self.Borrar()
            self.MPDI.insert(0,'Llena todos los Datos :)')
            self.PPI.insert(0,'Llena todos los Datos :)')
            self.ATI.insert(0,'Llena todos los Datos :)')
            self.MPDF.insert(0,'Llena todos los Datos :)')
            self.PPF.insert(0,'Llena todos los Datos :)')
            self.ATF.insert(0,'Llena todos los Datos :)')
            self.MODF.insert(0,'Llena todos los Datos :)')
            self.CMPDF.insert(0,'Llena todos los Datos :)')
            self.GIDFF.insert(0,'Llena todos los Datos :)')
            self.GCMPDF.insert(0,'Llena todos los Datos :)')
            self.DRCMPDF.insert(0,'Llena todos los Datos :)')