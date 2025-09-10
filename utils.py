import random

def crearVectores():
    materias = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
    legajos = [random.randint(10000,99999) for _ in range(5)]
    nomAlumnos = ["Juan Diaz","Ezequiel Senini","Juan Echarri","Francisco Gonzalez","Luca"]
    print(legajos)
    return materias, legajos, nomAlumnos


def matrizEnCero(legajos,materias):
    filas = len(legajos)
    columnas = len(materias)
    matriz = []
    for f in range(filas):
        matriz.append([0]*columnas)
    for fila in matriz:
        print(fila)
    return matriz


def matrizAleatoria(legajos, materias):
    filas = len(legajos)
    columnas = len(materias)
    matriz = []
    for f in range(filas):
        fila = [random.randint(1, 10) for _ in range(columnas)]
        matriz.append(fila)    
    for fila in matriz:
        print(fila)
    return matriz


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
        resu+=sum(m[f])
    return resu


def buscarElem(lista,elem):
    if elem in lista:
        return lista.index(elem)
    else:
        return -1


def elementoExistente(lista,elem):
    if elem in lista:
        return True
    else:
        return False


def sumaMatrizxFila(m,lista,cf):
    for f in range(cf):
        lista[f]= sum(m[f])


def sumaMatrizxColumna(m,lista,cf,cc):
    for j in range(cc):
        for i in range(cf):
            lista[j]+=m[cf][cc]


def validacionLegajos(legajos, legajo):
     while not (legajo.isdigit() and len(legajo) == 7 and not elementoExistente(legajos, int(legajo))):
        print("Error en ingreso de legajo. Asegurarse de que sean numeros, y que este en el formato correcto(7 digitos)")
        legajo=input("Ingresar legajo del alumno: ")
        leg = int(legajo)
        if leg == 0:
            seguir = False 
            menu()
        

def cargarAlumnos(legajos, nomAlumnos):
    print("Carga de alumnos (legajo 0 para terminar)")
    seguir = True
    while seguir:
        legajo = input("Ingresar el legajo del alumno: ")
        leg= int(legajo)
        if leg == 0:
            seguir = False
            menu()
        else:
            validacionLegajos(legajos,legajo)
            leg = int(legajo)
            
            if leg!=0:
                nombre=input("Ingresar nombre del alumno: ").title()
                while (nombre.isdigit() or nombre == "" ):
                    if nombre.isdigit():
                        print("Error! Se detecto solamente numeros.")
                    else:
                        print("Error. Re-ingrese el nombre del alumno")
                    nombre=input("Ingrese el nombre del alumno: ").title()
                legajos.append(legajo)
                nomAlumnos.append(nombre)
        

def cargarMateria(materias):
    print("Carga de materias (Ingrese 0 para terminar)")
    seguir = True
    while seguir:
        materia=input("Ingrese el nombre de la materia: ").title()

        if materia == "0":
            seguir = False
            menu()
        else:
            if elementoExistente(materias, materia):
                print("Esta materia ya ha sido cargada anteriormente")
            while materia.isdigit():
                print("Error! Se detecto solamente numeros.")
                materia=input("Ingrese el nombre de la materia: ").title()
            if not elementoExistente(materias,materia):
                materias.append(materia)
                print(f"Materia cargada con exito!, {materias}")


def cargarNota(matriz, legajos, materias):
    print("Carga de notas a traves del Legajo (Ingrese legajo 0 para terminar)")
    seguir = True
    while seguir:
        legajo = int(input("Ingrese numero de Legajo del alumno:\n"))
        if legajo == 0:
            seguir= False
            menu()
            
        posLegajo = buscarElem(legajos, legajo)
        while posLegajo == -1:
            print("Legajo ingresado no encontrado")
            legajo = int(input("Ingrese numero de Legajo del alumno (0 para terminar):\n"))
            if legajo == 0:
                return
            posLegajo = buscarElem(legajos, legajo)
            
        print("\nLista de Materias:")
        for i in range(len(materias)):
            print(f"{i+1}. {materias[i]}")
        materia = int(input("\nSeleccione materia a la cual cargar la nota:\n"))
        while materia > len(materias) or materia < 1:
            materia = int(input("Valor ingresado incorrecto\nIntente nuevamente:\n"))
            
        nota = int(input("Ingrese nota:\n"))
        while nota > 10 or nota < 1:
            nota = int(input("Valor ingresado incorrecto\nIntente nuevamente:\n"))
            
        matriz[posLegajo][materia-1] = nota
        print("Nota cargada exitosamente\n")


