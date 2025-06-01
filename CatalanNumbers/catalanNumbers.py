# Usamos un diccionario para la memoización
catalan_memo = {}

class Operations: # Corregido a PascalCase, aunque no la usaremos en la versión optimizada
    def __init__(self, i_val, j_val):
        self.i = i_val
        self.j = j_val

def catalenNumbersRecursive(n: int) -> int:
    if n <= 1:
        return 1

    # Si ya hemos calculado este valor, lo devolvemos del memo
    if n in catalan_memo:
        return catalan_memo[n]

    catalan_number = 0
    # C_n = sum_{i=0}^{n-1} C_i * C_{n-1-i}
    # El bucle 'i' va de 0 a n-1
    for i in range(n):
        # El primer término es C_i
        # El segundo término es C_{n-1-i}
        term1 = catalenNumbersRecursive(i)
        term2 = catalenNumbersRecursive(n - 1 - i)
        catalan_number += term1 * term2

    # Guardamos el resultado en el memo antes de devolverlo
    catalan_memo[n] = catalan_number
    return catalan_number
    