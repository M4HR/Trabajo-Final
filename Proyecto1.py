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
    t=input("Desea ingresar postulante?(S/N) ")
    if t =="s"or t=="S":
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
    
    break
# Proceso


# Postulantes Aptos
nom_apto=[]
edad_ap=[]
ponde_ap=[]
nive_ap=[]
aceptados=[nom_apto,edad_ap,ponde_ap,nive_ap] # Todos los postulantes aceptados - Bajos ciertos criterios

bec_nombre = []
bec_pon = []
bec_nive = []
bec_edad = []
becados = [bec_nombre, bec_edad, bec_pon, bec_nive] # Todos los postulantes pre becados - Reduccion del arreglo de 
# aceptados a 15 elementos y ordenado de mayor a menor

# Copia del Arreglo de Aceptados
cop_nombre = []
cop_pon = []
cop_nive = []
cop_edad = []
copia = [cop_nombre, cop_edad, cop_pon, cop_nive]

# No se esta usando actualmente - Arreglo Vacio
becasi_nombre = []
becasi_pon = []
becasi_nive = []
becasi_edad = []
becasi = [becasi_nombre, becasi_edad, becasi_pon, becasi_nive] # (Pendiente de Borrar)

# Postulantes aptos para recibir las becas
for i in range(len(nombres)):
    if edad[i] >= 18:
        if ponderado[i] >= 16:
            if nivel_ingles[i] == "Intermedio" or  nivel_ingles[i] =="intermedio"or  nivel_ingles[i] =="Avanzado"or  nivel_ingles[i] =="avanzado":
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
# Si son mas de 10 aceptados (Borrar):
Eva_nombre = []
Eva_pon = []
Eva_nive = []
Eva_edad = []
Eva_eva = []
Eva = [Eva_nombre, Eva_edad, Eva_pon, Eva_nive, Eva_eva]       

# Postulantes que obtienen la beca
a = len(aceptados[0])
for i in range(11):
    notas  = random.randint(0,20)
    Eva_eva.append(notas)
    while Eva_eva.count(notas) == 2:
        Eva_eva.remove(notas)
        Eva_eva.append(random.randint(0,20))
        
if a > 10:
    for i in range(len(cop_nombre)):
        aux = max(copia[2])
        aux2 = aux
        pos = cop_pon.index(aux)              
        if len(becados[0]) < 12:
            bec_nombre.append(copia[0][pos])
            Eva_nombre.append(copia[0][pos])
            copia[0].remove(copia[0][pos])
            bec_edad.append(copia[1][pos])
            Eva_edad.append(copia[1][pos])
            copia[1].remove(copia[1][pos])
            bec_pon.append(copia[2][pos])
            Eva_pon.append(copia[2][pos])
            copia[2].remove(copia[2][pos])
            bec_nive.append(copia[3][pos])
            Eva_nive.append(copia[3][pos])
            copia[3].remove(copia[3][pos])
else:
    bec_nombre.append(copia[0][pos])
    copia[0].remove(copia[0][pos])
    bec_edad.append(copia[1][pos])
    copia[1].remove(copia[1][pos])
    bec_pon.append(copia[2][pos])
    copia[2].remove(copia[2][pos])
    bec_nive.append(copia[3][pos])
    copia[3].remove(copia[3][pos])

for i in range(10):
    aux = max(Eva_eva)
    pos = Eva_eva.index(aux)
    if len(becasi[0])<=10: # and (Eva_eva.count(aux) == 1):
        becasi_nombre.append(Eva[0][pos])
        becasi_edad.append(Eva[1][pos])
        becasi_pon.append(Eva[2][pos])
        becasi_nive.append(Eva[3][pos])
        Eva[0].remove(Eva[0][pos])
        Eva[1].remove(Eva[1][pos])
        Eva[2].remove(Eva[2][pos])
        Eva[3].remove(Eva[3][pos])
        Eva[4].remove(Eva[4][pos])

# Salida
# Listado de postulantes aptos
print("***Postulantes Aptos***")

for i in range(len(nom_apto)):
    print(
        i+1,". Nombre:",aceptados[0][i],". Edad: ", aceptados[1][i],". Ponderado: ",aceptados[2][i],". Nivel de ingles: ",aceptados[3][i]
    )
# Lista de postulantes que ganaron la beca
print("***Obtuvieron una beca***")
for i in range(10):
    print(
        i+1,". Nombre:",becasi[0][i],". Edad: ", becasi[1][i],". Ponderado: ",becasi[2][i],". Nivel de ingles: ",becasi[3][i]
    )

print(" ")