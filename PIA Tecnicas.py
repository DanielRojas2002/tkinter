
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
        
         

       
            
        
    