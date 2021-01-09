from tkinter import *
import parser

indice=0
def get_number(n):
    global indice
    caja1.insert(indice,n)
    indice=indice+1
    
def get_operation(operator):
    global indice
    operator_len=len(operator)
    caja1.insert(indice,operator)
    indice+=operator_len
   
def clear_pantalla():
    caja1.delete(0,END)
    
def undo():
    caja1_state=caja1.get()
    if len(caja1_state):
        caja1_nuevo=caja1_state[:-1]
        clear_pantalla()
        caja1.insert(0,caja1_nuevo)
    else:
        clear_pantalla()
        caja1.insert(0,'Error')
        
def calculate():
    caja1_state=caja1.get()
    try:
        expresion=parser.expr(caja1_state).compile()
        result=eval(expresion)
        clear_pantalla()
        caja1.insert(0,result)
    except:
        clear_pantalla()
        caja1.insert(0,'Error')
        

ventana=Tk()
ventana.title("CALCULADORA BOTONES")
ventana.geometry("150x150")

caja1=Entry(ventana,bg="yellow")
caja1.grid(row=1,columnspan=8,sticky=W+E)

Button(ventana,text="1",command=lambda:get_number(1)).grid(row=2,column=0,sticky=W+E)
Button(ventana,text="2",command=lambda:get_number(2)).grid(row=2,column=1,sticky=W+E)
Button(ventana,text="3",command=lambda:get_number(3)).grid(row=2,column=2,sticky=W+E)

Button(ventana,text="4",command=lambda:get_number(4)).grid(row=3,column=0,sticky=W+E)
Button(ventana,text="5",command=lambda:get_number(5)).grid(row=3,column=1,sticky=W+E)
Button(ventana,text="6",command=lambda:get_number(6)).grid(row=3,column=2,sticky=W+E)

Button(ventana,text="7",command=lambda:get_number(7)).grid(row=4,column=0,sticky=W+E)
Button(ventana,text="8",command=lambda:get_number(8)).grid(row=4,column=1,sticky=W+E)
Button(ventana,text="9",command=lambda:get_number(9)).grid(row=4,column=2,sticky=W+E)


Button(ventana,text="AC",command=lambda:clear_pantalla()).grid(row=5,column=0,sticky=W+E)
Button(ventana,text="0",command=lambda:get_number(0)).grid(row=5,column=1,sticky=W+E)
Button(ventana,text="%",command=lambda:get_operation("%")).grid(row=5,column=2,sticky=W+E)

Button(ventana,text="+",command=lambda:get_operation("+")).grid(row=2,column=3,sticky=W+E)
Button(ventana,text="-",command=lambda:get_operation("-")).grid(row=3,column=3,sticky=W+E)
Button(ventana,text="X",command=lambda:get_operation("*")).grid(row=4,column=3,sticky=W+E)
Button(ventana,text="/",command=lambda:get_operation("/")).grid(row=5,column=3,sticky=W+E)

Button(ventana,text="<-",command=lambda:undo()).grid(row=2,column=4,sticky=W+E)
Button(ventana,text="exp",command=lambda:get_operation("**")).grid(row=3,column=4,sticky=W+E)
Button(ventana,text="**2",command=lambda:get_operation("**2")).grid(row=4,column=4,sticky=W+E)
Button(ventana,text="(",command=lambda:get_operation("(")).grid(row=5,column=4,sticky=W+E)
Button(ventana,text=")",command=lambda:get_operation(")")).grid(row=5,column=5,sticky=W+E)
Button(ventana,text="=",command=lambda:calculate()).grid(row=6,column=2,sticky=W+E,columnspan=2)










ventana.mainloop()
