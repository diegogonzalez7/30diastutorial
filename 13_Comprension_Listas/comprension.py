# La comprensión de listas es una forma compacta de crear una lista a partir de una secuencia.
# Este método es más rápido que procesar una lista usando un bucle for
# sintaxis: [i for i in iterable if expression]

# Pasar un string a lista
## Primera forma
lenguaje = 'Python'
lista = list(lenguaje)
print(lista)

## Segunda forma
lista = [i for i in lenguaje]
print(lista)


# Generar una lista de números
numeros = [i for i in range(11)]    # generar números del 0 al 10
print(numeros)                      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Podemos hacer operaciones matemáticas también
cuadrados = [i * i for i in range(11)]
print(cuadrados)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# También podemos crear una lista de tuplas
nums = [(i, i * i) for i in range(11)]
print(nums)                      # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


# Podemos combinar la comprensión con una condición if
impares = [i for i in range(25) if i % 2 != 0]
print(impares)

numeros = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positivos = [i for i in numeros if i >= 0]
print(positivos)


# Funciones lambda
## sintaxis: x = lambda param1, param2, param3: param1 + param2 + param3
## print(x(arg1, arg2, arg3))

def sumar_dos_numeros(a,b):
    return a + b
print(sumar_dos_numeros(2,3))

# Cambiamos la función por una función lambda
sumar_dos_numeros = lambda a, b: a + b
print(sumar_dos_numeros(2,3))

elevar = lambda x, n: pow(x,n)
print(elevar(2,3))

# Funciones lambda encapsuladas en funciones
def power(base):
    return lambda n : base ** n

cubo = power (2)(3)
print(cubo)


# EJERCICIOS

# 1) Filtra la lista mostrando solo los números negativos y 0
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos = [i for i in numbers if i <= 0]
print(negativos)


# 2) Crea la siguiente lista de tuplas usando comprensión de listas
## [(0, 1, 0, 0, 0, 0, 0),
## (1, 1, 1, 1, 1, 1, 1),
## (2, 1, 2, 4, 8, 16, 32),
## (3, 1, 3, 9, 27, 81, 243),
## (4, 1, 4, 16, 64, 256, 1024),
## (5, 1, 5, 25, 125, 625, 3125),
## (6, 1, 6, 36, 216, 1296, 7776),
## (7, 1, 7, 49, 343, 2401, 16807),
## (8, 1, 8, 64, 512, 4096, 32768),
## (9, 1, 9, 81, 729, 6561, 59049),
## (10, 1, 10, 100, 1000, 10000, 100000)]
tupla = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(tupla)