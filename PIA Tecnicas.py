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
        self.ventanai.iconbitmap("Multimedia\\num.ico")

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
        self.ventana.iconbitmap("Multimedia\\num.ico")

        self.x_ventana = self.ventana.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana.geometry(self.posicion)

        self.ventana.title("OP")
        self.ventana.maxsize(200, 200)
        self.ventana.minsize(200, 200)
        self.ventana.geometry("200x200")

        self.frame=tk.Frame(self.ventana,bg="red2")
        self.frame.pack(expand=True,fill="both")

        self.label=tk.Label(self.frame,text=" De Decimal a ->",bg="gold2")
        self.label.place(x=50,y=20,width=100,height=30)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=30,y=100)
        self.combo["values"]=("Binario","Octagonal","Hexagonal")

        self.boton01=tk.Button(self.frame,text="CHECAR",command=self.checar,bd=5)
        self.boton01.place(x=30,y=160,width=140,height=30)
        self.ventana.mainloop()
        
    def checar(self):
        if self.combo.get()=="Binario":
            self.ventana5=tk.Tk()
            self.ventana5.title("Contar : ")
            self.ventana5.iconbitmap("Multimedia\\num.ico")
            self.ancho_ventana = 200
            self.alto_ventana = 200

            self.x_ventana = self.ventana5.winfo_screenwidth() - 310 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="red2")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Numero a Convertir: ",bg="gold2")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="BUSCAR",command=self.De_a_bi,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()

        elif self.combo.get()=="Octagonal":
            self.ventana5=tk.Tk()
            self.ventana5.title("Contar : ")
            self.ventana5.iconbitmap("Multimedia\\funcion.ico")
            self.ancho_ventana = 200
            self.alto_ventana = 200

            self.x_ventana = self.ventana5.winfo_screenwidth() - 310 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="red2")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Numero a Convertir : ",bg="gold2")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="BUSCAR",command=self.De_a_oct,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()

        elif self.combo.get()=="Hexagonal":
            self.ventana5=tk.Tk()
            self.ventana5.title("Contar : ")
            self.ventana5.iconbitmap("Multimedia\\funcion.ico")
            self.ancho_ventana = 200
            self.alto_ventana = 200

            self.x_ventana = self.ventana5.winfo_screenwidth() - 310 - self.ancho_ventana // 2
            self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana5.geometry(self.posicion)

            self.ventana5.geometry("200x200")
            self.ventana5.maxsize(200, 200)
            self.ventana5.minsize(200, 200)

            self.frame4=tk.Frame(self.ventana5,bg="red2")
            self.frame4.pack(expand=True,fill="both")

            self.txt001=tk.Label(self.frame4,text="Numero a Convertir: ",bg="gold2")
            self.txt001.place(x=30,y=30,width=140,height=30)

            self.caja000=tk.Entry(self.frame4)
            self.caja000.place(x=50,y=80,width=100,height=30)

            self.boton11=tk.Button(self.frame4,text="BUSCAR",command=self.De_a_hex,bd=5)
            self.boton11.place(x=40,y=130,width=120,height=30)
            self.ventana5.mainloop()

    
        

    def De_a_bi(self):
        try:
            self.numero=int(self.caja000.get())
            self.numeroO=int(self.caja000.get())
            lista=[]
            while self.numero>=1:
                lista.insert(0,self.numero%2)
                self.numero=self.numero//2
        
            resultado="".join(str(i) for i in lista)
            messagebox.showinfo(message=f"Numero Decimal -> {self.numeroO}\nNumero Binario -> {resultado}",title=" Decimal -> Binario")

        except:
            messagebox.showerror(message="Ingreso mal el dato :(",title="ERROR")

    def De_a_oct(self):
        try:
            self.numero=int(self.caja000.get())
            self.numeroO=int(self.caja000.get())
            lista=[]
            while self.numero>=1:
                lista.insert(0,self.numero%8)
                self.numero=self.numero//8
        
            resultado="".join(str(i) for i in lista)
            messagebox.showinfo(message=f"Numero Decimal -> {self.numeroO}\nNumero Octagonal -> {resultado}",title=" Decimal -> Octagonal")

        except:
            messagebox.showerror(message="Ingreso mal el dato :(",title="ERROR")

            




    def De_a_hex(self):
        try:
            self.numero=int(self.caja000.get())
            self.numeroO=int(self.caja000.get())

            hexadecimal=hex(self.numero)
            hexadecimal=format(self.numero,"0X")
            resultado=(hexadecimal)

            messagebox.showinfo(message=f"Numero Decimal -> {self.numeroO}\nNumero Hexagonal -> {resultado}",title=" Decimal -> Hexagonal")

        except:
            messagebox.showerror(message="Ingreso mal el dato :(",title="ERROR")


    def binario(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("Convertir: ")
        self.ventana5.iconbitmap("Multimedia\\num.ico")
        self.ancho_ventana = 200
        self.alto_ventana = 200

        self.x_ventana = self.ventana5.winfo_screenwidth() - 610 - self.ancho_ventana // 2
        self.y_ventana = self.ventana5.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventana5.geometry(self.posicion)

        self.ventana5.geometry("200x200")
        self.ventana5.maxsize(200, 200)
        self.ventana5.minsize(200, 200)

        self.frame4=tk.Frame(self.ventana5,bg="red2")
        self.frame4.pack(expand=True,fill="both")

        self.txt001=tk.Label(self.frame4,text="Numero a Convertir: ",bg="gold2")
        self.txt001.place(x=30,y=30,width=140,height=30)

        self.caja000=tk.Entry(self.frame4)
        self.caja000.place(x=50,y=80,width=100,height=30)

        self.boton11=tk.Button(self.frame4,text="BUSCAR",command=self.BinarioADecimal,bd=5)
        self.boton11.place(x=40,y=130,width=120,height=30)
        self.ventana5.mainloop()


    def BinarioADecimal(self):
        try:
            numero=self.caja000.get()
            self.numeroO=int(self.caja000.get())
            cadena=numero[::-1]
            salida=0;contador=0
            while contador<len(cadena):
                if int(cadena[contador])==1:
                    salida+=int(cadena[contador])*2**contador
                contador+=1

            messagebox.showinfo(message=f"Numero Binario -> {self.numeroO}\nNumero Decimal -> {salida}",title=" Binario -> Decimal")

        except:
            messagebox.showerror(message="Ingreso mal el dato :(",title="ERROR")

    
    
        
                
    


    


    

app = Aplicacion()





        
         

       
            
        
    