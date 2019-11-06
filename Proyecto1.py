import os
import random
os.system("cls") 
# Entrada
nombres = []
ponderado = []
nivel_ingles = []
edad = []
datos = [nombres, edad,ponderado, nivel_ingles ]
# Importando datos
datos_estaticos = []
with open("Postulantes.txt", "r") as f:
    lineas = [linea.split() for linea in f]
for linea in lineas:
    aux_dato = linea
    aux_nom = linea[0]
    aux_edad = linea[1]
    aux_edad = int(aux_edad)
    aux_pon = linea[2]
    aux_pon = int(aux_pon)
    aux_ni = linea[3]
    nombres.append(aux_nom)
    edad.append(aux_edad)
    ponderado.append(aux_pon)
    nivel_ingles.append(aux_ni)
# Ingreso de Postulantes
print("***INGRESAR POSTULANTES***")
while True:
    agregar = open("Postulantes.txt", "a")
   
    n = input("Ingresa Nombre: ")     
    nombres.append(n)        
    while True:
        e = int(input("Ingresa edad: "))
        if e>=15:
            edad.append(e)
            break
        else:
            print("Ingrese edad mayor a 14")
    while True:       
        p = int(input("Ingresa ponderado: "))
        if p>=0 and p<=20:
            ponderado.append(p)
            break
        else:
            print("Ingrese nota ponderada entre 0 y 20")
    while True:
        ni = input("Ingresa nivel de ingles: ")
        if ni== "Intermedio" or ni =="intermedio"or  ni =="Avanzado"or  ni =="avanzado" or ni=="Basico" or ni=="basico":
            nivel_ingles.append(ni)
            break
        else:
            print("El nivel de ingles debe ser Avanzado , Intermedio o Basico")

    agregar.write("\n"+n+" "+str(e)+" "+str(p)+" "+ni)
    agregar.close()
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
cop_nombre = []
cop_pon = []
cop_nive = []
cop_edad = []
copia = [cop_nombre, cop_edad, cop_pon, cop_nive]
becasi_nombre = []
becasi_pon = []
becasi_nive = []
becasi_edad = []
becasi = [becasi_nombre, becasi_edad, becasi_pon, becasi_nive]
for i in range(len(nombres)):
    if edad[i] >= 18:
        # aceptados=[edad]
        if ponderado[i] >= 16:
            # aceptado=[edad,ponderado]
            if nivel_ingles[i] == "Intermedio" or  nivel_ingles[i] =="intermedio"or  nivel_ingles[i] =="Avanzado"or  nivel_ingles[i] =="avanzado":
                # aceptados.append(nombres[i], edad[i] ,ponderado[i],nivel_ingles[i])
                a = nombres[i]
                nom_apto.append(a)
                cop_nombre.append(a)
                b = edad[i]
                edad_ap.append(b)
                cop_edad.append(b)
                c = ponderado[i]
                cop_pon.append(c)
                ponde_ap.append(c)
                d = nivel_ingles[i]
                cop_nive.append(d)
                nive_ap.append(d)
        
# Postulantes que obtienen la beca
a = len(aceptados[0])

if a > 10:
    for i in range(len(cop_nombre)):
        aux = max(copia[2])
        aux2 = aux
        pos = cop_pon.index(aux)              
        if len(becados[0]) < 15:
            bec_nombre.append(copia[0][pos])
            copia[0].remove(copia[0][pos])
            bec_edad.append(copia[1][pos])
            copia[1].remove(copia[1][pos])
            bec_pon.append(copia[2][pos])
            copia[2].remove(copia[2][pos])
            bec_nive.append(copia[3][pos])
            copia[3].remove(copia[3][pos])
# Si las notas son iguales:
'''
for i in range(len(bec_nombre)):
    # con = 0
    conta = 0
    for j in range(len(bec_nombre)):
        con = 0
        if bec_pon[i] == bec_pon[j]:
            con += 1
        elif con >= 1 and bec_pon[i] == bec_pon[j]:
            conta += 1
    if con == 1:
        becasi_nombre.append(becados[0][i])
        becasi_edad.append(becados[1][i])
        becasi_pon.append(becados[2][i])
        becasi_nive.append(becados[3][i])
    elif con >= 1:
        posi = bec_pon.index(bec_pon[i])
        if conta <= (10-len(becasi_nombre)):
            print(conta)
            for w in range(conta):
                becasi_nombre.append(becados[0][posi+w])
                becasi_edad.append(becados[1][posi+w])
                becasi_pon.append(becados[2][posi+w])
                becasi_nive.append(becados[3][posi+w])
 '''   
# Salida
# Listado de postulantes aptos
print("***Postulantes Aptos***")

for i in range(len(nom_apto)):
    print(
        i+1,". Nombre:",aceptados[0][i],". Edad: ", aceptados[1][i],". Ponderado: ",aceptados[2][i],". Nivel de ingles: ",aceptados[3][i]
    )
# Lista de postulantes que ganaron la beca
print("***Obtuvieron una beca***")
for i in range(len(becasi_nombre)):
    print(
        i+1,". Nombre:",becasi[0][i],". Edad: ", becasi[1][i],". Ponderado: ",becasi[2][i],". Nivel de ingles: ",becasi[3][i]
    )
print(" ")