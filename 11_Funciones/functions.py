# Los usuarios creamos funciones para hacer el código más legible y reutilizable
# En Python tenemos la palabra reservada 'def' para definir las funciones
# En la definición podemos declarar parámetros, los cuales tendremos que pasar cuando llamemos a la función

# DECLARACIÓN DE FUNCIONES SIN PARÁMETROS
def print_name():
    nombre = 'Diego '
    apellido = 'González'
    print(nombre + apellido)
print_name()

# FUNCIONES QUE RETORNAN VALORES (1)
# Usaremos return en la función
def print_name():
    nombre = 'Diego '
    apellido = 'González'
    nombre_completo = nombre + apellido
    return nombre_completo
print(print_name())

# DECLARACIÓN DE FUNCIONES CON PARÁMETROS
def cuadrado(base):
    elevado = base * base
    return (elevado)
print(cuadrado(5))

def mayor(num1, num2):
    if num1 > num2:
        print('{} es mayor' .format(num1))
    elif num1 < num2:
        print('{} es mayor' .format(num2))
    else:
        print('Los dos números son iguales')
mayor(1,1)

lista = [1,2,4,5]

def añadir_ordenado(lista, numero):
    lista.append(numero)
    lista.sort()
    return lista
print(añadir_ordenado(lista, 3))

## Podemos pasar los parámetros con clave y valor. Esto es útil en caso de que la función reciba
## muchos parámetros y no sepamos el orden de introducción
mayor(num2=9, num1=1)

# TIPO DE DATO RETORNADO
## Nuestra función puede devolver cualquier tipo de dato:
### Int, Float, Double, Set, Lista, etc.
### clase function
### clase None -> la que no tiene return, solo con print
print(type(añadir_ordenado(lista,3)))
print(type(cuadrado))
print(type(mayor(2,3)))


# FUNCIONES CON VALORES POR DEFECTO
## Podemos ver que si no le pasamos ningún parámetro a la función ejecuta el primer sector del
## código, mientras que si insertamos parámetros, ejecuta la segunda parte del código
def num_default(numero = 'null'):
    if numero == 'null':
        print('No has introducido ningún valor:', numero)
    else:
        print('Has introducido el número', numero)
num_default(100)


# FUNCIONES QUE RECIBEN UN Nº ARBITRARIO DE PARÁMETROS
def suma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total
print(suma(5,10,25))

# PASAR FUNCIONES COMO PARÁMETRO A OTRAS FUNCIONES
mayor(cuadrado(2), cuadrado(3))


# EJERCICIOS

# 1) Crea una función que sume dos valores y devuelva la suma
def suma_dos_numeros(numero1, numero2):
    return (numero1 + numero2)
print(suma_dos_numeros(21,34))


# 2) Haz una función que calcule el área de un círculo
## area = π x r²
def area_circulo(lado):
    pi = 3.141592
    area = pi * lado * lado
    return area
print(area_circulo(5))


# 3) Haz una función que sume todos los números que se le pase, y que compruebe que todos son números
def suma_total(*numeros):
    total = 0
    for num in numeros:
        if isinstance(num,(int,float)):
            total += num
        else:
            return TypeError
    return (total)
print(suma_total(10,5,6,'else')) 


# 4) Haz una función que pase de grados Cº a Fº
## Fº = (Cº * 9/5) + 32
def fahrenheit(grados):
    grados_f = (grados * 9 / 5) + 32
    return grados_f
print(fahrenheit(30))


# 5) Haz una función que devuelva la estación del mes introducido
def estacion(mes):
    invierno = ['enero', 'febrero', 'diciembre']
    verano = ['junio', 'julio', 'agosto']
    otoño = ['septiembre', 'octubre', 'noviembre']
    primavera = ['marzo', 'abril', 'mayo']
    if mes in primavera:
        print('El mes introducido ({}) pertenece a Primavera' .format(mes))
    elif mes in verano:
        print('El mes introducido ({}) pertenece a Verano' .format(mes))
    elif mes in otoño:
        print('El mes introducido ({}) pertenece a Otoño' .format(mes))
    elif mes in invierno:
        print('El mes introducido ({}) pertenece a Invierno' .format(mes))     
    else:
        primavera('El mes introducido no es válido, prueba a escribirlo en minúsculas')
estacion('enero')


