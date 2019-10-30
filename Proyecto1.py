# Entrada
import os
os.system("cls") 

nombres = []
ponderado = []
nivel_ingles = []
edad = []
datos = [nombres, edad,ponderado, nivel_ingles ]
# Ingreso de Postulantes
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
# Postulantes Aptos
nom_apto=[]
edad_ap=[]
ponde_ap=[]
nive_ap=[]
aceptados=[nom_apto,edad_ap,ponde_ap,nive_ap]
bec_nombre = []
bec_pon = []
bec_nive = []
bec_edad = []
becados = [bec_nombre, bec_edad, bec_pon, bec_nive]
for i in range(len(nombres)):
    if edad[i] >= 18:
        # aceptados=[edad]
        if ponderado[i] >= 16:
            # aceptado=[edad,ponderado]
            if nivel_ingles[i] == "Intermedio" or  nivel_ingles[i] =="intermedio"or  nivel_ingles[i] =="Avanzado"or  nivel_ingles[i] =="avanzado":
                # aceptados.append(nombres[i], edad[i] ,ponderado[i],nivel_ingles[i])
                a = nombres[i]
                nom_apto.append(a)
                bec_nombre.append(a)
                b = edad[i]
                edad_ap.append(b)
                bec_edad.append(b)
                c = ponderado[i]
                bec_pon.append(c)
                ponde_ap.append(c)
                d = nivel_ingles[i]
                bec_nive.append(d)
                nive_ap.append(d)
        
# Postulantes que obtienen la beca
if len(bec_nombre)>= 2:
    for i in range(len(bec_nombre)):
        for j in range(1, len(bec_nombre)):
            if bec_pon[i]>bec_pon[j]:
                aux = bec_pon[i]
                bec_pon[i] = bec_pon[j+1]
                bec_pon[j+1] = aux



# Salida
# Listado de postulantes aptos
print("***Postulantes Aptos***")

for i in range(len(nom_apto)):
    print(
        i+1,". Nombre:",aceptados[0][i],". Edad: ", aceptados[1][i],". Ponderado: ",aceptados[2][i],". Nivel de ingles: ",aceptados[3][i]
    )
# Lista de postulantes que ganaron la beca
print(" ")