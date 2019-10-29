# Entrada
import os
os.system("cls") 

nombres = []
ponderado = []
nivel_ingles = []
edad = []
datos = [nombres, edad,ponderado, nivel_ingles ]
print("***INGRESAR POSTULANTES***")
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

# Proceso
nom_apto=[]
edad_ap=[]
ponde_ap=[]
nive_ap=[]
aceptados=[nom_apto,edad_ap,ponde_ap,nive_ap]
for i in range(len(nombres)):
    if edad[i] >= 18:
        # aceptados=[edad]
        if ponderado[i] >= 16:
            # aceptado=[edad,ponderado]
            if nivel_ingles[i] == "Intermedio" or  nivel_ingles[i] =="intermedio"or  nivel_ingles[i] =="Avanzado"or  nivel_ingles[i] =="avanzado":
                # aceptados.append(nombres[i], edad[i] ,ponderado[i],nivel_ingles[i])
                a = nombres[i]
                nom_apto.append(a)
                b = edad[i]
                edad_ap.append(b)
                c = ponderado[i]
                ponde_ap.append(c)
                d = nivel_ingles[i]
                nive_ap.append(d)
        
# Postulantes que obtienen la beca


# Salida
print("***Postulantes Aptos***")

for i in range(len(nom_apto)):
    print(
        i+1,". Nombre:",aceptados[0][i],". Edad: ", aceptados[1][i],". Ponderado: ",aceptados[2][i],". Nivel de ingles: ",aceptados[3][i]
    )
print(" ")