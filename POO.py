
from tkinter import Tk

class Aplicacion(Frame):
    indice=0
    listaOperaciones=[]
    Ccontador=0

    def __init__(self,master=None):
        super().__init__(master,width=120,height=170)
        self.master=master
        self.pack()
        self.botones()

    
    def funsuma(self):
    try:
        n1=self.caja1.get()
        n2=self.caja2.get() 
        r=float(n1)+float(n2)
        listaOperaciones.append(n1+" + "+n2+" = "+str(r))
        self.caja3.delete(0,'end')
        self.caja3.insert(0,r)

        global indice
        indice=indice+1
        self.caja4.delete(0,"end")
        self.caja4.insert(0,indice)
        global Ccontador
        Ccontador=Ccontador+1
    except:
        funborrar()
        self.caja1.insert(0,"Error")
        self.caja2.insert(0,"Error")
        self.caja3.insert(0,"Error")

    def funresta(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)-float(n2)
            listaOperaciones.append(n1+" - "+n2+" = "+str(r))
            self.caja3.delete(0,'end')
            self.caja3.insert(0,r)

            global Ccontador
            Ccontador=Ccontador+1
            
            global indice
            indice=indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,indice)

        except:
            funborrar()

            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")

    
    def funmulti(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)*float(n2)
            listaOperaciones.append(n1+" / "+n2+" = "+str(r))
            self.caja3.delete(0,"end")
            self.caja3.insert(0,r)

            global Ccontador
            Ccontador=Ccontador+1
            
            global indice
            indice=indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,indice)

        except:
            funborrar()

            self.caja1.insert(0,"Error")
            self.caja2.insert(0,"Error")
            self.caja3.insert(0,"Error")


        
    def fundiv(self):
        try:
            n1=self.caja1.get()
            n2=self.caja2.get()
            r=float(n1)/float(n2)
            listaOperaciones.append(n1+" X "+n2+" = "+str(r))
            self.caja3.delete(0,"end")
            self.caja3.insert(0,r)

            global Ccontador
            Ccontador=Ccontador+1
            
            global indice
            indice=indice+1
            self.caja4.delete(0,"end")
            self.caja4.insert(0,indice)
        
        except:
            funborrar()

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






    def botones(self):
        self.txt1=Label(ventana,text="Numero_1",bg="yellow")
        self.txt1.place(x=10,y=30,width=100,height=30)

        self.caja1=Entry(ventana,bg="pink")
        self.caja1.place(x=130,y=30,width=100,height=30)

        self.txt2=Label(ventana,text="Numero_2",bg="yellow")
        self.txt2.place(x=10,y=80,width=100,height=30)

        self.caja2=Entry(ventana,bg="pink")
        self.caja2.place(x=130,y=70 ,width=100,height=30)

        self.txt3=Label(ventana,text="Resultado",bg="orange")
        self.txt3.place(x=10,y=140,width=100,height=30)

        self.caja3=Entry(ventana,bg="pink")
        self.caja3.place(x=130,y=140,width=100,height=30)

        self.boton=Button(ventana,text="SUMA",command=funsuma)
        self.boton.place(x=270,y=50,width=100,height=30)

        self.boton2=Button(ventana,text="RESTA",command=funresta)
        self.boton2.place(x=400,y=50,width=100,height=30)

        self.boton3=Button(ventana,text="MULTIPLICACION",command=funmulti)
        self.boton3.place(x=270,y=100,width=100,height=30)

        self.boton4=Button(ventana,text="DIVISION",command=fundiv)
        self.boton4.place(x=400,y=100,width=100,height=30)

        self.boton5=Button(ventana,text="Borrar Todo",command=funborrar)
        self.boton5.place(x=450,y=250,width=100,height=30)

        self.boton6=Button(ventana,text="Borrar Numero1",command=funborrarn1)
        self.boton6.place(x=50,y=250,width=100,height=30)

        self.boton7=Button(ventana,text="Borrar Numero2",command=funborrarn2)
        self.boton7.place(x=250,y=250,width=100,height=30)

        self.txt4=Label(ventana,text="No de Operaciones Hechas : ",bg="gray")
        self.txt4.place(x=270,y=140,width=160,height=30)

        self.caja4=Entry(ventana,bg="gray")
        self.caja4.place(x=450,y=140,width=30,height=30)
