from tkinter import Tk,Label,Button,Entry



def funsuma():
    n1=caja1.get()
    n2=caja2.get()
    r=float(n1)+float(n2)
    caja3.delete(0,'end')
    caja3.insert(0,r)
    
def funresta():
    n1=caja1.get()
    n2=caja2.get()
    r=float(n1)-float(n2)
    caja3.delete(0,'end')
    caja3.insert(0,r)
    
def funmulti():
    n1=caja1.get()
    n2=caja2.get()
    r=float(n1)*float(n2)
    caja3.delete(0,"end")
    caja3.insert(0,r)
    
def fundiv():
    n1=caja1.get()
    n2=caja2.get()
    r=float(n1)/float(n2)
    caja3.delete(0,"end")
    caja3.insert(0,r)
    
def funborrar():
    caja1.delete(0,"end")
    caja2.delete(0,"end")
    caja3.delete(0,"end")

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
boton5.place(x=250,y=250,width=100,height=30)



ventana.mainloop()