import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk



class desempleos:
    def __init__ (self,desempleados,PEA):
        self.__desempleados=desempleados
        self.__PEA=PEA
    
    
    def calculo(self):
        archivoA=open("C:\\comun\\Desempleo.txt" , 'a')
        resultado=(self.__desempleados/self.__PEA)*100
        textoa=str(resultado)
        archivoA.write("RESPUESTA DE LA TASA DE DESEMPLEO :)" +"\n" )
        archivoA.write("TASA DE DESEMPLEO = " + textoa +  "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        messagebox.showinfo(message="Su archivo TXT fue generado e C\\comun",title="Tasa Desempleo ")


#--------------------------------------------------------------------------------------------------------------------------------------
# METODO DEL INGRESO

class MetodoDelIngreso():
    def __init__ (self,II,IP,IN,D,BC,R,RT,INFE):
        self.__II=II
        self.__IP=IP
        self.__IN=IN
        self.__D=D
        self.__BC=BC
        self.__R=R
        self.__RT=RT
        self.__INFE=INFE
        
         
    def PIB(self):
        IN=(self.__RT+self.__R+self.__IN+self.__IP+self.__BC)
        pib=(IN+self.__II+self.__D+self.__INFE)
        textoa=str(IN)
        textob=str(pib)
        archivoA=open("C:\\comun\\Metodo_Ingreso.txt" , 'a')
        archivoA.write("RESPUESTAS DEL METODO DEL INGRESO :)" +"\n" )
        archivoA.write("Ingreso Nacional(IN) = " + textoa +  "\n" )
        archivoA.write("Producto Interno Bruto(PIB) =" + textob + "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        messagebox.showinfo(message="Su archivo TXT fue generado e C\\comun",title="Metodo Ingreso ")

#-------------------------------------------------------------------------------------------------------------------------------------
#METODO DEL GASTO

class MetodoDelGasto():
    def __init__(self,ID,INFEE,E,D,IM,GG,GCF):
        self.__ID=ID
        self.__INFEE=INFEE
        self.__E=E
        self.__D=D
        self.__IM=IM
        self.__GG=GG
        self.__GCF=GCF
        
    
    def PIB(self):
        XN=(self.__E-self.__IM)
        pib=(self.__GCF+self.__INFEE+self.__GG+XN)
        PIN=(pib-self.__D)
        IN=(PIN-self.__INFEE-self.__ID)
        textoa=str(pib)
        textob=str(PIN)
        textoc=str(IN)

        archivoA=open("C:\\comun\\Metodo_Gasto.txt" , 'a')
        archivoA.write("RESPUESTAS DEL METODO DEL GASTO :)" +"\n" )
        archivoA.write("Producto Interno Bruto(PIB) =" + textoa +  "\n" )
        archivoA.write("Producto Interno Neto(PIN) = " + textob +  "\n" )
        archivoA.write("Ingreso Nacional(IN) =" + textoc +  "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        messagebox.showinfo(message="Su archivo TXT fue generado e C\\comun",title="Metodo Gasto ")
        
    
    


#VARIABLES MACROECONOMICAS
   
def indice(listaNivel,listaIndice,baseo,listaAño):
    archivoA=open("C:\\comun\\Variables_Economicas.txt" , 'a')
    archivoA.write("RESPUESTAS DE LAS VARIABLES MACROECONOMICAS :)" +"\n" )
    contador=0
    separador=("*"*40)
    for precio in listaNivel:
        z=(precio/(listaNivel[baseo]))*100
        listaIndice.append(z)
    print(separador)
    print("")
    for numero in listaIndice:
        print("INDICE DE PRECIOS : ")
        print(f"El indice de Precios del año {listaAño[contador]} es = {numero}")
        textoa=str(numero)
        archivoA.write("Indice de Precios = " + textoa +  "\n" )
        contador=contador+1
        print(separador)
        print("")
    archivoA.close()


def inflacion(listaIndice,listaAño,cuantos,listaInflacion):
    archivoA=open("C:\\comun\\Variables_Economicas.txt" , 'a')
    contador=1
    contador2=0
    contadorA=1
    separador=("*"*40)
    
    for numero in range(cuantos-1):
        resultado=(listaIndice[contador]-listaIndice[contador2])/listaIndice[contador2]*100
        contador=contador+1
        contador2=contador2+1
        if resultado!=0:
            listaInflacion.append(resultado)
    
    for numero in listaInflacion:
        textoa=str(numero)
        archivoA.write("Inflacion = " + textoa +  "\n" )
        contadorA=contadorA+1
    archivoA.close()


def PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos):
    archivoA=open("C:\\comun\\Variables_Economicas.txt" , 'a')
    contador=0
    contadorA=0
    separador=("*"*40)
    for numero in range(cuantos):
        resultado=(listaPIBN[contador]/listaIndice[contador])*100
        listaPIBR.append(resultado)
        contador=contador+1
    
    for numero in listaPIBR:
        print("Producto Interno Bruto Real : ")
        print(f"El Producto Interno Bruto Real del año {listaAño[contadorA]} es = {numero}")
        textoa=str(numero)
        archivoA.write("Producto Interno Bruto Real = " + textoa +  "\n" )
        contadorA=contadorA+1
        print(separador)
        print("")
    archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
    archivoA.close()


class Aplicacion:
    def __init__(self):
        self.ventanai=tk.Tk()
        self.ancho_ventana = 600
        self.alto_ventana = 600

        self.x_ventana = self.ventanai.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventanai.geometry(self.posicion)
        self.ventanai.title("BIENVENIDO AL MENU PRINCIPAL : ")
        self.ventanai.geometry("600x600")
        self.ventanai.maxsize(600, 600)
        self.ventanai.minsize(600, 600)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.ventanai.iconbitmap("icono.ico")

        self.frame=tk.Frame(self.ventanai,bg="slate gray")
        self.frame.pack(expand=True,fill="both")

        self.framee=tk.Frame(self.ventanai,bg="royal blue")
        self.framee.place(x=0,y=0,width=600,height=120)

        self.txt0101=tk.Label(self.framee,text="SELECCIONE LO QUE DESEA HACER",background="gold",font=self.fontStyle)
        self.txt0101.place(x=40,y=10,width=500,height=100)

    
        self.image=tk.PhotoImage(file="base.gif")
        self.txt=tk.Label(image=self.image)
        self.txt.place(x=85,y=150)


        self.frame2=tk.Frame(self.ventanai,bg="deep sky blue")
        self.frame2.place(x=0,y=480,width=600,height=130)
        self.frame2.config(cursor="hand1")

        self.botonAlta=tk.Button(self.frame2,text="PIB",command=self.PIB,bd=5)
        self.botonAlta.place(x=10,y=40,width=100,height=30)

        self.boton2=tk.Button(self.frame2,text="TASA DE DESEMPLEO",command=self.TD,bd=5)
        self.boton2.place(x=460,y=40,width=130,height=30)

        self.boton4=tk.Button(self.frame2,text="INDICE DE PRECIOS ,INFLACION Y PRODUCTO REAL",command=self.IIP,bd=5)
        self.boton4.place(x=140,y=40,width=300,height=30)

        self.boton5=tk.Button(self.frame2,text="FORMULAS",command=self.formulas,bd=5)
        self.boton5.place(x=230,y=80,width=100,height=30)

        self.ventanai.mainloop()

    def formulas(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 500
        self.alto_ventana = 500

        self.x_ventana = self.ventanai.winfo_screenwidth() - 440 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("FORMULAS : ")
        self.ventana.geometry("500x500")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.maxsize(500, 500)
        self.ventana.minsize(500, 500)

        self.MI=tk.Frame(self.ventana,bg="seagreen")
        self.MI.place(x=0,y=0,width=250,height=250)

        self.G=tk.Frame(self.ventana,bg="yellow")
        self.G.place(x=250,y=0,width=250,height=250)

        self.T=tk.Frame(self.ventana,bg="green yellow")
        self.T.place(x=0,y=250,width=250,height=250)

        self.IIP=tk.Frame(self.ventana,bg="olive drab")
        self.IIP.place(x=250,y=250,width=250,height=250)

     
        self.txt0=tk.Label(self.MI,text="METODO DEL INGRESO: ",bg="gold")
        self.txt0.place(x=20,y=20,width=200,height=30)

        self.txt00=tk.Label(self.MI,text="IN=(RT+R+IN+IP+BC)\nPIB=(IN+IIE+DEP+INFE)")
        self.txt00.place(x=20,y=100,width=200,height=30)

        self.txt1=tk.Label(self.G,text="METODO DEL GASTO: ",bg="seagreen")
        self.txt1.place(x=20,y=20,width=200,height=30)

        self.txt11=tk.Label(self.G,text="XN=(E-I)\nPIB=(C+I+G+XN)\nIN=(PIN-ingreso neto de los factores\n-Impuestos indirectos)")
        self.txt11.place(x=20,y=80,width=220,height=80)

        
        self.txt2=tk.Label(self.T,text="TASA DE DESEMPLEO: ",bg="olive drab")
        self.txt2.place(x=20,y=20,width=200,height=30)

        self.txt22=tk.Label(self.T,text="TD=(Desempleados/PEA)*100")
        self.txt22.place(x=20,y=100,width=200,height=30)

        self.txt3=tk.Label(self.IIP,text="Indice de precios,Inflacion,PIBR",bg="green yellow")
        self.txt3.place(x=20,y=20,width=200,height=30)

        self.txt33=tk.Label(self.IIP,text="IP=(Nivel de precios/\nBase de nivel de precios)*100\n\nINFLACION=(Indice de precios-\nIndice de precios uno atras)*100\n\nPIBR=\n(Producto interno bruto nominal/\nIndice de precios)*100")
        self.txt33.place(x=20,y=60,width=200,height=180)

        self.ventana.mainloop()
        

    
    def PIB(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 180

        self.x_ventana = self.ventana.winfo_screenwidth() - 350 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)
        self.ventana.title("METODOS PARA SACAR EL PIB : ")
        self.ventana.geometry("200x180")
        self.ventana.maxsize(100, 180)
        self.ventana.minsize(200, 180)

        self.frame=tk.Frame(self.ventana,bg="yellow")
        self.frame.pack(expand=True,fill="both")
        
        self.txt=tk.Label(self.frame,text="METODOS :",bg="orange")
        self.txt.place(x=50,y=30,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=80)
        self.combo["values"]=("Metodo del Ingreso","Metodo del Gasto")

        self.boton2=tk.Button(self.frame,text="SELECCIONAR",command=self.PIB1,bd=5)
        self.boton2.place(x=40,y=120,width=120,height=30)

        self.ventana.mainloop()

    def PIB1(self):
        if self.combo.get()=="Metodo del Ingreso":
            self.ventana=tk.Tk()
            self.ancho_ventana = 600
            self.alto_ventana = 650

            self.x_ventana = self.ventanai.winfo_screenwidth() - 440 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)

            self.ventana.title("PIB INGRESO : ")
            self.ventana.geometry("600x650")
            self.ventana.iconbitmap("icono.ico")
            self.ventana.maxsize(600, 650)
            self.ventana.minsize(600, 650)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")
            

            self.txt0=tk.Label(self.frame,text="METODO DEL INGRESO: ",bg="gold",font=self.fontStyle)
            self.txt0.place(x=220,y=30,width=220,height=40)

            self.txt1=tk.Label(self.frame,text="Impuestos Indirectos : ",bg="sky blue")
            self.txt1.place(x=40,y=110,width=230,height=40)

            self.caja1=tk.Entry(self.frame)
            self.caja1.place(x=290,y=110,width=120,height=40)

            self.txt2=tk.Label(self.frame,text="Ingresos de los Propietarios : ",bg="sky blue")
            self.txt2.place(x=40,y=170,width=230,height=40)

            self.caja2=tk.Entry(self.frame)
            self.caja2.place(x=290,y=170,width=120,height=40)

            self.txt3=tk.Label(self.frame,text="Intereses : ",bg="sky blue")
            self.txt3.place(x=40,y=230,width=230,height=40)

            self.caja3=tk.Entry(self.frame)
            self.caja3.place(x=290,y=230,width=120,height=40)

            self.txt4=tk.Label(self.frame,text="Depreciacion : ",bg="sky blue")
            self.txt4.place(x=40,y=290,width=230,height=40)

            self.caja4=tk.Entry(self.frame)
            self.caja4.place(x=290,y=290,width=120,height=40)

            self.txt5=tk.Label(self.frame,text="Beneficios Corporativos : ",bg="sky blue")
            self.txt5.place(x=40,y=350,width=230,height=40)

            self.caja5=tk.Entry(self.frame)
            self.caja5.place(x=290,y=350,width=120,height=40)

            self.txt6=tk.Label(self.frame,text="Renta : ",bg="sky blue")
            self.txt6.place(x=40,y=410,width=230,height=40)

            self.caja6=tk.Entry(self.frame)
            self.caja6.place(x=290,y=410,width=120,height=40)

            self.txt7=tk.Label(self.frame,text="Renumeraciones de los Trabajadores : ",bg="sky blue")
            self.txt7.place(x=40,y=470,width=230,height=40)

            self.caja7=tk.Entry(self.frame)
            self.caja7.place(x=290,y=470,width=120,height=40)

            self.txt8=tk.Label(self.frame,text="Ingresos Neto de los Factores Extranjeros:" ,bg="sky blue")
            self.txt8.place(x=40,y=540,width=230,height=40)

            self.caja8=tk.Entry(self.frame)
            self.caja8.place(x=290,y=540,width=120,height=40)

            self.boton3=tk.Button(self.frame,text="BORRAR TODO",command=self.borrar,bd=5)
            self.boton3.place(x=460,y=300,width=100,height=30)

            self.boton4=tk.Button(self.frame,text="CALCULAR",command=self.CALCULAR,bd=5)
            self.boton4.place(x=460,y=350,width=100,height=30)

   
        elif self.combo.get()=="Metodo del Gasto":
            self.ventana=tk.Tk()
            self.ancho_ventana = 600
            self.alto_ventana = 650

            self.x_ventana = self.ventanai.winfo_screenwidth() - 440 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)

            self.ventana.title("PIB GASTO : ")
            self.ventana.geometry("600x650")
            self.ventana.iconbitmap("icono.ico")
            self.ventana.maxsize(600, 650)
            self.ventana.minsize(600, 650)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")
            

            self.txt0=tk.Label(self.frame,text="METODO DEL GASTO: ",bg="gold",font=self.fontStyle)
            self.txt0.place(x=220,y=30,width=220,height=40)

            self.txt1=tk.Label(self.frame,text="Impuestos Indirectos : ",bg="sky blue")
            self.txt1.place(x=40,y=110,width=230,height=40)

            self.caja1=tk.Entry(self.frame)
            self.caja1.place(x=290,y=110,width=120,height=40)

            self.txt2=tk.Label(self.frame,text="ingreso neto de los factores extranjeros : ",bg="sky blue")
            self.txt2.place(x=40,y=170,width=230,height=40)

            self.caja2=tk.Entry(self.frame)
            self.caja2.place(x=290,y=170,width=120,height=40)

            self.txt3=tk.Label(self.frame,text="Exportaciones : ",bg="sky blue")
            self.txt3.place(x=40,y=230,width=230,height=40)

            self.caja3=tk.Entry(self.frame)
            self.caja3.place(x=290,y=230,width=120,height=40)

            self.txt4=tk.Label(self.frame,text="Depreciacion : ",bg="sky blue")
            self.txt4.place(x=40,y=290,width=230,height=40)

            self.caja4=tk.Entry(self.frame)
            self.caja4.place(x=290,y=290,width=120,height=40)

            self.txt5=tk.Label(self.frame,text="Importaciones : ",bg="sky blue")
            self.txt5.place(x=40,y=350,width=230,height=40)

            self.caja5=tk.Entry(self.frame)
            self.caja5.place(x=290,y=350,width=120,height=40)

            self.txt6=tk.Label(self.frame,text="Gasto de Gobierno : ",bg="sky blue")
            self.txt6.place(x=40,y=410,width=230,height=40)

            self.caja6=tk.Entry(self.frame)
            self.caja6.place(x=290,y=410,width=120,height=40)

            self.txt7=tk.Label(self.frame,text="Gasto en Consumo de las familias : ",bg="sky blue")
            self.txt7.place(x=40,y=470,width=230,height=40)

            self.caja7=tk.Entry(self.frame)
            self.caja7.place(x=290,y=470,width=120,height=40)

            self.boton5=tk.Button(self.frame,text="BORRAR TODO",command=self.borrar2,bd=5)
            self.boton5.place(x=460,y=300,width=100,height=30)

            self.boton6=tk.Button(self.frame,text="CALCULAR",command=self.CALCULAR2,bd=5)
            self.boton6.place(x=460,y=350,width=100,height=30)

            
            #ID=float(input("Dime el impuesto indirecto : "))
           # INFEE=float(input("Dime el ingreso neto de los factores extranjeros : "))
            #E=float(input("Dime las Exportaciones : "))
            #D=float(input("Dime la Depreciacion : "))
            #IM=float(input("Dime las Importaciones : "))
            #GG=float(input("Dime el Gasto de Gobierno : "))
            #GCF=float(input("Dime el Gasto en Consumo de las familias : "))
            #objeto=MetodoDelGasto(ID,INFEE,E,D,IM,GG,GCF)
            #objeto.formulas()
            #objeto.PIB()

    def borrar(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")
        self.caja3.delete(0,"end")
        self.caja4.delete(0,"end")
        self.caja5.delete(0,"end")
        self.caja6.delete(0,"end")
        self.caja7.delete(0,"end")
        self.caja8.delete(0,"end")

    def borrar2(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")
        self.caja3.delete(0,"end")
        self.caja4.delete(0,"end")
        self.caja5.delete(0,"end")
        self.caja6.delete(0,"end")
        self.caja7.delete(0,"end")

    def borrar3(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")



    def CALCULAR(self):
        try:
            II=float(self.caja1.get())
            IP=float(self.caja2.get())
            IN=float(self.caja3.get())
            D=float(self.caja4.get())
            BC=float(self.caja5.get())
            R=float(self.caja6.get())
            RT=float(self.caja7.get())
            INFE=float(self.caja8.get())

            objeto=MetodoDelIngreso(II,IP,IN,D,BC,R,RT,INFE)
            objeto.PIB()
        except:
            messagebox.showerror(message="Ingreso letras en lugar de Numeros :(",title="ERROR ")

        

    def CALCULAR2(self):
        try:
            ID=float(self.caja1.get())
            INFEE=float(self.caja2.get())
            E=float(self.caja3.get())
            D=float(self.caja4.get())
            IM=float(self.caja5.get())
            GG=float(self.caja6.get())
            GCF=float(self.caja7.get())

            objeto=MetodoDelGasto(ID,INFEE,E,D,IM,GG,GCF)
            objeto.PIB()

        except:
            messagebox.showerror(message="Ingreso letras en lugar de Numeros :(",title="ERROR ")

    def CALCULAR3(self):
        try:
            desempleo=float(self.caja1.get())
            PEA=float(self.caja2.get())
            
            objeto=desempleos(desempleo,PEA)
            objeto.calculo()
        except:
            messagebox.showerror(message="Ingreso letras en lugar de Numeros :(",title="ERROR ")



    def TD(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 400
        self.alto_ventana = 300

        self.x_ventana = self.ventanai.winfo_screenwidth() - 440 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("DESEMPLEO : ")
        self.ventana.geometry("400x300")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.maxsize(400, 300)
        self.ventana.minsize(400, 300)

        self.frame=tk.Frame(self.ventana,bg="slate gray")
        self.frame.pack(expand=True,fill="both")
        

        self.txt0=tk.Label(self.frame,text="TASA DE DESEMPLEO: ",bg="gold",font=self.fontStyle)
        self.txt0.place(x=100,y=30,width=200,height=40)

        self.txt1=tk.Label(self.frame,text="Desempleados o \nPoblacion no ocupada : ",bg="sky blue")
        self.txt1.place(x=40,y=80,width=150,height=50)

        self.caja1=tk.Entry(self.frame)
        self.caja1.place(x=220,y=80,width=150,height=50)

        self.txt2=tk.Label(self.frame,text="Fuerza Laboral o \n PEA : ",bg="sky blue")
        self.txt2.place(x=40,y=160,width=150,height=50)

        self.caja2=tk.Entry(self.frame)
        self.caja2.place(x=220,y=160,width=150,height=50)

        self.boton1=tk.Button(self.frame,text="BORRAR TODO",command=self.borrar3,bd=5)
        self.boton1.place(x=80,y=250,width=100,height=30)

        self.boton2=tk.Button(self.frame,text="CALCULAR",command=self.CALCULAR3,bd=5)
        self.boton2.place(x=250,y=250,width=100,height=30)

            
            #objeto=desempleos(desempleo,PEA)
            #objeto.calculo()


    def IIP(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 180

        self.x_ventana = self.ventana.winfo_screenwidth() - 350 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)
        self.ventana.title("AÑOS : ")
        self.ventana.geometry("200x180")
        self.ventana.maxsize(100, 180)
        self.ventana.minsize(200, 180)

        self.frame=tk.Frame(self.ventana,bg="yellow")
        self.frame.pack(expand=True,fill="both")
        
        self.txt=tk.Label(self.frame,text="Cuantos años vas a registrar :",bg="orange")
        self.txt.place(x=20,y=30,width=170,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=80)
        self.combo["values"]=("2","3")

        self.boton2=tk.Button(self.frame,text="SELECCIONAR",command=self.IIP1,bd=5)
        self.boton2.place(x=40,y=120,width=120,height=30)

        self.ventana.mainloop()

    def IIP1(self):
        if self.combo.get()=="2":

            self.ventana=tk.Tk()
            self.ancho_ventana = 700
            self.alto_ventana = 600

            self.x_ventana = self.ventanai.winfo_screenwidth() - 440 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)

            self.ventana.title("DESEMPLEO : ")
            self.ventana.geometry("700x600")
            self.ventana.iconbitmap("icono.ico")
            self.ventana.maxsize(700, 600)
            self.ventana.minsize(700, 600)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")
            

            self.txt0=tk.Label(self.frame,text="AÑOS: ",bg="gold",font=self.fontStyle)
            self.txt0.place(x=250,y=30,width=220,height=40)

            self.txt1=tk.Label(self.frame,text="Ingrese el año 1: ",bg="sky blue")
            self.txt1.place(x=20,y=80,width=100,height=30)

            self.caja1=tk.Entry(self.frame)
            self.caja1.place(x=130,y=80,width=100,height=30)

            self.txt11=tk.Label(self.frame,text="Nivel de precios del año 1: ",bg="sky blue")
            self.txt11.place(x=350,y=80,width=170,height=30)

            self.caja11=tk.Entry(self.frame)
            self.caja11.place(x=550,y=80,width=100,height=30)

            self.txt2=tk.Label(self.frame,text="Ingrese el Año 2 ",bg="sky blue")
            self.txt2.place(x=20,y=160,width=100,height=30)

            self.caja2=tk.Entry(self.frame)
            self.caja2.place(x=130,y=160,width=100,height=30)

            self.txt3=tk.Label(self.frame,text="Año base",bg="sky blue")
            self.txt3.place(x=310,y=300,width=100,height=30)

            self.caja3=tk.Entry(self.frame)
            self.caja3.place(x=310,y=340,width=100,height=30)

        #self.boton1=tk.Button(self.frame,text="BORRAR TOD",command=self.borrar4,bd=5)
        #self.boton1.place(x=80,y=250,width=100,height=30)

        #self.boton2=tk.Button(self.frame,text="CALCULAR",command=self.CALCULAR4,bd=5)
        #self.boton2.place(x=250,y=250,width=100,height=30)
        
        
    def CALCULAR4(self):
        pass
        
        listaAño=[]
        contador1=1
        listaNivel=[]
        listaPIBN=[]
        listaIndice=[]
        listaInflacion=[]
        listaPIBR=[]
        contador=0
        contadoor=0
        cuantos=int(input("Cuantos Años vas a registrar : "))
        print(separador)
        for año in range(cuantos):
            año=int(input("Ingresa el Año : "))
            listaAño.append(año)
            
       
        base=int(input("Cual es el indice del año base : "))
        baseo=(base-1)
        
            
        for precio in range(cuantos):
            nivel_precios=float(input(f"Ingresa el Nivel de Precios del Año {listaAño[contador]} :"))
            listaNivel.append(nivel_precios)
            contador=contador+1
        print(separador)
            
        for producto in range(cuantos):
            PIBN=float(input(f"Ingrese el Producto Interno Bruto Nominal del Año {listaAño[contadoor]} : "))
            listaPIBN.append(PIBN)
            contadoor=contadoor+1
        print(separador)
        
     
        indice(listaNivel,listaIndice,baseo,listaAño)
        inflacion(listaIndice,listaAño,cuantos,listaInflacion)
        PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos)
   
        
       
        

            
    
app=Aplicacion()