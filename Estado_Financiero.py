import sys 
import matplotlib.pyplot as plt
from tkinter import *


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




def RealizarEF():
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

    ventana2=Tk()
    ventana2.title("Estado Financiero Respuestas : ")
    ventana2.geometry("600x600")

    
    
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
        txt16=Label(ventana2,text=elemento,bg="yellow")
        txt16.grid(row=contador,column=5)
        contador=contador+1
    ventana2.mainloop()

    if 1==1:
        datos=["ComprasTotales","ComprasNetasDeMateriales","MaterialesDisponibles","MateriaPrimaUtilizada","CostoPrimo"]
        valores=[ComprasTotales,ComprasTotales,MaterialesDisponibles,MateriaPrimaUtilizada,CostoPrimo]
        colores=["red","green","orange","blue","purple"]
        plt.bar(datos,height=valores,color=colores,width=0.5)
        plt.title("Respuestas seccion 1 ")
        plt.show()

        datos2=["CostoIncurrido","TotalDeProduccionEnProcesos","CostoDeProduccion","TotalArticulosParaLaVenta","CostoProduccionDeLoVendido"]
        valores2=[CostoIncurrido,TotalDeProduccionEnProcesos,CostoDeProduccion,TotalDeArticulosListosParaLaVenta,CostoDeProduccionDeLoVendido] 
        plt.bar(datos2,height=valores2,color=colores,width=0.5)
        plt.title("Respuestas seccion 2")
        plt.show()
opcion=1
try:
    ventana=Tk()
    ventana.title("Estado Financiero Datos : ")
    ventana.geometry("600x600") 
    while opcion==1:

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

        boton1=Button(ventana,text="Registrar",command=RealizarEF)
        boton1.place(x=460,y=530,width=100,height=30)

        boton2=Button(ventana,text="Borrar Todo",command=Borrar)
        boton2.place(x=460,y=460,width=100,height=30)


        print("-"*100)
        opcion=int(input("Deseas seguir sacando Estados Financieros 1=SI 2=NO : "))
        print("-"*100)

except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("*"*30,"Fin del Programa","*"*30) 
    ventana.mainloop()