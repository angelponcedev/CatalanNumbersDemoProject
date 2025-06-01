# Gets an integer and returns an integer
def factorial_recursivo(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("El input debe ser un número entero.")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0:  # Caso base: 0! = 1
        return 1
    else:  # Paso recursivo: n! = n * (n-1)!
        return n * factorial_recursivo(n - 1)