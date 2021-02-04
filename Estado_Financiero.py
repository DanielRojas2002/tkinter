import sys 
import datetime
import matplotlib.pyplot as plt
from tkinter import *
import pandas as pd


def Borrar():
    MPDI.delete(0,"end")
    PPI.delete(0,"end")
    ATI.delete(0,"end")
    MPDF.delete(0,"end")
    PPF.delete(0,"end")
    ATF.delete(0,"end")
    MODF.delete(0,"end")
    CMPDF.delete(0,"end")
    GIDFF.delete(0,"end")
    GCMPDF.delete(0,"end")
    DRCMPDF.delete(0,"end")
    ahora = datetime.datetime.now()
    ahora1=ahora.strftime('%d/%m/%Y %H:%M:%S')
    caja4.delete(0,"end")
    caja4.insert(0,ahora1)




def RealizarEF():
    try:
        dic={}
        a=(MPDI.get())
        b=(PPI.get())
        c=(ATI.get())
        d=(MPDF.get())
        e=(PPF.get())
        g=(ATF.get())
        h=(MODF.get())
        i=(CMPDF.get())
        j=(GIDFF.get())
        k=(GCMPDF.get())
        l=(DRCMPDF.get())
        ahora = datetime.datetime.now()
        ahora1=ahora.strftime('%d/%m/%Y %H:%M:%S')
        caja4.delete(0,"end")
        caja4.insert(0,ahora1)

        lista=[]
        lista1=[]
        lista2=[]
        lista3=[]
        lista4=[]
        lista5=[]
        lista6=[]
        lista7=[]
        lista8=[]
        lista9=[]
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

  
        lista.append(ComprasTotales)
        lista1.append(ComprasNetasDeMateriales)
        lista2.append(MaterialesDisponibles)
        lista3.append(MateriaPrimaUtilizada)
        lista4.append(CostoPrimo)
        lista5.append(CostoIncurrido)
        lista6.append(TotalDeProduccionEnProcesos)
        lista7.append(CostoDeProduccion)
        lista8.append(TotalDeProduccionEnProcesos)
        lista9.append(CostoDeProduccionDeLoVendido)

        dic["Compras Totales"]=lista
        dic["Compras Netas de Materiales"]=lista1
        dic["Materiales Disponibles"]=lista2
        dic["Materia Prima Utilizada"]=lista3
        dic["Costo Primo"]=lista4
        dic["Costo Incurrido"]=lista5
        dic["Total de Produccion en Procesos"]=lista6
        dic["Costo de Produccion"]=lista7
        dic["Total de Articulos para la Venta"]=lista8
        dic["Costo de Produccion de lo Vendido"]=lista9

        dic2=pd.DataFrame(dic)

        fecha=datetime.datetime.now()
        fecha2=fecha.strftime('%d_%m_%Y_%H_%M_%S')
        a="Reporte_"+str(fecha2)
        b=".xlsx"
        c=a+b
        ruta = "C:\\comun\\"+c
        dic2.to_excel(ruta, index=None)

        messagebox.showinfo(message="Su Archivo Excel fue generado en C:comun",title=":)")
    except:
        Borrar()
        MPDI.insert(0,'Llena todos los Datos :)')
        PPI.insert(0,'Llena todos los Datos :)')
        ATI.insert(0,'Llena todos los Datos :)')
        MPDF.insert(0,'Llena todos los Datos :)')
        PPF.insert(0,'Llena todos los Datos :)')
        ATF.insert(0,'Llena todos los Datos :)')
        MODF.insert(0,'Llena todos los Datos :)')
        CMPDF.insert(0,'Llena todos los Datos :)')
        GIDFF.insert(0,'Llena todos los Datos :)')
        GCMPDF.insert(0,'Llena todos los Datos :)')
        DRCMPDF.insert(0,'Llena todos los Datos :)')


def Graficar():
    try:

        a=(MPDI.get())
        b=(PPI.get())
        c=(ATI.get())
        d=(MPDF.get())
        e=(PPF.get())
        g=(ATF.get())
        h=(MODF.get())
        i=(CMPDF.get())
        j=(GIDFF.get())
        k=(GCMPDF.get())
        l=(DRCMPDF.get())
        ahora = datetime.datetime.now()
        ahora1=ahora.strftime('%d/%m/%Y %H:%M:%S')
        caja4.delete(0,"end")
        caja4.insert(0,ahora1)

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

        valores=[]
        valores2=[]

        valores.append(ComprasTotales)
        valores.append(ComprasNetasDeMateriales)
        valores.append(MaterialesDisponibles)
        valores.append(MateriaPrimaUtilizada)
        valores.append(CostoPrimo)

        valores2.append(CostoIncurrido)
        valores2.append(TotalDeProduccionEnProcesos)
        valores2.append(CostoDeProduccion)
        valores2.append(TotalDeArticulosListosParaLaVenta)
        valores2.append(CostoDeProduccionDeLoVendido)

        figura=plt.figure()
        ax1=figura.add_subplot(211)
        ax2=figura.add_subplot(212)

        datos=["CompraTotal","CompraNetaMaterial","MaterialDisponible","MateriaPrimaUtilizada","CostoPrimo"]
        colores=["red","green","orange","blue","purple"]
        ax1.bar(datos,valores,color=colores,width=0.5,align="center")
        ax1.set_xticklabels(datos)
        ax1.set_ylabel("Respuestas seccion 1 ")

        datos2=["CostoIncurrido","TotalProduccionProcesos","CostoProduccion","TotalArticulosVenta","CostoProduccionVendido"]
        ax2.bar(datos2,height=valores2,color=colores,width=0.5,align="center")
        ax2.set_xticklabels(datos2)
        ax2.set_ylabel("Respuestas seccion 2 ")
        plt.show()
        
    except:
        Borrar()
        MPDI.insert(0,'Llena todos los Datos :)')
        PPI.insert(0,'Llena todos los Datos :)')
        ATI.insert(0,'Llena todos los Datos :)')
        MPDF.insert(0,'Llena todos los Datos :)')
        PPF.insert(0,'Llena todos los Datos :)')
        ATF.insert(0,'Llena todos los Datos :)')
        MODF.insert(0,'Llena todos los Datos :)')
        CMPDF.insert(0,'Llena todos los Datos :)')
        GIDFF.insert(0,'Llena todos los Datos :)')
        GCMPDF.insert(0,'Llena todos los Datos :)')
        DRCMPDF.insert(0,'Llena todos los Datos :)')


