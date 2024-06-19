# Un bucle en Python, como en cualquier otro lenguaje de programación, es una secuencia de
# instrucciones de código que se ejecuta repetidas veces, hasta que la condición especificada 
# en el bucle deja de cumplirse. Los bucles más importantes son el While y el For


# BUCLE WHILE
## Este bucle ejecuta una serie de sentencias repetidamente hasta que la condición se satisfaga
## Podemos añadir un bloque else para cuando se satisfaga la condición
import time
a = 0
while a < 10:
    print(a)
    a += 1
else: 
    print('Has llegado al 10')


# Break y Continue
## Usamos break cuando queramos que el bucle se detenga
a = 0
while a < 10:
    print(a)
    a += 1
    if a == 4:
        print('Has llegado al 4. Saliendo del bucle...')
        time.sleep(2)
        break

## Usamos continue para saltar la iteración actual y continuar a la siguiente
a = 0
print('Números pares hasta el 10')
while a < 10:
    if a % 2 != 0:
        a += 1
        continue
    print(a)
    a += 1
else: 
    print('Has llegado al 10')


# BUCLE FOR
## Este bucle se usa para iterar sobre una secuencia, ya sea una lista, tupla, diccionario, set o string
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for number in numeros:
    print(number)

string = 'Hola'
for letra in string:
    print(letra)

persona = {
    'nombre': 'Diego',
    'apellido': 'Gonzalez',
    'edad': 20,
    'pais': 'España',
    'estudiando': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Calle Alemania',
        'cpostal': '23775'
    }
}

for key, value in persona.items():
    print(key, value)

# Función range(start, end, step)
lista = list(range(0,21,2))
for item in lista:
    print(item)

# Bucle for anidado
for key in persona:
    if key == 'skills':
        for skill in persona['skills']:
            print(skill)

# For Else
## Hace la misma función que el else del bucle while

for number in lista:
    print(number)
else:
    print('Has llegado al final de la lista')

# Pass
## Cuando no queremos poner nada en la sentencia, podemos ponerle un pass para evitar errores
for number in [1,2,3]:
    pass



# EJERCICIOS

# 1) Itera del 0 al 10 usando bucles for y while
n = 0
while n <= 10:
    print(n)
    n += 1

for n in range(0,11):
    print(n)


# 2) Itera del 10 al 0 usando bucles for y while
n = 10
while n >= 0:
    print(n)
    n -= 1

for n in range(10,-1,-1):
    print(n)
 

# 3) Haz un bucle que haga un triángulo con 7 #
## Si ponemos en el print * x nos hace print del string x veces
for i in range(1, 8):
    print('Hola' * i)


# 4) Usa bucles anidados para crear lo siguiente:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# Con while
n = 8
count = 8
count2 = 8
while count > 0:
    while count2 > 0:
        print('# ' * n)
        count2 -= 1
    count -= 1

# Con for
for i in range(8):  # Outer loop for each row
    for j in range(8):  # Inner loop for each column in the row
        print('#', end=' ')  # Print # with a space, but don't go to a new line
    print()  # Go to the next line after printing 8 # characters

 
# 5) Usa bucles para imprimir el siguiente patrón:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# Con while
n = 0
while n <= 10:
    print('{} x {} = {}' .format(n, n, n*n))
    n += 1

# Con for
for i in range(11):
    print('{} x {} = {}' .format(i, i, i*i))


# 6) Itera una lista e imprime todos sus elementos
list = ['Python', 'Java', 'Pandas', 'Octave']
for len in list:
    print(len)
 
# 7) Usa un bucle para iterar los números del 0 al 100 imprimiendo solo números pares 
# Con while
n = 0
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1

# Con for
for i in range(101):
    if i % 2 == 0:
        print(i)
 
# 8) Usa un bucle para iterar los números del 0 al 100 imprimiendo solo números impares
# Con while
n = 0
while n <= 100:
    if n % 2 != 0:
        print(n)
    n += 1

# Con for
for i in range(101):
    if i % 2 != 0:
        print(i)


# 9) Usa un bucle para iterar los números del 1 al 100 y suma todos sus valores
# Con while
suma = 0
n = 0
while n <= 100:
    suma += n
    n += 1
else: 
    print('La suma de todos los números es', suma) 

# Con for
suma = 0
for i in range(101):
    suma += i
else: 
    print('La suma de todos los números es', suma)


# 10) Haz lo mismo que en el anterior, pero ahora suma los pares y los impares
# Con while
suma_pares = 0
suma_impares = 0
n = 0
while n <= 100:
    if n % 2 == 0: # Pares
        suma_pares += n
    elif n % 2 != 0: # Imares
        suma_impares += n
    n += 1
else:
    print('La suma de todos los nº pares es {} y la suma de todos los nº impares es {}' 
          .format(suma_pares, suma_impares))
    
# Con for
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0: # Pares
        suma_pares += i
    elif i % 2 != 0: # Imares
        suma_impares += i
else:
    print('La suma de todos los nº pares es {} y la suma de todos los nº impares es {}' 
          .format(suma_pares, suma_impares))
 
# 11) Importa la lista de países situada en countries.py e itera imprimiendo los países que empiecen por A
from countries import countries # Importamos la lista con todos los paises

for country in countries:
    if country[0] == 'A':
        print(country)
 

# 12) Importa la lista de países situada en countries.py e itera imprimiendo los países que contengan land
for country in countries:
    if 'land' in country:
        print(country)
 

# 13) Revierte una lista usando bucles
lista = []
lista1 = ['Hola', 'Adios']
for i in range(2):
    lista.append(lista1[i])

print(lista)

lista_ordenada = [1,2,3,4,5,6,7,8,9,10]
lista_reverse = []
for i in range(len(lista_ordenada), 0, -1):
    lista_reverse.append(lista_ordenada[i-1])

print('Lista original:', lista_ordenada)
print('Lista revertida:', lista_reverse)