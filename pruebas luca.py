materias=["Matematica", "Programacion 1"]

def menu():
    print("Menu")
    

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

    menu

cargarMateria()
print(materias)