try:
    ventana=Tk()
    ventana.title("Estado Financiero Datos : ")
    ventana.geometry("600x600") 
   
    txt1=Label(ventana,text="INVENTARIO INICIAL",bg="yellow")
    txt1.place(x=220,y=10,width=170,height=30)

    txt2=Label(ventana,text="Materia Prima Directa : ",bg="lightblue")
    txt2.place(x=10,y=60,width=170,height=30)

    MPDI=Entry(ventana,bg="lightblue")
    MPDI.place(x=220,y=60,width=170,height=30)

    txt3=Label(ventana,text="Produccion en Proceso : ",bg="lightblue")
    txt3.place(x=10,y=100,width=170,height=30)

    PPI=Entry(ventana,bg="lightblue")
    PPI.place(x=220,y=100,width=170,height=30)

    txt4=Label(ventana,text="Articulos Terminados : ",bg="lightblue")
    txt4.place(x=10,y=140,width=170,height=30)

    ATI=Entry(ventana,bg="lightblue")
    ATI.place(x=220,y=140,width=170,height=30)

    txt5=Label(ventana,text="INVENTARIO FINAL",bg="yellow")
    txt5.place(x=220,y=200,width=170,height=30)

    txt6=Label(ventana,text="Materia Prima Directa : ",bg="lightblue")
    txt6.place(x=10,y=240,width=170,height=30)

    MPDF=Entry(ventana,bg="lightblue")
    MPDF.place(x=220,y=240,width=170,height=30)

    txt7=Label(ventana,text="Produccion de Procesos : ",bg="lightblue")
    txt7.place(x=10,y=280,width=170,height=30)

    PPF=Entry(ventana,bg="lightblue")
    PPF.place(x=220,y=280,width=170,height=30)

    txt8=Label(ventana,text="Articulos Terminados : ",bg="lightblue")
    txt8.place(x=10,y=320,width=170,height=30)

    ATF=Entry(ventana,bg="lightblue")
    ATF.place(x=220,y=320,width=170,height=30)

    txt9=Label(ventana,text="Mano de Obra Directa : ",bg="lightblue")
    txt9.place(x=10,y=360,width=170,height=30)

    MODF=Entry(ventana,bg="lightblue")
    MODF.place(x=220,y=360,width=170,height=30)

    txt10=Label(ventana,text="Compras de M.P.D : ",bg="lightblue")
    txt10.place(x=10,y=400,width=170,height=30)

    CMPDF=Entry(ventana,bg="lightblue")
    CMPDF.place(x=220,y=400,width=170,height=30)

    txt12=Label(ventana,text="Gasto Indirecto de Fabricacion : ",bg="lightblue")
    txt12.place(x=10,y=440,width=170,height=30)

    GIDFF=Entry(ventana,bg="lightblue")
    GIDFF.place(x=220,y=440,width=170,height=30)

    txt13=Label(ventana,text="Gastos/Compras de M.P.D : ",bg="lightblue")
    txt13.place(x=10,y=480,width=170,height=30)

    GCMPDF=Entry(ventana,bg="lightblue")
    GCMPDF.place(x=220,y=480,width=170,height=30)

    txt14=Label(ventana,text="Devoluciones y Descuentos ",bg="lightblue")
    txt14.place(x=10,y=520,width=170,height=30)

    txt15=Label(ventana,text="/Compras de M.P.D : ",bg="lightblue")
    txt15.place(x=10,y=540,width=170,height=30)

    DRCMPDF=Entry(ventana,bg="lightblue")
    DRCMPDF.place(x=220,y=530,width=170,height=30)

    boton1=Button(ventana,text="Calcular",command=RealizarEF)
    boton1.place(x=460,y=530,width=100,height=30)

    boton2=Button(ventana,text="Graficar",command=Graficar)
    boton2.place(x=460,y=480,width=100,height=30)

    boton3=Button(ventana,text="Borrar Todo",command=Borrar)
    boton3.place(x=460,y=430,width=100,height=30)

    txt16=Label(ventana,text="Hora : ",bg="lightblue")
    txt16.place(x=450,y=60,width=80,height=30)

    caja4=Entry(ventana,bg="lightblue")
    caja4.place(x=435,y=100,width=120,height=30)




except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("*"*30,"Fin del Programa","*"*30) 
    ventana.mainloop()
