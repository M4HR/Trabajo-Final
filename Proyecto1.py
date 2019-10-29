#Entrada
import os
os.system("cls") 

nombres = []
ponderado = []
nivel_ingles = []
edad = []
datos = [nombres, edad,ponderado, nivel_ingles ]

while True:

    n = input("Ingresa Nombre: ")
    nombres.append(n)

    e = int(input("Ingresa edad: "))
    edad.append(e)

    p = int(input("Ingresa ponderado: "))
    ponderado.append(p)

    ni = input("Ingresa nivel de ingles: ")
    nivel_ingles.append(ni)

   

    pregunta = input("Desea seguir ingresando postulantes?(S/N)")

    if pregunta == "N" or pregunta == "n":
        break

#Proceso

ponderado_max= max(ponderado)
ponderadoaceptado=[ponderado_max]
w=ponderado.index(ponderado_max)


#Salida