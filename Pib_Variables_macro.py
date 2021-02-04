import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk



class desempleos:
    def __init__ (self,desempleados,PEA):
        self.__desempleados=desempleados
        self.__PEA=PEA
    
    
    def calculo(self):
        archivoA=open("./archivos/datos.txt" , 'a')
        resultado=(self.__desempleados/self.__PEA)*100
        textoa=str(resultado)
        print(f"La tasa de Desempleo es : {resultado}")
        archivoA.write("RESPUESTA DE LA TASA DE DESEMPLEO :)" +"\n" )
        archivoA.write("TASA DE DESEMPLEO = " + textoa +  "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()


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
        
          
    def formulas(self):
        print("-"*40)
        print("IN=(Rt+R+In+Ip+Bc)")
        print("PIB=(IN+IIE+dep+INFE)")
        print("-"*40)

    
    def PIB(self):
        IN=(self.__RT+self.__R+self.__IN+self.__IP+self.__BC)
        pib=(IN+self.__II+self.__D+self.__INFE)
        textoa=str(IN)
        textob=str(pib)
        print("")
        print("¿¿¿RESPUESTAS???:")
        print(f"Ingreso Nacional(IN) = {IN}  ")
        print(f"Producto Interno Bruto(PIB) = {pib} ")
        archivoA=open("./archivos/datos.txt" , 'a')
        archivoA.write("RESPUESTAS DEL METODO DEL INGRESO :)" +"\n" )
        archivoA.write("Ingreso Nacional(IN) = " + textoa +  "\n" )
        archivoA.write("Producto Interno Bruto(PIB) =" + textob + "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        print("")

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
        
    
    def formulas(self):
        print("-"*40)
        print("Estas son las Formulas ")
        print("Xn=(E-I)")
        print("PIB=(C+I+G+Xn)")
        print("IN=(PIN-ingreso neto de los factores-impuestos indirectos)")
        print("-"*40)
    
    
    def PIB(self):
        XN=(self.__E-self.__IM)
        pib=(self.__GCF+self.__INFEE+self.__GG+XN)
        PIN=(pib-self.__D)
        IN=(PIN-self.__INFEE-self.__ID)
        textoa=str(pib)
        textob=str(PIN)
        textoc=str(IN)
        print("¿¿¿RESPUESTAS???:")
        print(f"Producto Interno Bruto(PIB) = {pib} ")
        print(f"Producto Interno Neto(PIN) = {PIN}  ")
        print(f"Ingreso Nacional(IN) = {IN}  ")
        print("")

        archivoA=open("./archivos/datos.txt" , 'a')
        archivoA.write("RESPUESTAS DEL METODO DEL GASTO :)" +"\n" )
        archivoA.write("Producto Interno Bruto(PIB) =" + textoa +  "\n" )
        archivoA.write("Producto Interno Neto(PIN) = " + textob +  "\n" )
        archivoA.write("Ingreso Nacional(IN) =" + textoc +  "\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        
    
    


#VARIABLES MACROECONOMICAS
def formulas():
    print("*Indice de Precios : "+ "=" +"(NIVEL DE PRECIOS / BASE DE NIVEL DE PRECIOS * 100")
    print("*Inflacion : "+ "=" + "INDICE DE PRECIOS – INDICE DE PRECIOS UNO ATRÁS / INDICE DE PRECIOS UNO ATRÁS * 100")
    print("*PIBR : " + "=" + "PRODUCTO INTERNO BRUTO NOMINAL / INDICE DE PRECIOS * 100")

    
def indice(listaNivel,listaIndice,baseo,listaAño):
    archivoA=open("./archivos/datos.txt" , 'a')
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
    archivoA=open("./archivos/datos.txt" , 'a')
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
        print("INFLACION : ")
        print(f"La Inflacion del año {listaAño[contadorA]} es = {numero}")
        textoa=str(numero)
        archivoA.write("Inflacion = " + textoa +  "\n" )
        contadorA=contadorA+1
        print(separador)
        print("")
    archivoA.close()


def PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos):
    archivoA=open("./archivos/datos.txt" , 'a')
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

        self.ventanai.mainloop()
    
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



            #self.frame2=tk.Frame(self.ventana,bg="deep sky blue")
            #self.frame2.place(x=380,y=510,width=230,height=100)
            #self.frame2.config(cursor="pencil")

           
            #II=float(input("Dime los Impuestos Indirectos : "))
            #IP=float(input("Dime los Ingresos de los Propietarios : "))
            #IN=float(input("Dime los Intereses : "))
            #D=float(input("Dime la Depreciacion : "))
            #BC=float(input("Dime los Beneficios Corporativos : "))
            #R=float(input("Dime la Renta : "))
            #RT=float(input("Dime la Remuneraciones de los trabajadores : "))
            #INFE=float(input("Dime el Ingreso Neto de los Factores Extranjeros : "))
            #objeto=MetodoDelIngreso(II,IP,IN,D,BC,R,RT,INFE)
            #objeto.formulas()
            #objeto.PIB()
            
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

    def TD(self):
            desempleo=int(input("Ingresa los Desempleados o la poblacion no ocupada : "))
            PEA=int(input("Ingresa La Fueza Laboral o PEA : "))
            objeto=desempleos(desempleo,PEA)
            objeto.calculo()
            print(separador)
            print("")
            print("1=SI\n2=NO")
            opcion=int(input("Deseas regresar al Menu Principal : "))
            print("")

    def IIP(self):
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
            
        print(separador)
        for año in listaAño:
            print(f"{contador1}-{año}")
            contador1=contador1+1
        base=int(input("Cual es el indice del año base : "))
        baseo=(base-1)
        print(separador)
        
            
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
        
        print("")
        print(separador)
        print("Estas son las Formulas :) ")
        formulas()
        print(separador)
        print("")
        
        print(separador)
        indice(listaNivel,listaIndice,baseo,listaAño)
        print(separador)
        print("")
        
        print(separador)
        inflacion(listaIndice,listaAño,cuantos,listaInflacion)
        print("")
        
        print(separador)
        PIBR(listaPIBN,listaIndice,listaPIBR,listaAño,cuantos)
        print("")
        
        print(separador)
        print("")
        print("1=SI\n2=NO")
        opcion=int(input("Deseas regresar al Menu Principal : "))
        print("")
        

            
    
app=Aplicacion()