def actualizarNota(matriz, legajos, materias):
    print("Actualizacion de notas (legajo 0 para terminar)")
    seguir = True
    while seguir:
        legajo = int(input("Ingresar el legajo del alumno: "))
        
        if legajo == 0:
            seguir = False
            return

        posAlumno = buscarElem(legajos, legajo)
        while posAlumno == -1:
            print("Legajo no encontrado en el registro de alumnos")
            legajo = int(input("Ingrese otro legajo (0 para terminar): "))
            if legajo == 0:
                seguir = False
                return
            posAlumno = buscarElem(legajos, legajo)
        
        if seguir:
            print("\nMaterias disponibles:")
            for i in range(len(materias)):
                print(f"{i+1}. {materias[i]}")
                
            num_materia = int(input("Seleccione el numero de materia: "))
            while num_materia < 1 or num_materia > len(materias):
                print("Numero de materia invalido")
                num_materia = int(input("Seleccione el numero de materia: "))
            
            posMateria = num_materia - 1
            
            nota_actual = matriz[posAlumno][posMateria]
            print(f"Nota actual en {materias[posMateria]}: {nota_actual}")
            
            nota = int(input("Nueva nota del alumno (1-10): "))
            while nota < 1 or nota > 10:
                print("La nota debe estar entre 1 y 10")
                nota = int(input("Ingrese la nota nuevamente (1-10): "))
            
            matriz[posAlumno][posMateria] = nota
            print(f"Nota actualizada correctamente: {materias[posMateria]} = {nota}")
            print("-" * 50)


def mostrarTabla(matriz, materias, legajos):
    print("TABLA DE ALUMNOS")
    encabezado ="Legajo\t"
    for materia in materias:
        encabezado += materia + "\t"
    print(encabezado) 
    for i in range(len(legajos)):
        fila = str(legajos[i]) + "\t"
        for nota in matriz[i]:
            fila += str(nota) + "\t"
        print(fila)


def buscarAlumno(matriz, materias, legajos):
    legajo_buscar = int(input("Ingrese el legajo a buscar: "))
    encabezado = ""
    for materia in materias:
        encabezado += materia + "\t"

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscar:
            fila = str(legajos[i]) + "\t"
            for nota in matriz[i]:
                fila += str(nota) + "\t"
            print(encabezado)
            print(fila)
        else:
            print("Legajo no encontrado")


def ordenarInformacion(matriz, materias, legajos):
    print("Ordenar informacion (0 para volver al menu)")
    seguir = True
    while seguir: 
        print("""
        1 - Ordenar por promedio
        2 - Filtrar por materia
        3 - Ordenar por legajo
        0 - Volver al menu principal
        """)

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 0:
            seguir = False
            return
        elif opcion == 1:
            hay_notas = False
            for i in range(len(matriz)):
                if any(nota != 0 for nota in matriz[i]):
                    hay_notas = True
                    
            if not hay_notas:
                print("No hay notas cargadas para mostrar promedios")
                continue
                
            alumnos = []
            for i in range(len(matriz)):
                notas_validas = [nota for nota in matriz[i] if nota != 0]
                if notas_validas:
                    promedio = sum(notas_validas) / len(notas_validas)
                else:
                    promedio = 0
                alumnos.append((promedio, legajos[i], matriz[i]))

            alumnos.sort(reverse=True)

            print("\nAlumnos ordenados por promedio (mayor a menor): ")
            for promedio, legajo, notas in alumnos:
                print(f"Legajo: {legajo} | Promedio: {promedio:.2f} | Notas: {notas}")
                
        elif opcion == 2:
            print("\nMaterias disponibles:")
            for i in range(len(materias)):
                print(f"{i+1}. {materias[i]}")
            
            num_materia = int(input(f"Seleccione el numero de materia (1 a {len(materias)}): "))
            while num_materia < 1 or num_materia > len(materias):
                print("Numero de materia invalido")
                num_materia = int(input(f"Seleccione el numero de materia (1 a {len(materias)}): "))
            
            indice_materia = num_materia - 1
            print(f"\nNotas de la materia '{materias[indice_materia]}':")
            
            alumnos_materia = []
            for i in range(len(matriz)):
                alumnos_materia.append((matriz[i][indice_materia], legajos[i]))
            alumnos_materia.sort(reverse=True)
            
            for nota, legajo in alumnos_materia:
                if nota != 0:
                    print(f"Legajo: {legajo} | Nota: {nota}")
                else:
                    print(f"Legajo: {legajo} | Sin nota")
                    
        elif opcion == 3:
            alumnos = []
            for i in range(len(matriz)):
                alumnos.append((legajos[i], matriz[i]))

            alumnos.sort(reverse=True)

            print("\nAlumnos ordenados por legajo (mayor a menor): ")
            for legajo, notas in alumnos:
                print(f"Legajo: {legajo} | Notas: {notas}")
        else:
            print("Opcion invalida. Intente nuevamente.")
        
        print("-" * 50)


