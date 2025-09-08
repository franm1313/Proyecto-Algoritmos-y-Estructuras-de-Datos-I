import random


#Funcion para crear  los vectores
def crear_vectores():
    materias = ["matematica", "fisica", "quimica", "historia", "lengua"]
    legajos = [random.randint(10000,99999) for _ in range(30)]
    return materias, legajos


#Funcion para crear una matriz inicializada en 0
def matriz_en_cero():
    filas = 30
    columnas = 5
    matriz = []
    for f in range(filas):
        matriz.append([0]*columnas)
    for fila in matriz:
        print(fila)
    return matriz

#Funcion para crear una matriz inicializada con valores aleatorios
def matriz_aleatoria():
    filas = 30
    columnas = 5
    matriz = []
    for f in range(filas):
        fila = [random.randint(1, 10) for _ in range(columnas)]
        matriz.append(fila)
        
    for fila in matriz:
        print(fila)
    return matriz

#Opc 6
def ordenar_informacion(matriz, materias, legajos):

    def ordenar_por_promedio():
        alumnos = []
        for i in range(len(matriz)):
            promedio = sum(matriz[i]) / len(matriz[i])
            alumnos.append((promedio, legajos[i], matriz[i]))

        alumnos.sort(reverse=True)

        print("\nAlumnos ordenados por promedio (mayor a menor): ")
        for promedio, legajo, notas in alumnos:
            print(f"Legajo: {legajo} | Promedio: {promedio:.2f} | Notas: {notas}")

    def filtrar_por_materia(indice_materia):
        if 0 <= indice_materia < len(materias):
            print(f"\nNotas de la materia '{materias[indice_materia]}':")
            for i in range(len(matriz)):
                print(f"Legajo: {legajos[i]} | Nota: {matriz[i][indice_materia]}")
        else:
            print("Índice de materia inválido")

    def ordenar_por_legajo():
        alumnos = []
        for i in range(len(matriz)):
            alumnos.append((legajos[i], matriz[i]))

        alumnos.sort(reverse=True)

        print("\nAlumnos ordenados por legajo (mayor a menor): ")
        for legajo, notas in alumnos:
            print(f"Legajo: {legajo} | Notas: {notas}")

    # Submenú de ordenamientos
    print("""
    1 - Ordenar por promedio
    2 - Filtrar por materia
    3 - Ordenar por legajo
    """)


    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        ordenar_por_promedio()
    elif opcion == 2:
        indice = int(input(f"Ingrese el índice de la materia (0 a {len(materias)-1}): "))
        filtrar_por_materia(indice)
    elif opcion == 3:
        ordenar_por_legajo()
    else:
        print("Opción inválida.")


def opc1():
    print("soy la funcion numero 1")

def opc2():
    print("soy la funcion numero 2")

def opc3():
    print("soy la funcion numero 3")

def opc4():
    print("soy la funcion numero 4")

def opc5():
    print("soy la funcion numero 5")


"""
    FUNCION DEL MENU DEL PROGRAMA
"""
def menu():
    materias, legajos = crear_vectores()
    
    print("""███╗░░██╗░█████╗░████████╗███████╗░██████╗██████╗░██╗░░░██╗
████╗░██║██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗╚██╗░██╔╝
██╔██╗██║██║░░██║░░░██║░░░█████╗░░╚█████╗░██████╔╝░╚████╔╝░
██║╚████║██║░░██║░░░██║░░░██╔══╝░░░╚═══██╗██╔═══╝░░░╚██╔╝░░
██║░╚███║╚█████╔╝░░░██║░░░███████╗██████╔╝██║░░░░░░░░██║░░░
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░░░░░░░╚═╝░░░""")
    
    print(f"""

NUMERO DE ALUMNOS ACTUALES: {len(legajos)}
NUMERO DE MATERIAS ACTUALES: {len(materias)}
          
OPCION 1: Cargar alumno.
OPCION 2: Cargar materia.
OPCION 3: Cargar notas
OPCION 4: Actualizar nota.
OPCION 5: Mostrar tabla de alumnos.
OPCION 6: Ordenar por Legajo/Promedio/Notas.
OPCION 7: Buscar alumno por legajo.
OPCION 8: Mostrar Estadisticas.
OPCION 9: Salir del programa.""")
    opc = -1
    while (opc != 0):
        

        opc = int(input("Ingrese una opcion: "))

        if (opc < 0 or opc > 5):
            opc = int(input("Ingrese una opcion valida: "))

        if (opc == 1):
            opc1()
        elif(opc ==2):
            opc2()
        elif(opc ==3):
            opc3()
        elif(opc ==4):
            opc4()
        elif(opc ==5):
            opc5()
        elif(opc ==6):
            ordenar_informacion()
