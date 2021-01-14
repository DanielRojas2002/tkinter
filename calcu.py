from tkinter import Tk,Label,Button,Entry
indice=0
listaOperaciones=[]
Ccontador=0


def funsuma():
    try:
        n1=caja1.get()
        n2=caja2.get() 
        r=float(n1)+float(n2)
        listaOperaciones.append(n1+" + "+n2+" = "+str(r))
        caja3.delete(0,'end')
        caja3.insert(0,r)

        global indice
        indice=indice+1
        caja4.delete(0,"end")
        caja4.insert(0,indice)
        global Ccontador
        Ccontador=Ccontador+1
    except:
        funborrar()

        caja1.insert(0,"Error")
        caja2.insert(0,"Error")
        caja3.insert(0,"Error")
        
    
def funresta():
    try:
        n1=caja1.get()
        n2=caja2.get()
        r=float(n1)-float(n2)
        listaOperaciones.append(n1+" - "+n2+" = "+str(r))
        caja3.delete(0,'end')
        caja3.insert(0,r)

        global Ccontador
        Ccontador=Ccontador+1
        
        global indice
        indice=indice+1
        caja4.delete(0,"end")
        caja4.insert(0,indice)

    except:
        funborrar()

        caja1.insert(0,"Error")
        caja2.insert(0,"Error")
        caja3.insert(0,"Error")

    
def funmulti():
    try:
        n1=caja1.get()
        n2=caja2.get()
        r=float(n1)*float(n2)
        listaOperaciones.append(n1+" / "+n2+" = "+str(r))
        caja3.delete(0,"end")
        caja3.insert(0,r)

        global Ccontador
        Ccontador=Ccontador+1
        
        global indice
        indice=indice+1
        caja4.delete(0,"end")
        caja4.insert(0,indice)

    except:
        funborrar()

        caja1.insert(0,"Error")
        caja2.insert(0,"Error")
        caja3.insert(0,"Error")


    
def fundiv():
    try:
        n1=caja1.get()
        n2=caja2.get()
        r=float(n1)/float(n2)
        listaOperaciones.append(n1+" X "+n2+" = "+str(r))
        caja3.delete(0,"end")
        caja3.insert(0,r)

        global Ccontador
        Ccontador=Ccontador+1
        
        global indice
        indice=indice+1
        caja4.delete(0,"end")
        caja4.insert(0,indice)
    
    except:
        funborrar()

        caja1.insert(0,"Error")
        caja2.insert(0,"Error")
        caja3.insert(0,"Error")
    
def funborrar():
    caja1.delete(0,"end")
    caja2.delete(0,"end")
    caja3.delete(0,"end")

def funborrarn1():
    caja1.delete(0,"end")
    
def funborrarn2():
    caja2.delete(0,"end")


ventana=Tk()
ventana.title("CALCULADORA DE OPERACIONES BASICAS")
ventana.geometry("600x300")

txt1=Label(ventana,text="Numero_1",bg="yellow")
txt1.place(x=10,y=30,width=100,height=30)

caja1=Entry(ventana,bg="pink")
caja1.place(x=130,y=30,width=100,height=30)

txt2=Label(ventana,text="Numero_2",bg="yellow")
txt2.place(x=10,y=80,width=100,height=30)

caja2=Entry(ventana,bg="pink")
caja2.place(x=130,y=70 ,width=100,height=30)

txt3=Label(ventana,text="Resultado",bg="orange")
txt3.place(x=10,y=140,width=100,height=30)

caja3=Entry(ventana,bg="pink")
caja3.place(x=130,y=140,width=100,height=30)

boton=Button(ventana,text="SUMA",command=funsuma)
boton.place(x=270,y=50,width=100,height=30)

boton2=Button(ventana,text="RESTA",command=funresta)
boton2.place(x=400,y=50,width=100,height=30)

boton3=Button(ventana,text="MULTIPLICACION",command=funmulti)
boton3.place(x=270,y=100,width=100,height=30)

boton4=Button(ventana,text="DIVISION",command=fundiv)
boton4.place(x=400,y=100,width=100,height=30)

boton5=Button(ventana,text="Borrar Todo",command=funborrar)
boton5.place(x=450,y=250,width=100,height=30)

boton6=Button(ventana,text="Borrar Numero1",command=funborrarn1)
boton6.place(x=50,y=250,width=100,height=30)

boton7=Button(ventana,text="Borrar Numero2",command=funborrarn2)
boton7.place(x=250,y=250,width=100,height=30)

txt4=Label(ventana,text="No de Operaciones Hechas : ",bg="gray")
txt4.place(x=270,y=140,width=160,height=30)

caja4=Entry(ventana,bg="gray")
caja4.place(x=450,y=140,width=30,height=30)

ventana.mainloop()

ventana2=Tk()
ventana2.title("REGISTRO DE OPERACIONES")
ventana2.geometry("300x300")

contador=1
for elemento in listaOperaciones:
    txt1=Label(ventana2,text=elemento,bg="yellow")
    txt1.grid(row=contador,column=5)
    contador=contador+1
    
txt2=Label(ventana2,text=(f"Numero de Operaciones : {Ccontador} "),bg="yellow")
txt2.grid(row=contador,column=5)

ventana2.mainloop()