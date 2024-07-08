# Un módulo es un archivo que contiene un conjunto de códigos y funciones que pueden ser incluidas en nuestra aplicación
# Para crear un módulo escribiremos nuestro código en un archivo .py, crearemos modulo1.py
# Usaremos la palabra reservada import para importar las funciones del modulo1
import modulo1
print(modulo1.generate_full_name('Diego', 'Gonzalez'))

# Podemos renombrar las funciones importadas de esta forma
from modulo1 import generate_full_name as generador_de_nombres
print(generador_de_nombres('Juan', 'Pérez'))

# También tenemos módulos predefinidos, usaremos los más comunes como math, datetime, os, sys, random, etc.


# MÓDULO OS
## El módulo os sirve para llevar a cabo funciones del sistema operativo tales como crear,
## eliminar o cambiar directorios, ver su contenido o cambiarlo

import os

os.mkdir('dir_prueba') # Crea un directorio en el wd actual

directorio = os.getcwd() # Hace un pwd
print(directorio)

os.chdir('dir_prueba') # Cambia el directorio de trabajo por un subdirectorio del actual wd

directorio = os.getcwd()
print(directorio)

os.chdir('..') # Ahora estamos volviendo a un directorio padre usando ..
directorio = os.getcwd()
print(directorio)

os.rmdir('dir_prueba') # Eliminamos el directorio que hemos creado 


# MÓDULO SYS
## El módulo sys proporciona funciones y variables usadas para manipular diferentes partes del
## entorno de ejecución.

import sys
# ejecutamos con python3 modules.py Diego 30diaspython
print('Bienvenido {}. Disfrute el reto {}!' .format(sys.argv[1], sys.argv[2]))
# sys.argv devuelve una lista de comandos por terminal, 0 es el nombre del script (modules.py), y a partir 
# de 1 son los argumentos que se le pasan a la función

sys.maxsize # Devuelve el int más grande (9223372036854775807)
sys.path # El path del entorno de ejecución
sys.version # Para saber la versión de python que se está usando


# MÓDULO STATISTICS
## Proporciona funciones para información numérica y estadísticas matemáticas (mean, median, mode, etc.)

from statistics import *

edades = [20,21,24,19,27,26,22,23,22,21,24,23,20]
print(mean(edades)) # Devuelve la media de edades
print(median(edades)) # Devuelve la mediana de edades (la del medio)
print(mode(edades)) # Devuelve el valor que aparece más, si hay empate devuelve el primero que sale
print(stdev(edades)) # Devuelve la desviación típica de edades


# MÓDULO MATH
## Contiene muchas operaciones matemáticas y constantes
## Podemos importar todas las funciones del módulo usando from math import *, evitando poner así math. en todas las llamadas al módulo

import math
print(math.pi) # Constante del número π
print(math.e) # Constante del número e
print(math.sqrt(36)) # Raíz cuadrada
print(math.pow(3,2)) # Número 3 elevado a 2
print(math.floor(9.81)) # Redondeo el número hacia abajo
print(math.ceil(9.81)) # Redondeo hacia arriba
print(math.log10(100)) # Logaritmo en base 10


# MÓDULO STRING
## Proporciona una serie de funciones útiles para trabajar con cadenas de texto

from string import *
print(ascii_letters) # Devuelve todas las letras ASCII
print(digits) # Devuelve todos los dígitos
print(punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# MÓDULO RANDOM
## Este módulo tiene muchas funciones que generan números pseudoaleatorios 

from random import *
print(random()) # Devuelve un número aleatorio entre 0.00 y 0.9999...
print(randint(5,20)) # Devuelve un número entero entre 5 y 20 (a y b)



# EJERCICIOS

# 1) Escribe una función que genere un user id con 6 letras o números random

def generate_random_id():
    numeros_y_letras = ascii_letters + digits
    randomid = ''.join(choices(numeros_y_letras,k=6))
    print(randomid)    

generate_random_id()

def generate_random_id2():
    id = ''
    i = 0
    while i<6:
        rand = randint(0,49)
        i +=1
        if rand % 2 == 0:
            id = id + ascii_letters[rand]
        else:
            id = id + str(randint(0,9))
    print(id)

generate_random_id2()

# 2) Modifica la función anterior para que recoja por pantalla el número de ids y el número de caracteres

def generate_n_ids(numids, numchar):
    numeros_y_letras = ascii_letters + digits
    ids = []
    for _ in range(numids):
        random_id = ''.join(choices(numeros_y_letras, k=numchar))
        ids.append(random_id)
    return ids

print(generate_n_ids(5,6))


# 3) Crea una función que genere un color rgb (tres valores de 0 a 255)
## Usaremos la biblioteca Pillow para procesar el código rgb que hemos generado y lo guardaremos en un archivo png
from PIL import Image # pip install Pillow

def generate_rgb():
    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rgb

def save_rgb_image(filename, width=100, height=100):
    rgb = generate_rgb()
    image = Image.new('RGB', (width, height), rgb)
    image.save(filename)
    print(f"El color RGB generado {rgb} ha sido guardado como imagen en {filename}")

filename = 'color_image.png'
save_rgb_image(filename)


# 4) Escribe una función que genere un color formado por 6 caracteres hexadecimales

def generate_hexa():
    hexadecimal = digits + 'A' + 'B' + 'C' + 'D' + 'E' + 'F' 
    hexa = choices(hexadecimal, k=6)
    color = '#'
    for code in hexa:
        color = color + code 
    return color

print(generate_hexa())

# 5) Haz lo mismo, pero con códigos RGB random en formato string

def generate_rgb():
    color_rgb = 'rgb({},{},{})' .format(randint(0,255),randint(0,255),randint(0,255)) 
    return color_rgb

print(generate_rgb())

# 6) Haz una función generate_colors('hexa'/'rgb', n) que, dependiendo de si se especifica hexa o rgb, genere n códigos de colores

def generate_colors(code, n):
    i = 0
    lista = []
    if code == 'hexa':
        while i < n:
            lista.append(generate_hexa())
            i += 1
    elif code == 'rgb':
        while i < n:
            lista.append(generate_rgb())
            i += 1
    return lista

print(generate_colors('rgb', 5))
print(generate_colors('hexa', 7))


# 7) Crea una función llamada lista_aleatoria(lista) que devuelva una lista aleatoria

def lista_aleatoria(lista):
    lista_random = []
    longitud = len(lista)
    i = 0
    while i < longitud:
        elemento = lista.pop(randint(0,len(lista)-1))
        lista_random.append(elemento)
        i += 1
    return lista_random

lista = ['a', 'b', 'c', 'd', 'e']
print(lista_aleatoria(lista))


# 8) Crea una función que devuelva un lista de 7 números random únicos del 0-9

def seven_unique_numbers():
    lista = []
    i = 0
    digitos = list(digits)
    while i < 7:
        elemento = digitos.pop(randint(0,len(digitos)-1))
        lista.append(elemento)
        i += 1
    print(lista)

seven_unique_numbers()