def mostrarEstadisticas(matriz, materias, legajos):
    
    opcion = input()
    if opcion == "0":
        return
    
    hay_notas = False
    for i in range(len(matriz)):
        for j in range(len(materias)):
            if matriz[i][j] != 0:
                hay_notas = True
    
    if not hay_notas:
        print("No hay notas cargadas en el sistema para mostrar estadisticas.")
        return
    
    print("\n PROMEDIO POR MATERIA")
    for j in range(len(materias)):
        notas = []
        for i in range(len(legajos)):
            if matriz[i][j] != 0:
                notas.append(matriz[i][j])
        
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"{materias[j]}: {promedio:.2f} (basado en {len(notas)} notas")
        else:
            print(f"{materias[j]}: Sin notas cargadas")
    
    print(f"\n PROMEDIO GENERAL")
    todas_las_notas = []
    for i in range(len(legajos)):
        for j in range(len(materias)):
            if matriz[i][j] != 0:
                todas_las_notas.append(matriz[i][j])
    
    if todas_las_notas:
        promedio_general = sum(todas_las_notas) / len(todas_las_notas)
        print(f"Promedio general: {promedio_general:.2f}")
        print(f"Total de notas: {len(todas_las_notas)}")
    else:
        print("No hay notas cargadas")

    print("\n--- PROMEDIO POR ALUMNO")
    for i in range(len(legajos)):
        notas = []
        for j in range(len(materias)):
            if matriz[i][j] != 0:
                notas.append(matriz[i][j])
        
        if notas:
            promedio_alumno = sum(notas) / len(notas)
            print(f"Legajo {legajos[i]} Promedio: {promedio_alumno:.2f} ({len(notas)} notas cargadas)")
        else:
            print(f"Legajo {legajos[i]}  Sin notas cargadas")
    
    print("\n ESTADISTICAS ADICIONALES")
    if todas_las_notas:
        nota_maxima = max(todas_las_notas)
        nota_minima = min(todas_las_notas)
        print(f"Nota mas alta: {nota_maxima}")
        print(f"Nota mas baja: {nota_minima}")
        
        aprobados = len([nota for nota in todas_las_notas if nota >= 4])
        desaprobados = len([nota for nota in todas_las_notas if nota < 4])
        print(f"Notas aprobadas: {aprobados}")
        print(f"Notas desaprobadas: {desaprobados}")
        menu()

"""
    FUNCION DEL MENU DEL PROGRAMA
"""
def menu():
    materias, legajos, nomAlumnos = crearVectores()
    matriz = matrizAleatoria(legajos, materias)
    
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
    while (opc != 9):
        

        opc = int(input("Ingrese una opcion: "))

        if (opc < 0 or opc > 9):
            opc = int(input("Ingrese una opcion valida: "))

        if (opc == 1):
            cargarAlumnos(nomAlumnos,legajos)
        elif(opc ==2):
            cargarMateria(materias)
        elif(opc ==3):
            cargarNota(matriz, legajos, materias)
        elif(opc ==4):
            actualizarNota(matriz,legajos,materias)
        elif(opc ==5):
            mostrarTabla(matriz,materias,legajos)
        elif(opc ==6):
            ordenarInformacion(matriz,materias,legajos)
        elif(opc == 7):
            buscarAlumno(matriz,materias,legajos)
        elif(opc == 8):
            mostrarEstadisticas(matriz,materias,legajos)