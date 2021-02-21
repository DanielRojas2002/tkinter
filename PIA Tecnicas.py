import sys 
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox

class Aplicacion():
    def __init__(self):
        self.ventanai=tk.Tk()
        self.ancho_ventana = 500
        self.alto_ventana = 500

        self.x_ventana = self.ventanai.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventanai.geometry(self.posicion)
        self.ventanai.title("BIENVENIDO AL Convertidor de Numeros: ")
        self.ventanai.geometry("500x500")
        self.ventanai.maxsize(500, 500)
        self.ventanai.minsize(500, 500)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.ventanai.iconbitmap("Multimedia\\icono.ico")

        self.frame=tk.Frame(self.ventanai,bg="slate gray")
        self.frame.pack(expand=True,fill="both")

        self.framee=tk.Frame(self.ventanai,bg="royal blue")
        self.framee.place(x=0,y=0,width=600,height=120)

        self.txt0101=tk.Label(self.framee,text="Conversor de Numeros",background="gold",font=self.fontStyle)
        self.txt0101.place(x=20,y=10,width=450,height=100)

    
        self.image=tk.PhotoImage(file="Multimedia\\numero.gif")
        self.txt=tk.Label(image=self.image)
        self.txt.place(x=100,y=170)


        self.frame2=tk.Frame(self.ventanai,bg="deep sky blue")
        self.frame2.place(x=0,y=400,width=500,height=100)
        self.frame2.config(cursor="hand1")

        self.botonDecimal=tk.Button(self.frame2,text="DECIMAL",command=self.Decimal,bd=5)
        self.botonDecimal.place(x=80,y=40,width=100,height=30)

        self.botonb=tk.Button(self.frame2,text="BINARIO",command=self.binario,bd=5)
        self.botonb.place(x=300,y=40,width=100,height=30)

        self.ventanai.mainloop()

    def Decimal(self):
        self.ventana=tk.Tk()
        self.ancho_ventana = 200
        self.alto_ventana = 200
        self.ventana.iconbitmap("Multimedia\\filtro.ico")

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

        self.label=tk.Label(self.frame,text="FUNCIONES : ",bg="gold2")
        self.label.place(x=50,y=20,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=100)
        self.combo["values"]=("Binario","Octagonal","Hexagonal")

        self.boton01=tk.Button(self.frame,text="CHECAR",command=self.checar,bd=5)
        self.boton01.place(x=30,y=160,width=140,height=30)
        self.ventana.mainloop()
        
    def checar(self):
        pass

    def binario(self):
        pass


app = Aplicacion()




def BinarioADecimalAOCyHE(numero):
    cadena=numero[::-1]
    salida=0;contador=0
    while contador<len(cadena):
        if int(cadena[contador])==1:
            salida+=int(cadena[contador])*2**contador
        contador+=1

    print("El resultado en Decimal es :  ",salida)
    print("*"*40)
    print("1=Este numero Decimal lo quiero convertir a Octagonal ")
    print("2=Este numero Decimal lo quiero convertir a Hexadecimal ")
    eleccion=int(input(":"))
    if eleccion==1:
        lista=[]
        while salida>=1:
            lista.insert(0,salida%8)
            salida=salida//8
  
        resultado="".join(str(i) for i in lista)
        print("Este es el numero convertido en Octagonal : ",resultado)
        
        
        
   
    elif eleccion==2:
        lista=[]
        while salida>=1:
            lista.insert(0,salida%16)
            salida=salida//16
        resultado1="".join(str(i) for i in lista)
        print("Toma en cuenta que :")
        print("10=A")
        print("11=B")
        print("12=C")
        print("13=D")
        print("14=E")
        print("15=F")
        print("16=G")
        
        print("Este es el numero convertido en Hexadecimal : ",resultado1)
        
        

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    

def DecimalABinario(numero):
    lista=[]
    while numero>=1:
        lista.insert(0,numero%2)
        numero=numero//2
  
    resultado="".join(str(i) for i in lista)
    print("Este es el numero convertido en Binario : ",resultado)


def DecimalAOctagonal(numero):
    lista=[]
    while numero>=1:
        lista.insert(0,numero%8)
        numero=numero//8
    
    resultado="".join(str(i) for i in lista)
    print("Este es el numero convertido en Octagonal : ",resultado)


def DecimalAHexadecimal(numero):
    lista=[]
    while numero>=1:
        lista.insert(0,numero%16)
        numero=numero//16
  
    resultado="".join(str(i) for i in lista)
    print("Toma en cuenta que :")
    print("10=A")
    print("11=B")
    print("12=C")
    print("13=D")
    print("14=E")
    print("15=F")
    print("16=G")
    print("Este es el numero convertido en Hexadecimal : ",resultado)



menu=1
while menu==1:
    print("*"*20,"MENU","*"*20)
    print("1=Quiero sacar del Sistema Binario , lo quiero convertir a Sistema Decimal")
    print("2=Quiero sacar del Sistema Decimal , lo quiero convertir a Sistema Binario")
    print("3=Quiero sacar del Sistema Decimal , lo quiero convertir a Sistema Octagonal")
    print("4=Quiero sacar del Sistema Decimal , lo quiero convertir a Sistema Hexagonal")
    opcion=int(input(":"))
    if opcion==1:
        numero=(input("Ingrese el numero Binario para convertirlo a Decimal : "))
        BinarioADecimalAOCyHE(numero)
        print("Quieres regresar al MENU : ")
        print("1=SI")
        print("2=NO")
        menu=int(input(":"))
        
    elif opcion==2:
        numero=int(input("Ingrese un numero en sistema Decimal : "))
        DecimalABinario(numero)
        print("Quieres regresar al MENU : ")
        print("1=SI")
        print("2=NO")
        menu=int(input(":"))
        
    elif opcion==3:
        numero=int(input("Ingrese un numero en sistema Decimal : "))
        DecimalAOctagonal(numero)
        print("Quieres regresar al MENU : ")
        print("1=SI")
        print("2=NO")
        menu=int(input(":"))
        
    elif opcion==4:
         numero=int(input("Ingrese un numero en sistema Decimal : "))
         DecimalAHexadecimal(numero)
         print("Quieres regresar al MENU : ")
         print("1=SI")
         print("2=NO")
         menu=int(input(":"))
        
         

       
            
        
    