def ingresaMayora(valor,texto):
    resu=float(input(texto))
    while resu < valor:
        print("Error. Re ingrese")
        resu=float(input(texto))
    return resu

def inicializarMatriz(m,cf,cc,valor):
    for f in range(cf):
        m.append([])
        for c in range(cc):
            m[f].append(valor)
            
def sumarMatrz(m,cf):
    resu=0
    for f in range(cf):
        resu+=sum(m[f])   #Usando funcion de listas
    return resu
            
def buscarElem(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return -1

def elementoExistente(lista,elem):
    for i in range (len(lista)):
        if lista[i]== elem:
            return True
    return False

def sumaMatrizxFila(m,lista,cf):
    for f in range(cf):
        lista[f]= sum(m[f])

def sumaMatrizxColumna(m,lista,cf,cc):
    for j in range(cc):
        for i in range(cf):
            lista[j]+=m[f][c]

#opc 1
def cargarAlumnos(legajos,nomAlumnos):
    print("Carga de alumnos (legajo 0 para terminar)")
    seguir=True
    while seguir:
        legajo = int(input("Ingresar el legajo del alumno:"))
        if legajo == 0:
            seguir=False
        else:
            if(elementoExistente(legajos,legajo)):
                print("Legajo existente. Re-ingrese el legajo del alumno")
        nombre=input("Ingresar el nombre del alumno")
        if nombre == "":
            print("Error. Re-ingresar el nombre del alumno")
        legajos.append(legajo)
        nomAlumnos.append(nombre)
        print("Alumno cargado correctamente")
#opc 2

def cargarMateria():
    print("Carga de materias (Ingrese 0 para terminar)")
    materia=input("Ingrese el nombre de la materia: ").title()
    while materia != "0":

        while materia.isdigit():
            print("Error! Se detecto solamente numeros.")
            materia=input("Ingrese el nombre de la materia: ").title()
        
        if materia in materias:
            print("Esta materia ya ha sido cargada anteriormente")
        else:
            materias.append(materia)
            print("Materia cargada con exito!")
        
        materia=input("Ingrese el nombre de la materia: ").title()

    if materia == "0":
        menu()

cargarMateria()
print(materias)


#opc4 (actualizarNota):
def actualizarNota(matriz, legajos, materias):
    print("Actualización de notas (legajo 0 para terminar)")
    seguir = True
    while seguir:
        legajo = ingresaMayora(0,"Legajo del alumno")
        if legajo == 0:
            seguir = False
        else:
            posAlumno = buscarElem(legajos, legajo)
            while(posAlumno == -1):
                print("Legajo no encontrado en el registro de alumnos")
                legajo = ingresaMayora(0,"Ingrese otro legajo")
                posAlumno = buscarElem(legajos, legajo)
            
            materia = input("Ingresar el nombre de la materia: ")
            posMateria = buscarElem(materias, materia)
            while(posMateria == -1):
                print("Materia no encontrada")
                materia = input("Ingrese nuevamente el nombre de la materia: ")
                posMateria = buscarElem(materias, materia)
            
            nota = ingresaMayora(0,"Nueva nota del alumno (1-10)")
            while nota < 1 or nota > 10:
                print("La nota debe estar entre 1 y 10")
                nota = ingresaMayora(0,"Ingrese la nota nuevamente (1-10)")
            
            matriz[posAlumno][posMateria] = nota
            print("Nota actualizada correctamente")

#opc 5
def mostrarTabla(matriz, materias, legajos):
    print("=== TABLA DE ALUMNOS ===")
    encabezado ="Legajo\t"
    for materia in materias:
        encabezado += materia + "\t"    #Vector de materias
    print(encabezado) 
    for i in range(len(legajos)):
        fila = str(legajos[i]) + "\t"
        for nota in matriz[i]:
            fila += str(nota) + "\t"
        print(fila)

#opc 7
def buscarAlumno(matriz, materias, legajos):
    legajo_buscar = int(input("Ingrese el legajo a buscar: "))
    for materia in materias:
        encabezado += materia + "\t"    #Vector de materias
    print(encabezado) 
    for i in range(len(legajos)):
        fila = str(legajos[i]) + "\t"
        for nota in matriz[i]:
            fila += str(nota) + "\t"
        print(fila)
