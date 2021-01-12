import sys 
import matplotlib.pyplot as plt
from tkinter import *
class EstadoFinanciero:
    def __init__(self,MPDI,PPI,ATI,MPDF,PPF,ATF,MODF,CMPDF,GIDFF,GCMPDF,DRCMPDF):
        self.__MPDI=MPDI
        self.__PPI=PPI
        self.__ATI=ATI
        self.__MPDF=MPDF
        self.__PPF=PPF
        self.__ATF=ATF
        self.__MODF=MODF
        self.__CMPDF=CMPDF
        self.__GIDFF=GIDFF
        self.__GCMPDF=GCMPDF
        self.__DRCMPDF=DRCMPDF

    def RealizarEF(self):
        ComprasTotales=(self.__CMPDF+self.__GCMPDF)
        ComprasNetasDeMateriales=(ComprasTotales-self.__DRCMPDF)
        MaterialesDisponibles=(ComprasNetasDeMateriales+self.__MPDI)
        MateriaPrimaUtilizada=(MaterialesDisponibles-self.__MPDF)
        CostoPrimo=(MateriaPrimaUtilizada+self.__MODF)
        CostoIncurrido=(CostoPrimo+self.__GIDFF)
        TotalDeProduccionEnProcesos=(CostoIncurrido+self.__PPI)
        CostoDeProduccion=(TotalDeProduccionEnProcesos-self.__PPF)
        TotalDeArticulosListosParaLaVenta=(CostoDeProduccion+self.__ATI)
        CostoDeProduccionDeLoVendido=(TotalDeArticulosListosParaLaVenta-self.__ATF)
        
        print(f"Estas son tus Compras Totales : {ComprasTotales} ")
        print(f"Estas son tus Compras Netas De Materiales : {ComprasNetasDeMateriales} ")
        print(f"Estas son tus Materiales Disponibles : {MaterialesDisponibles} ")
        print(f"Esta es tu Materia Prima Utilizada : {MateriaPrimaUtilizada} ")
        print(f"Esto es tu Costo Primo : {CostoPrimo} ")
        print(f"Este es tu Costo Incurrido/Costo Previo : {CostoIncurrido} ")
        print(f"Este es tu Total De Produccion En Procesos : {TotalDeProduccionEnProcesos} ")
        print(f"Este es tu Costo De Produccion : {CostoDeProduccion} ")
        print(f"Esto es tu Total De Articulos Listos Para La Venta : {TotalDeArticulosListosParaLaVenta} ")
        print(f"Este es tu Costo de Produccion De Lo Vendido : { CostoDeProduccionDeLoVendido} ")
        print("-"*100)
        print("1=SI\n2=NO")
        opcion2=int(input("¿Quieres graficar las respuestas? : "))
        if opcion2==1:
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
        txt1.place(x=220,y=10,width=140,height=30)

        txt2=Label(ventana,text="Materia Prima Directa : ",bg="lightblue")
        txt2.place(x=10,y=60,width=140,height=30)

        MPDI=Entry(ventana,bg="lightblue")
        MPDI.place(x=220,y=60,width=140,height=30)

        txt3=Label(ventana,text="Produccion en Proceso : ",bg="lightblue")
        txt3.place(x=10,y=120,width=140,height=30)

        PPI=Entry(ventana,bg="lightblue")
        PPI.place(x=220,y=120,width=140,height=30)

        txt4=Label(ventana,text="Articulos Terminados : ",bg="lightblue")
        txt4.place(x=10,y=180,width=140,height=30)

        ATI=Entry(ventana,bg="lightblue")
        ATI.place(x=220,y=180,width=140,height=30)

        txt5=Label(ventana,text="INVENTARIO FINAL",bg="yellow")
        txt5.place(x=220,y=230,width=140,height=30)

        txt6=Label(ventana,text="Materia Prima Directa : ",bg="lightblue")
        txt6.place(x=10,y=270,width=140,height=30)

        MPDF=Entry(ventana,bg="lightblue")
        MPDF.place(x=220,y=270,width=140,height=30)

        txt7=Label(ventana,text="Produccion de Procesos : ",bg="lightblue")
        txt7.place(x=10,y=320,width=140,height=30)

        PPF=Entry(ventana,bg="lightblue")
        PPF.place(x=220,y=320,width=140,height=30)

        txt8=Label(ventana,text="Articulos Terminados : ",bg="lightblue")
        txt8.place(x=10,y=360,width=140,height=30)

        ATF=Entry(ventana,bg="lightblue")
        ATF.place(x=220,y=360,width=140,height=30)

        txt9=Label(ventana,text="Mano de Obra Directa : ",bg="lightblue")
        txt9.place(x=10,y=400,width=140,height=30)

        MODF=Entry(ventana,bg="lightblue")
        MODF.place(x=220,y=400,width=140,height=30)




        MODF=int(input("Dime tu Mano de Obra Directa del inventaria final : "))
        CMPDF=int(input("Dime tus Compras de M.P.D del inventario final : "))
        GIDFF=int(input("Dime tu Gasto Indirecto de Fabricacion del inventario final : "))
        GCMPDF=int(input("Dime tu Gasto/compras de M.P.D del inventario final : "))
        DRCMPDF=int(input("Dime tus Devoluciones y Descuentos / compras de M.P.D del inventario final : "))
        a=EstadoFinanciero(MPDI,PPI,ATI,MPDF,PPF,ATF,MODF,CMPDF,GIDFF,GCMPDF,DRCMPDF)
        print("-"*100)
        a.RealizarEF()
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