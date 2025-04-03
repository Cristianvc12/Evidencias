from mapify import mapify

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Función que eleva al cuadrado
def elevar_al_cuadrado(x):
    return x ** 2

# Aplicar la función a cada número en la lista
numeros_cuadrados = mapify(elevar_al_cuadrado, numeros)

print(list(numeros_cuadrados))