# 6) Haz una función que calcule la pendiente de una ecuación lineal dada
## y = m*x + c
def pendiente(m,x,c=0):
    print('La pendiente de la ecuación {} * {} + {} es {}' .format(m,x,c,m))

m = int(input('Introduzca el valor del coeficiente: '))
x = int(input('Introduzca el valor de la variable: '))
c = int(input('Introduzca el valor de la constante: '))
pendiente(m,x,c)


# 7) Haz una función que calcule los resultados de una ecuación cuadrática
## ax² + bx + c = 0
## x = (-b ± √(b²-4ac)) / (2a)
import math
def ec_cuadratica(a=0,b=0,c=0):
    if (b*b)-(4*a*c) >= 0:
        resultado1 = (-b + math.sqrt((b*b)-(4*a*c))) / (2*a)
        resultado2 = (-b - math.sqrt((b*b)-(4*a*c))) / (2*a)
        print('Los valores de x para la ecuación {}x² + {}x + {} son {:.2f} y {:.2f}' .format(a,b,c,resultado1,resultado2))
    else:
        print('Math error')
    
a = int(input('Introduzca el valor del coeficiente de x²: '))
b = int(input('Introduzca el valor del coeficiente de x: '))
c = int(input('Introduzca el valor de la constante: '))
ec_cuadratica(a,b,c)


# 8) Haz una función que imprima una lista que se le pasa por parámetro
def print_list(lista):
    for element in lista:
        print(element)
print_list([1,2,3,4,5])


# 9) Haz una función que revierta una lista
def reverse_list(lista):
    nueva_lista = []
    for element in range(len(lista)-1, -1, -1):
        nueva_lista.append(lista[element])
    print(nueva_lista)
reverse_list([1,2,3,45,6])


# 10) Haz una función que ponga la primera letra en mayúscula de las palabras de una lista
def capitalize(lista):
    lista_cap = []
    for string in lista:
        if isinstance(string, str):
            lista_cap.append(string.capitalize())
        else:
            return TypeError
    print(lista_cap)
capitalize(['hola','que tal','adios'])


# 11) Haz una función que añada un nuevo elemento a una lista que se le pasa como parámetro
def add_item(lista, item):
    lista.append(item)
    print(lista)
add_item(['a','b','c'], 'd')


# 12) Haz ahora una función que elimine un elemento de una lista que se le pasa como parámetro
def remove_item(lista):
    elemento_eliminado = lista.pop()
    print('Se ha eliminado el elemento {}. Lista resultante: {}' .format(elemento_eliminado, lista))
remove_item([1,2,3,4,5])

def remove_item2(lista, elemento):
    for item in lista:
        if elemento == item:
            lista.remove(3)
    print(lista)
remove_item2([1,2,3,4,5,6,3,1,3],3)


# 13) Haz una función que calcule la suma de números desde 0 hasta el que se pasa como parámetro
def suma_all(n):
    count = 0
    suma = 0
    while count <= n:
        suma += count
        count += 1
    return(suma)
print(suma_all(56)) # 1596

# 14) Haz una función que cuente desde 0 hasta n los números pares e impares, siendo n un número
# entero pasado como argumento 
def pares_e_impares(num):
    count_pares = 0
    count_impares = 0
    for i in range(0,num+1):
        if i % 2 == 0:
            count_pares += 1
        elif i % 2 != 0:
            count_impares += 1
    print('Hay {} números impares' .format(count_impares))
    print('Hay {} números pares' .format(count_pares))
pares_e_impares(100)


# 15) Haz una funcion que calcule el factorial de un número
## Con recursividad
def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))
print(factorial(5))

## Sin recursividad
def factorial2(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial
print(factorial2(5))


# 16) Haz una función que diga si un número es primo o no
def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    else:
        return True
print(primo(8))

string = 'Hola Hola'
print(string.find('Hola'))
print(string.rfind('Hola'))

# 17) Haz una función que diga si todos los elementos de una lista son únicos o no
def unique(lista):
    return len(lista) == len(set(lista))

lista = [1,2,3,4,5,6]
lista2 = ['hola', 'hola', 'Hola']
print(unique(lista))
print(unique(lista2))


# 18) Haz una función que compruebe que todos los elementos sean del mismo tipo
def mismo_tipo(lista):
    tipo = type(lista[0])
    for item in lista:
        if type(item) != tipo:
            return False
    else:
        return True
list = [1,2,3,4,'4.0']
print(mismo_tipo(list))