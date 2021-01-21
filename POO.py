
import tkinter as tk

class Aplicacion():
    indice=0
    listaOperaciones=[]
    Ccontador=0

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("CALCULADORA DE OPERACIONES BASICAS")
        self.ventana1.geometry("600x300")
        self.txt1=tk.Label(self.ventana1,text="Numero_1",bg="yellow")
        self.txt1.place(x=10,y=30,width=100,height=30)

        self.caja1=tk.Entry(self.ventana1,bg="pink")
        self.caja1.place(x=130,y=30,width=100,height=30)

        self.txt2=tk.Label(self.ventana1,text="Numero_2",bg="yellow")
        self.txt2.place(x=10,y=80,width=100,height=30)

        self.caja2=tk.Entry(self.ventana1,bg="pink")
        self.caja2.place(x=130,y=70 ,width=100,height=30)

        self.txt3=tk.Label(self.ventana1,text="Resultado",bg="orange")
        self.txt3.place(x=10,y=140,width=100,height=30)

        self.caja3=tk.Entry(self.ventana1,bg="pink")
        self.caja3.place(x=130,y=140,width=100,height=30)

        self.boton=tk.Button(self.ventana1,text="SUMA",command=self.funsuma)
        self.boton.place(x=270,y=50,width=100,height=30)

        self.boton2=tk.Button(self.ventana1,text="RESTA",command=self.funresta)
        self.boton2.place(x=400,y=50,width=100,height=30)

        self.boton3=tk.Button(self.ventana1,text="MULTIPLICACION",command=self.funmulti)
        self.boton3.place(x=270,y=100,width=100,height=30)

        self.boton4=tk.Button(self.ventana1,text="DIVISION",command=self.fundiv)
        self.boton4.place(x=400,y=100,width=100,height=30)

        self.boton5=tk.Button(self.ventana1,text="Borrar Todo",command=self.funborrar)
        self.boton5.place(x=450,y=250,width=100,height=30)

        self.boton6=tk.Button(self.ventana1,text="Borrar Numero1",command=self.funborrarn1)
        self.boton6.place(x=50,y=250,width=100,height=30)

        self.boton7=tk.Button(self.ventana1,text="Borrar Numero2",command=self.funborrarn2)
        self.boton7.place(x=250,y=250,width=100,height=30)

        self.txt4=tk.Label(self.ventana1,text="No de Operaciones Hechas : ",bg="gray")
        self.txt4.place(x=270,y=140,width=160,height=30)

        self.caja4=tk.Entry(self.ventana1,bg="gray")
        self.caja4.place(x=450,y=140,width=30,height=30)

        self.ventana1.mainloop()
        self.ventana2=tk.Tk()
        self.ventana2.title("REGISTRO DE OPERACIONES")
        self.ventana2.geometry("300x300")
        contador=1
        for elemento in self.listaOperaciones:
            self.txt5=tk.Label(self.ventana2,text=elemento,bg="yellow")
            self.txt5.grid(row=contador,column=5)
            contador=contador+1
            
        self.txt2=tk.Label(self.ventana2,text=(f"Numero de Operaciones : {self.Ccontador} "),bg="yellow")
        self.txt2.grid(row=contador,column=5)
        self.ventana2.mainloop()

    
    def funsuma(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get() 
            r=float(n1)+float(n2)
            self.listaOperaciones.append(n1+" + "+n2+" = "+str(r))
            self.caja3.delete(0,'end')
            self.caja3.insert(0,r)

            self.indice=self.indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,self.indice)
           
            self.Ccontador=self.Ccontador+1
        except:
            self.funborrar()
            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")

    def funresta(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)-float(n2)
            self.listaOperaciones.append(n1+" - "+n2+" = "+str(r))
            self.caja3.delete(0,'end')
            self.caja3.insert(0,r)

            self.Ccontador=self.Ccontador+1
            
            self.indice=self.indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,self.indice)

        except:
            self.funborrar()

            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")

    
    def funmulti(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)*float(n2)
            self.listaOperaciones.append(n1+" / "+n2+" = "+str(r))
            self.caja3.delete(0,"end")
            self.caja3.insert(0,r)

            
            self.Ccontador=self.Ccontador+1
            
            
            self.indice=self.indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,self.indice)

        except:
            self.funborrar()

            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")


        
    def fundiv(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)/float(n2)
            self.listaOperaciones.append(n1+" X "+n2+" = "+str(r))
            self.caja3.delete(0,"end")
            self.caja3.insert(0,r)


            self.Ccontador=self.Ccontador+1
            
            
            self.indice=self.indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,self.indice)
        
        except:
            self.funborrar()

            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")
        
    def funborrar(self):
        self.caja1.delete(0,"end")
        self.caja2.delete(0,"end")
        self.caja3.delete(0,"end")

    def funborrarn1(self):
        self.caja1.delete(0,"end")
        
    def funborrarn2(self):
        self.caja2.delete(0,"end")

    

app=Aplicacion()


