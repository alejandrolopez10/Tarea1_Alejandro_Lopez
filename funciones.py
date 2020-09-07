#!/usr/bin/env python
# coding: utf-8



#Funcion Factorial

def factorial(n=int):
    mult=1    #Inicializamos la multiplicación
    
    for i in range (1,n,1):
        mult=mult*(i+1)
        i=mult
    return int(mult)


#-------------Funcion Binomial


def binomial(n=int,k=int):
    
    #Hacemos esto con la ayuda de la funcion binomial(n,k)
    
    return int(factorial(n)/(factorial(k)*factorial(n-k)) )


#-------------Triangulo de Pascal


def pascal(n=int):
    
    trian=open("pascal-n.txt", "w")    #creamos el archivo de texto donde estara el triangulo de pascal
    
#Necesitaremos dos for, uno para iterar n y otro para iterar k  

    for i in range(0,n,1):             #Esto nos asegura n lineas
        
        lista=[]   #En esta lista guardaremos los coeficientes binomiales de cada linea
        
        for t in range (0,i+1,1):
            
            lista.append(binomial(i,t))
            
        print ((n-t)*" ",str(lista),end="\n")    #Imprimimos la lista
        
        a=str(lista)+"\n"         #convertimos los elementos de la lista en strings para poder copiarlos a un .txt
        
        trian.write(a)            #Copiamos cada linea en el archivo .txt
        
    
    trian.close()
    return
    
    

#-----------Moneda parte a
def monedaA(n=100,k=10):
    a=binomial(n,k)/(2**n)
    print ("La probabilidad de que al lanzar la moneda 100 veces caiga cara 10 veces es: ",a)
    
#-----------Moneda parte b    

def monedaB(n=100,k=30):
    b=binomial(n,k)/(2**n)
    print ("la probabilidad de que caiga cara 30 veces es: ",b)   





