import sys 
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import pandas as pd

class Aplicacion():
    def __init__(self):
        self.ventanai=tk.Tk()
        self.ancho_ventana = 300
        self.alto_ventana = 300

        self.x_ventana = self.ventanai.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventanai.geometry(self.posicion)
        self.ventanai.title("BIENVENIDO :) ")
        self.ventanai.geometry("300x300")
        self.ventanai.maxsize(300, 300)
        self.ventanai.minsize(300, 300)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=10)
        #self.ventanai.iconbitmap("Multimedia\\num.ico")

        self.frame=tk.Frame(self.ventanai,bg="slate gray")
        self.frame.pack(expand=True,fill="both")

        self.framee=tk.Frame(self.ventanai,bg="royal blue")
        self.framee.place(x=0,y=0,width=300,height=50)

        self.txt01=tk.Label(self.framee,text="BIENVENIDO AL MANEJADOR DE CSV",background="gold",font=self.fontStyle)
        self.txt01.place(x=30,y=10,width=250,height=30)

        self.txt02=tk.Label(self.frame,text="Ingresa el nombre del Archivo CSV:")
        self.txt02.place(x=50,y=70,width=200,height=30)

        self.caja0=tk.Entry(self.frame)
        self.caja0.place(x=50,y=110,width=200,height=30)

        self.txt03=tk.Label(self.frame,text=".csv")
        self.txt03.place(x=255,y=120,width=30,height=20)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=50,y=160,width=200,height=30)
        self.combo["values"]=("ChecarEncabezadosDelCSV","ChecarElCsv","Graficar")

        self.boton1=tk.Button(self.frame,text="Realizar",command=self.realizar,bd=5)
        self.boton1.place(x=50,y=210,width=200,height=30)

    
        self.ventanai.mainloop()

    def realizar(self):
        try:
            if self.combo.get()=="ChecarEncabezadosDelCSV":
                try:
                    ex=self.caja0.get()
                    excel=ex+".csv"
                    notas=pd.read_csv(excel)
                    
                    self.ventana=tk.Tk()
                    self.ventana.title("ENCABEZADOS :) ")
                    self.ancho_ventana = 300
                    self.alto_ventana = 300

                    self.x_ventana = self.ventanai.winfo_screenwidth() - 500 - self.ancho_ventana // 2
                    self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana.geometry(self.posicion)
                
                    self.ventana.maxsize(300, 300)
                    self.ventana.minsize(300, 300)
                    self.scrollbar=tk.Scrollbar(self.ventana)
                    self.scrollbar.pack(side="right",fill="y")
                    contadorE=1
                    contador=0
                    self.mylist=tk.Listbox(self.ventana,yscrollcommand=self.scrollbar.set)
                    for i in notas.columns:
                        encabezado="Encabezado"+str(contadorE)+" : "+str(i)
                        self.mylist.insert(contador,encabezado)
                        contadorE=contadorE+1
                        contador=contador+1
                    self.mylist.pack(side="top",fill="both",expand=True)
                    self.scrollbar.config(command=self.mylist.yview)
                    self.ventana.mainloop()
                except:
                    messagebox.showerror(message="Archivo no Encontrado",title="ERROR")
            
            elif self.combo.get()=="ChecarElCsv":
                try:
                    ex=self.caja0.get()
                    excel=ex+".csv"
                    notas=pd.read_csv(excel)

                    encabezados=[]
                    for i in notas.columns:
                        encabezados.append(i)

                    self.ventana9=tk.Tk()
                    self.ancho_ventana = 790
                    self.alto_ventana = 200

                    self.x_ventana = self.ventana9.winfo_screenwidth() - 410 - self.ancho_ventana // 2
                    self.y_ventana = self.ventana9.winfo_screenheight() - 500 - self.alto_ventana // 2
                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana9.geometry(self.posicion)

                    self.ventana9.title("CSV:")
                    self.ventana9.geometry("800x500")
                
                    self.ventana9.maxsize(800, 500)
                    self.ventana9.minsize(800, 500)
                    self.frame09=tk.Frame(self.ventana9,bd=4,relief="ridge",bg="crimson")
                    self.frame09.pack(expand=True,fill="both")

                    self.scroll_x=tk.Scrollbar(self.frame09,orient="horizontal")
                    self.scroll_y=tk.Scrollbar(self.frame09,orient="vertical")

                    self.Empleado_Tabla=ttk.Treeview(self.frame09,columns=encabezados,xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                    self.scroll_x.pack(side="bottom",fill="x")
                    self.scroll_y.pack(side="right",fill="y")
                    self.scroll_x.config(command=self.Empleado_Tabla.xview)
                    self.scroll_y.config(command=self.Empleado_Tabla.yview)

                    for titulo in encabezados:
                        self.Empleado_Tabla.heading(str(titulo),text=str(titulo))
                    
                    self.Empleado_Tabla['show']='headings'
                    for titulo in encabezados:
                        self.Empleado_Tabla.column(str(titulo),width=100)

                    index = iid = 0
                    notas2=pd.read_csv(excel)
                    for elemento in notas2.values:
                        self.Empleado_Tabla.insert("", index, iid, values=elemento)
                        index = iid = index + 1

                    self.Empleado_Tabla.pack(fill="both",expand=1)
                    self.ventana9.mainloop()
                
                except:
                    messagebox.showerror(message="Archivo no Encontrado",title="ERROR")
                    

            elif self.combo.get()=="Graficar":
                try:
                    ex=self.caja0.get()
                    excel=ex+".csv"
                    notas=pd.read_csv(excel)

                    self.ventana=tk.Tk()
                    self.ventana.title("Graficos")
                    self.ancho_ventana = 200
                    self.alto_ventana = 200

                    self.x_ventana = self.ventanai.winfo_screenwidth() - 750 - self.ancho_ventana // 2
                    self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

                    self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
                    self.ventana.geometry(self.posicion)
                
                    self.ventana.maxsize(200, 200)
                    self.ventana.minsize(200, 200)

                    self.frame=tk.Frame(self.ventana,bg="slate gray")
                    self.frame.pack(expand=True,fill="both")
                    
                    self.txt1=tk.Label(self.frame,text="Eliga el Grafico que desee")
                    self.txt1.place(x=20,y=20,width=150,height=30)

                    self.combo2=ttk.Combobox(self.frame)
                    self.combo2.place(x=20,y=90,width=150,height=30)
                    self.combo2["values"]=("Pastel","Barras")

                    self.botong=tk.Button(self.frame,text="Realizar",command=self.grafica)
                    self.botong.place(x=20,y=140,width=150,height=30)
                    self.ventana.mainloop()

                except:
                    messagebox.showerror(message="Archivo no Encontrado",title="ERROR")

        except:
            messagebox.showerror(message="Archivo no Encontrado",title="ERROR")

    def grafica(self):
        if self.combo2.get()=="Pastel":
            self.ventana=tk.Tk()
            self.ventana.title("Graficos")
            self.ancho_ventana = 400
            self.alto_ventana = 400

            self.x_ventana = self.ventanai.winfo_screenwidth() - 500 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)
        
            self.ventana.maxsize(400, 400)
            self.ventana.minsize(400, 400)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")
            
            self.txt1=tk.Label(self.frame,text="Eliga la etiqueta del Nombre:")
            self.txt1.place(x=20,y=20,width=150,height=30)

            self.caja1=tk.Entry(self.frame)
            self.caja1.place(x=20,y=60,width=150,height=30)

            self.ventana.mainloop()
        
        
        

            
                


        #except:
           # messagebox.showerror(message="No se pueden graficar\nDe esa forma por los tipos de valores",title="ERROR")
        

            
                
            




app=Aplicacion()

#ex=self.caja0.get()
#excel=ex+".csv"
#notas=pd.read_csv(excel)

#nombre=notas[etiqueta1].unique()
#valor=notas[etiqueta2].unique()

#Graficamos
#plt.pie(valor,labels=nombre,autopct="%1.1f %%",shadow=True, startangle=90)
#plt.title(titulo)
#plt.legend()
#plt.show()
#except:
#messagebox.showerror(message="Favor de validar el nombre y el valor de las etiquetas",title="ERROR")
