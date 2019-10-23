# PROTOTIPO
# Se requiere de un arreglo de nombres, ponderados, nivel ingles, edad, entre otros.
import os
os.system("cls") 

nombres = []
ponderado = []
nivel_ingles = []
edad = []
datos = [nombres, ponderado, nivel_ingles, edad]

while True:

    n = input("Ingresa Nombre: ")
    nombres.append(n)

    p = int(input("Ingresa ponderado: "))
    ponderado.append(p)

    ni = input("Ingresa nivel de ingles: ")
    nivel_ingles.append(ni)

    e = int(input("Ingresa edad: "))
    edad.append(e)

    pregunta = input("Desea seguir ingresando postulantes?(S/N)")

    if pregunta == "N" or pregunta == "n":
        break

  print(" ")
        

ponderado_max= max(ponderado)
ponderadoaceptado=[ponderado_max]
w=ponderado.index(ponderado_max)
print(datos)
print("Obtuvo la beca:",nombres[w])

