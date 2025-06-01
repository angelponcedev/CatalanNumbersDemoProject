import os
import itertools

from CatalanNumbers.catalanNumbers import catalenNumbersRecursive
from CatalanNumbers.factorial import factorial_recursivo

def validateParsing(parenthesisList: list) -> bool:
    """
    Valida si una lista de caracteres de paréntesis está bien formada.
    Una secuencia es válida si:
    1. Al leer de izquierda a derecha, el número de '(' encontrados
       es siempre mayor o igual al número de ')' encontrados.
    2. El número total de '(' es igual al número total de ')'.
    """
    balance = 0
    for char_p in parenthesisList:
        if char_p == '(':
            balance += 1
        elif char_p == ')':
            balance -= 1
        
        # Si en algún momento el balance es negativo, significa que hay un ')'
        # sin un '(' correspondiente antes.
        if balance < 0:
            return False
            
    # Al final, el balance debe ser exactamente 0 para que todos los '('
    # tengan su correspondiente ')'.
    return balance == 0

# Trying all different combinations for N and validating them
def greedyParsing(n: int) -> int:
    """
    Genera todas las secuencias posibles con n '(' y n ')',
    valida cada una y devuelve el recuento de las válidas.
    """
    if n < 0:
        raise ValueError("El número de pares de paréntesis no puede ser negativo.")
    if n == 0:
        # Una cadena vacía se considera una secuencia válida de 0 pares.
        return 1 

    total_length = 2 * n
    # Creamos una lista de índices de posición: [0, 1, ..., 2*n - 1]
    positions = list(range(total_length))
    
    valid_combination_count = 0
    
    # Iteramos sobre todas las formas de elegir 'n' posiciones para los '('
    # de un total de 'total_length' posiciones.
    # Cada 'open_indices_tuple' será una tupla de n índices donde irán los '('.
    for open_indices_tuple in itertools.combinations(positions, n):
        # Convertimos la tupla de índices a un set para búsquedas rápidas (O(1) en promedio)
        open_indices_set = set(open_indices_tuple)
        
        current_combination = [''] * total_length # Inicializamos la lista de caracteres
        
        # Construimos la secuencia de paréntesis actual
        for i in range(total_length):
            if i in open_indices_set:
                current_combination[i] = '('
            else:
                current_combination[i] = ')'
        
        # Validamos la combinación generada
        if validateParsing(current_combination):
            valid_combination_count += 1
            
    return valid_combination_count

def parenthesisParsing(algoritmo):
    n = -1
    while n < 0:
        os.system("cls")
        print('''1.-Parser de Contenido de un archivo de codigo: Calculo de combinaciones validas para un numero de parentesis dado
                
                Descripcion\nEl equipo de desarrollo "Syntax Sorcerers" está trabajando en el desarrollo de un compilador, el compilador debe ser capaz de identificar si un grupo de parentesis
                esta bien anidado, para esto les gustaria conocer cuantas son las combinaciones validas para un numero N dado de pares de parentesis.
                La utilidad de conocer este numero es para identificar hasta que numero de pares de parentesis es conveniente realizar testeos para verificar el funcionamiento correcto del compilador.
                
                El Desafío:
                
                Antes de implementar el analizador sintáctico (parser) completo para el compilador, el equipo necesita realizar algunas estimaciones para generar casos de prueba exhaustivos. Para ello, quieren saber:
                Dado un número par de caracteres de paréntesis, digamos N (lo que equivale a N pares de paréntesis), 
                ¿cuántas secuencias parentesis válidos y únicos se pueden formar?
                
                Una grupo de parentesis es "válido" si cumple las reglas estándar de los paréntesis bien formados:

                    -El número total de paréntesis de apertura ( es igual al número total de paréntesis de cierre ). (Esto ya está implícito al usar N pares).
                    -Al leer la secuencia de izquierda a derecha, en ningún momento el recuento de paréntesis de cierre ) puede superar el recuento de paréntesis de apertura (.
                    
                Tarea para el Equipo:
                
                El equipo "Syntax Sorcerers" necesita desarrollar una forma de calcular este número. Se les ha proporcionado un entero N, que representa el número de total de paréntesis que se utilizarán.
                Deben determinar cuántas cadenas distintas de N caracteres, compuestas por N/2 paréntesis de apertura y N/2 parentesis de cierre, forman una estructura de codigo válido.
                
                Ejemplos para N (pares de paréntesis):

                    Si N = 0 (0 pares, 0 caracteres en total):
                    Hay 1 forma válida: "" (la cadena vacía, representando ninguna plantilla).


                    Si N = 1 (1 par, 2 caracteres en total):
                    Hay 1 forma válida: ()


                    Si N = 2 (2 pares, 4 caracteres en total):
                    Hay 2 formas válidas: (()), ()()


                    Si N = 3 (3 pares, 6 caracteres en total):
                    Hay 5 formas válidas: ((())), (()()), (())(), ()(()), ()()()
                    
~~~~ Porfavor Ingrese la cantidad de PARES de parentesis del que se desea conocer la cantidad de combinaciones validas ~~~~~''')
        n = abs(int(input()))
        
        #Logica para numeros de catalan recursivamente con programacion dinamica
        if algoritmo == 1:
            combinacionesValidas = greedyParsing(n)
        else:
            combinacionesValidas = catalenNumbersRecursive(n)
        combinacionesTotales = factorial_recursivo(n)
        print(f'''  
                    ---------------------------------------------------------------------            
                    Pares de parentesis: {n}
                    numero de combinaciones de parentesis totales: {combinacionesTotales} 
                    numero de combinaciones validas calculadas: {combinacionesValidas}
                    ---------------------------------------------------------------------
                    ''')
        input()
    return