# General libraries and imports
import os
# Submodules from the program
from ParenthesisParsing.parenthesisParsing import parenthesisParsing

# Menu, returns integer
def menu() -> int:
    opcionEscogida = 0
    opcionesValidas = [1,2,3,4,5]
    while opcionEscogida not in opcionesValidas:
        print("-"*100)
        print(" "*38,"Numeros de Catalan")
        print("\tEscoja una de las opciones dadas en el menu")
        print("\t1.-Analisis sintactico de un compilador: Calculo de combinaciones validas para un numero de parentesis dado")
        print("\t2.-Caso real 2")
        print("\t3.-Caso real 3")
        print("\t4.-Caso real 4")
        print("\t5.-Salir")
        print("-"*100)
        opcionEscogida = int(input())
        os.system("cls")
    return opcionEscogida

def subMenu() -> int:
    opcionEscogida = 0
    opcionesValidas = [1,2,3]
    while opcionEscogida not in opcionesValidas:
        print("-"*100)
        print(" "*38,"Eleccion de Algoritmo")
        print("\tEscoja una de las opciones dadas en el menu")
        print("\t1.-Algoritmo Gloton")
        print("\t2.-Algoritmo Recursivo con Programacion Dinamica")
        print("\t3.-Volver al menu principal")
        print("-"*100)
        opcionEscogida = int(input())
        os.system("cls")
    return opcionEscogida

# main
def main():
    opcionMenuPrincipal = 0
    opcionDeAlgoritmo = 0
    while opcionMenuPrincipal != 5:
        opcionMenuPrincipal = 0
        opcionDeAlgoritmo = 0
        while opcionDeAlgoritmo not in [1,2]:
            opcionMenuPrincipal = menu()
            if opcionMenuPrincipal == 5:
                break
            opcionDeAlgoritmo = subMenu()
        
        match opcionMenuPrincipal:
            #Opcion parentiesis
            case 1:
                parenthesisParsing(opcionDeAlgoritmo)
            # Opcion caso 2
            case 2:
                if opcionDeAlgoritmo == 1:
                    # Algoritmo gloton
                    pass
                else:
                    # Algoritmo recursivo con programacion dinamica
                    pass
            # Opcion caso 3
            case 3:
                if opcionDeAlgoritmo == 1:
                    # Algoritmo gloton
                    pass
                else:
                    # Algoritmo recursivo con programacion dinamica
                    pass
            case 4:
                if opcionDeAlgoritmo == 1:
                    # Algoritmo gloton
                    pass
                else:
                    # Algoritmo recursivo con programacion dinamica
                    pass
            # Opcion caso 5
            case 5:
                print("Gracias por usar nuestro proyecto, que tenga buen dia")
                input()
                exit()
            case _:
                print("Error al escoger opcion valida del menu")
                input()
                os.system("cls")
                main()

if __name__ == "__main__": 
    main()