import sys 
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import dates as mpl_dates

class Aplicacion():
    def __init__(self):
        self.ventanai=tk.Tk()
        self.ancho_ventana = 360
        self.alto_ventana = 300

        self.x_ventana = self.ventanai.winfo_screenwidth() - 1050 - self.ancho_ventana // 2
        self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
        self.ventanai.geometry(self.posicion)
        self.ventanai.title("VECTOR CASA DE BOLSA SA DE CV")
        self.ventanai.geometry("360x300")
        self.ventanai.maxsize(360, 300)
        self.ventanai.minsize(360, 300)
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=10)
        #self.ventanai.iconbitmap("Multimedia\\num.ico")

        self.frame=tk.Frame(self.ventanai,bg="slate gray")
        self.frame.pack(expand=True,fill="both")

        self.framee=tk.Frame(self.ventanai,bg="royal blue")
        self.framee.place(x=0,y=0,width=360,height=50)

        self.txt01=tk.Label(self.framee,text="GRAFICAS DE PROMOCION",background="gold",font=self.fontStyle)
        self.txt01.place(x=30,y=10,width=300,height=30)

        self.txt02=tk.Label(self.frame,text="Ingresa el nombre del Archivo CSV:")
        self.txt02.place(x=50,y=70,width=250,height=30)

        self.caja0=tk.Entry(self.frame)
        self.caja0.place(x=50,y=110,width=250,height=30)

        self.txt03=tk.Label(self.frame,text=".csv")
        self.txt03.place(x=310,y=120,width=30,height=20)

        self.combo=ttk.Combobox(self.frame)
        self.combo.place(x=50,y=160,width=250,height=30)
        self.combo["values"]=("ChecarEncabezadosDelCSV","ChecarElCsv","Graficar")

        self.boton1=tk.Button(self.frame,text="Realizar",bd=5,command=self.realizar)
        self.boton1.place(x=50,y=210,width=250,height=30)

    
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
                    self.combo2["values"]=("Pastel","Barras","Tendencia(Usuario)","Tendencia(General)")

                    self.botong=tk.Button(self.frame,text="Realizar",bd=5,command=self.grafica)
                    self.botong.place(x=20,y=140,width=150,height=30)
                    self.ventana.mainloop()

                except:
                    messagebox.showerror(message="Archivo no Encontrado",title="ERROR")

        except:
            messagebox.showerror(message="Archivo no Encontrado",title="ERROR")

    def grafica(self):
        if self.combo2.get()=="Pastel":
            self.ventana=tk.Tk()
            self.ventana.title("Datos necesarios para graficar(Pastel)")
            self.ancho_ventana = 400
            self.alto_ventana = 250

            self.x_ventana = self.ventanai.winfo_screenwidth() - 300 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)
        
            self.ventana.maxsize(400, 250)
            self.ventana.minsize(400, 250)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")

            self.txt0=tk.Label(self.frame,text="Ingrese los Datos para poder Graficar :)")
            self.txt0.place(x=80,y=20,width=250,height=30)
            
            self.txt1=tk.Label(self.frame,text="Ingrese el Titulo del Grafico:")
            self.txt1.place(x=20,y=60,width=180,height=30)

            self.cajatit=tk.Entry(self.frame)
            self.cajatit.place(x=230,y=60,width=120,height=30)

            self.txt2=tk.Label(self.frame,text="Eliga la etiqueta del Nombre:")
            self.txt2.place(x=20,y=110,width=180,height=30)

            self.cajanom=tk.Entry(self.frame)
            self.cajanom.place(x=230,y=110,width=120,height=30)

            self.txt3=tk.Label(self.frame,text="Eliga la etiqueta del Valor:")
            self.txt3.place(x=20,y=160,width=180,height=30)

            self.cajaval=tk.Entry(self.frame)
            self.cajaval.place(x=230,y=160,width=120,height=30)

            self.botongraficar=tk.Button(self.frame,text="GRAFICAR",bd=5,command=self.GRAFICARP)
            self.botongraficar.place(x=150,y=210,width=100,height=30)

            self.ventana.mainloop()

        elif self.combo2.get()=="Barras":
            self.ventana=tk.Tk()
            self.ventana.title("Datos necesarios para graficar(Barras)")
            self.ancho_ventana = 400
            self.alto_ventana = 250

            self.x_ventana = self.ventanai.winfo_screenwidth() - 300 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)
        
            self.ventana.maxsize(400, 250)
            self.ventana.minsize(400, 250)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")

            self.txt0=tk.Label(self.frame,text="Ingrese los Datos para poder Graficar :)")
            self.txt0.place(x=80,y=20,width=250,height=30)
            
            self.txt1=tk.Label(self.frame,text="Ingrese el Titulo del Grafico:")
            self.txt1.place(x=20,y=60,width=180,height=30)

            self.cajatit=tk.Entry(self.frame)
            self.cajatit.place(x=230,y=60,width=120,height=30)

            self.txt2=tk.Label(self.frame,text="Eliga la etiqueta del Nombre:")
            self.txt2.place(x=20,y=110,width=180,height=30)

            self.cajanom=tk.Entry(self.frame)
            self.cajanom.place(x=230,y=110,width=120,height=30)

            self.txt3=tk.Label(self.frame,text="Eliga la etiqueta del Valor:")
            self.txt3.place(x=20,y=160,width=180,height=30)

            self.cajaval=tk.Entry(self.frame)
            self.cajaval.place(x=230,y=160,width=120,height=30)

            self.botongraficar=tk.Button(self.frame,text="GRAFICAR",bd=5,command=self.GRAFICARB)
            self.botongraficar.place(x=150,y=210,width=100,height=30)

            self.ventana.mainloop()

        elif self.combo2.get()=="Tendencia(Usuario)":
            self.ventana=tk.Tk()
            self.ventana.title("Datos necesarios para graficar(Tendencia(Individual))")
            self.ancho_ventana = 400
            self.alto_ventana = 380

            self.x_ventana = self.ventanai.winfo_screenwidth() - 300 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)
        
            self.ventana.maxsize(400, 380)
            self.ventana.minsize(400, 380)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")

            self.txt0=tk.Label(self.frame,text="Ingrese los Datos para poder Graficar :)")
            self.txt0.place(x=80,y=20,width=250,height=30)
            
            self.txt1=tk.Label(self.frame,text="Ingrese el Titulo del Grafico:")
            self.txt1.place(x=20,y=60,width=180,height=30)

            self.cajatit=tk.Entry(self.frame)
            self.cajatit.place(x=230,y=60,width=120,height=30)

            self.txt2=tk.Label(self.frame,text="Eliga la etiqueta del Nombre:")
            self.txt2.place(x=20,y=110,width=180,height=30)

            self.cajanom=tk.Entry(self.frame)
            self.cajanom.place(x=230,y=110,width=120,height=30)

            self.txt22=tk.Label(self.frame,text="Ingrese el Nombre del Usuario:")
            self.txt22.place(x=20,y=160,width=180,height=30)

            self.cajanombre=tk.Entry(self.frame)
            self.cajanombre.place(x=230,y=160,width=120,height=30)

            self.txt3=tk.Label(self.frame,text="Eliga la etiqueta del Valor:")
            self.txt3.place(x=20,y=210,width=180,height=30)

            self.cajaval=tk.Entry(self.frame)
            self.cajaval.place(x=230,y=210,width=120,height=30)

            self.txt4=tk.Label(self.frame,text="Eliga la etiqueta del Tiempo:")
            self.txt4.place(x=20,y=260,width=180,height=30)

            self.cajatiempo=tk.Entry(self.frame)
            self.cajatiempo.place(x=230,y=260,width=120,height=30)

            self.botongraficar=tk.Button(self.frame,text="GRAFICAR",bd=5,command=self.GRAFICARTU)
            self.botongraficar.place(x=150,y=310,width=100,height=30)

            self.ventana.mainloop()


        elif self.combo2.get()=="Tendencia(General)":
            self.ventana=tk.Tk()
            self.ventana.title("Datos necesarios para graficar(Barras)")
            self.ancho_ventana = 400
            self.alto_ventana = 300

            self.x_ventana = self.ventanai.winfo_screenwidth() - 300 - self.ancho_ventana // 2
            self.y_ventana = self.ventanai.winfo_screenheight() // 2 - self.alto_ventana // 2

            self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.ventana.geometry(self.posicion)
        
            self.ventana.maxsize(400, 300)
            self.ventana.minsize(400, 300)

            self.frame=tk.Frame(self.ventana,bg="slate gray")
            self.frame.pack(expand=True,fill="both")

            self.txt0=tk.Label(self.frame,text="Ingrese los Datos para poder Graficar(Tendencia) :)")
            self.txt0.place(x=60,y=20,width=280,height=30)
            
            self.txt1=tk.Label(self.frame,text="Ingrese el Titulo del Grafico:")
            self.txt1.place(x=20,y=60,width=180,height=30)

            self.cajatit=tk.Entry(self.frame)
            self.cajatit.place(x=230,y=60,width=120,height=30)

            self.txt2=tk.Label(self.frame,text="Eliga la etiqueta del Nombre:")
            self.txt2.place(x=20,y=110,width=180,height=30)

            self.cajanom=tk.Entry(self.frame)
            self.cajanom.place(x=230,y=110,width=120,height=30)

            self.txt3=tk.Label(self.frame,text="Eliga la etiqueta del Valor:")
            self.txt3.place(x=20,y=160,width=180,height=30)

            self.cajaval=tk.Entry(self.frame)
            self.cajaval.place(x=230,y=160,width=120,height=30)

            self.txt4=tk.Label(self.frame,text="Eliga la etiqueta del Tiempo:")
            self.txt4.place(x=20,y=210,width=180,height=30)

            self.cajatiempo=tk.Entry(self.frame)
            self.cajatiempo.place(x=230,y=210,width=120,height=30)

            self.botongraficar=tk.Button(self.frame,text="GRAFICAR",bd=5,command=self.GRAFICARTG)
            self.botongraficar.place(x=150,y=260,width=100,height=30)

            self.ventana.mainloop()


    def GRAFICARTG(self):
        pass
        ex=self.caja0.get()
        excel=ex+".csv"
        notas=pd.read_csv(excel)

        titulo=self.cajatit.get()
        etiqueta1=self.cajanom.get()
        etiqueta2=self.cajaval.get()
       # etiqueta3=self.
    
        datos=notas[[etiqueta1,etiqueta2]]

        
        



    def GRAFICARTU(self):
        try:
            ex=self.caja0.get()
            excel=ex+".csv"
            notas=pd.read_csv(excel)

            titulo=self.cajatit.get()
            etiqueta1=self.cajanom.get()
            etiqueta2=self.cajaval.get()
            etiqueta3=self.cajatiempo.get()
            etiqueta4=self.cajanombre.get()

            notas[etiqueta3]=pd.to_datetime(notas[etiqueta3])

            dato=notas[etiqueta1]==etiqueta4
            DATOS=notas[dato]
            #DATOS.sort_values(etiqueta3,inplace=True)

            valor=DATOS[etiqueta2]
            tiempo=DATOS[etiqueta3]

            try:
                plt.style.use('seaborn')
                plt.plot_date(tiempo,valor,linestyle="solid")
                plt.gcf().autofmt_xdate()
                formato=mpl_dates.DateFormatter('%b, %d, %Y')
                plt.gca().xaxis.set_major_formatter(formato)
                plt.title(titulo+": "+etiqueta1+": "+etiqueta4)
                plt.xlabel(etiqueta3)
                plt.ylabel(etiqueta2)
                plt.tight_layout()
                plt.show()

            except:
                messagebox.showerror(message="No se pueden graficar\nDe esa forma por los tipos de valores",title="ERROR")
            
        except:
            messagebox.showerror(message="No ingreso bien el nombre de las etiquetas",title="ERROR")
        

    
            

    def GRAFICARB(self):
        try:
            ex=self.caja0.get()
            excel=ex+".csv"
            notas=pd.read_csv(excel)

            titulo=self.cajatit.get()
            etiqueta1=self.cajanom.get()
            etiqueta2=self.cajaval.get()
            
            nombre=notas[etiqueta1]
            valor=notas[etiqueta2]

            fig=plt.subplots()
            plt.xlabel(etiqueta1,fontsize=20)
            plt.ylabel(etiqueta2,fontsize=20)
            plt.xticks(rotation=45)
            plt.title(titulo,fontsize=20)
            plt.bar(nombre,valor)
            plt.grid(True)
            plt.show()

        except:
            messagebox.showerror(message="No se pueden graficar\nDe esa forma por los tipos de valores\no No ingreso bien las etiquetas",title="ERROR")


    def GRAFICARP(self):
        try: 
            ex=self.caja0.get()
            excel=ex+".csv"
            notas=pd.read_csv(excel)

            titulo=self.cajatit.get()
            etiqueta1=self.cajanom.get()
            etiqueta2=self.cajaval.get()
            
            nombre=notas[etiqueta1]
            valor=notas[etiqueta2]

            porcentaje=notas[etiqueta2].sum()
            porcentajeb=round(porcentaje)
          
        
            
            leyenda = []
            for navegador, mercado in zip(nombre,valor):
                mercado2=round((mercado/porcentajeb*100),2)
                leyenda.append(navegador + '  (' + str(mercado2) + '%)')

            
            plt.pie(valor,labels=None,autopct="%0.1f %%")
            plt.title(titulo)
            plt.rc('legend', fontsize=6)
            plt.legend(leyenda,loc='best',bbox_to_anchor=(1.05, 1.0))
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror(message="No se pueden graficar\nDe esa forma por los tipos de valores\no No ingreso bien las etiquetas",title="ERROR")
        

            
                
            


app=Aplicacion()

