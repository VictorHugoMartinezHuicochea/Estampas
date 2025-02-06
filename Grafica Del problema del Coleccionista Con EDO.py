#Escuela Superior de Fisico y Matematicas
#Licenciatura En Matematica Algoritmica
#Analisis Matematico
#Grafica de Puntos Aleatorios
#Profesor: Marco Antonio Rodriguez Andrade
#Alumno: Victor Hugo Martinez Huicochea


#Importamos librerias
import matplotlib.pyplot as plt
import random
import numpy
import math


#K es el numero de sobres comprados
k=120
#L es la cantidad de coleccionistas en el experimento
l=20
#M es la cantidad de estampillas diferentes que hay
M=240
#H es la cantidad de estampillas por sobre
h=5


#Iniciamos la apertura de sobres por coleccionista
for p in range (l):
    #Creamos arrays, uno que contenga al punto inicial y otro vacia que contenga los puntos
    puntos = set([])
    a=[0]

    #Para cada sobre abierto
    for i in range(k):
        #Creamos una lista de 5 enteros aleatorios entre 1 y 240
        numeros = set([random.randint(1, M) for i in range(h)])
        #Los unimos al conjunto que tenemos
        puntos=puntos|numeros
        #Checamos cardinalidad y lo agregamos al historial a
        a.append(len(puntos))
    #Graficamos el array a que es el historial de la cardinalidad por apertura de sobre
    plt.plot(a,linestyle='--',color="orange")



#Para la EDO
x=numpy.array(range(1200))*0.1
y=numpy.zeros(len(x))
for i in range(len(x)):
    #Solucionamos el EDO y luego solucionamos su problema de valores iniciales y graficamos
    y[i]=240-235*(math.exp((1/48)-(x[i]/48)))

#Graficamos la solucion al EDO
plt.plot(x,y,linewidth=3,color="black",label='Solucion Al EDO')

#Mostramos y embellecemos la tabla
plt.title("Grafica de Puntos Aleatorios",fontsize=20)
plt.xlabel("Recursion")
plt.ylabel("Cardinalidad")
plt.legend()
plt.show()
