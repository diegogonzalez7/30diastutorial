# Python admite varios tipos de operadore:

# OPERADORES DE ASIGNACIÓN

# =     -> Asignación de valores
## x = 4

# +=    -> Asignación de adición
## x += 2 (6) 

# -=    -> Asignación de sustracción
## x -= 2 (2) 

# *=    -> Asignación de producto
## x *= 2 (8)

# /=    -> Asignación de división
## x /= 4 (1)

# %=    -> Asignación del resto de la división
## x %= 3 (1)

# //=   -> Asignación del cociente de la división
## x //= 2 (2) 

# **=   -> Asignación del exponente
## x **= 3 (64) 

# &=    -> Hace un AND binario entre los dos números y asigna los valores coincidentes
## x &= 5 (101) (4 -> 100)

# |=    -> Hace un OR binario entre los dos números y asigna los valores coincidentes
## x |= 5 (101) (5 -> 101) 

# ^=    -> Hace un XOR binario entre los dos números y asigna los valores coincidentes
## x ^= 7 (111) (3 -> 011)

# >>=   -> Desplaza el valor binario un número de veces a la derecha y asigna dicho valor
## x = 2 (1 -> 001)

# <<=   -> Desplaza el valor binario un número de veces a la izquierda y asigna dicho valor
## x = 2 (16 -> 10000)


# OPERADORES ARITMÉTICOS
x = 2
y = 5

print('Suma:', x + y) # 7
print('Resta:', x - y) # -3
print('Multiplicación:', x * y) # 10
print('División:', y / x) # 2.5
print('División entera:', y // x) #2
print('Módulo o resto:', y % x) # 1
print('Exponente:', x ** y) # 32

# EJERCICIOS

## Calcula el área de un círculo cuyo radio sea 10

# Sabemos que la fórmula del área de un círculo es: A = π * r² 
radio = 10
pi = 3.14159
area = pi * (radio ** 2)
print('El área del cículo cuyo radio es', radio, 'es', area)

## Calcula la densidad de un líquido cuya masa es de 60 kg y el volumen es de 0.1 m³

# Sabemos que la densidad se calcula así: ρ = m / v
masa = 60
volumen = 0.1
densidad = masa / volumen
print('El volumen del líquido es', densidad, 'kg/m³')


# OPERADORES DE COMPARACIÓN

# ==    -> Devuelve True si los dos números son iguales, False en caso contrario
# !=    -> Devuelve True si los dos números son distintos, False en caso contrario
# >     -> Devuelve True si el primer número es mayor que el segundo, False en caso contrario
# <     -> Devuelve True si el primer número es menor que el segundo, False en caso contrario
# >=    -> Devuelve True si el primer número es mayor o igual que el segundo, False en caso contrario
# <=    -> Devuelve True si el primer número es menor o igual que el segundo, False en caso contrario

print(1==1) # True
print(1!=1) # False
print(len('hola')>len('adios')) # False (4 !> 5)
print(len('hola')<len('adios')) # True (4 < 5)
print(len('buenas')>=len('tardes')) # True (6 >= 6)
print(len('si')<=len('no')) # True (2 <= 2)

# Podemos usar is, is not, in o not in también:

print('1 es 1 =', 1 is 1) # True
print('1 no es 2 =', 1 is not 2) # True
print('C en ABD =', 'C' in 'ABD') # False
print('C no está en ABD =', 'C' not in 'ABD') # True


# OPERADORES LÓGICOS

# and -> Devuelve True si todas las sentencias son True, False en caso contrario 
# or  -> Devuelve True si alguna de las sentencias son True, False en caso contrario
# not -> Devuelve True si la sentencia es Falsa, False en caso contrario

print('10 mayor que 7 y 7 mayor que 4:', 10 > 7 and 4 > 1) # True
print('10 mayor que 100 y 1 mayor que 0:', 10 > 100 or 1 > 0) # True
print('3 no es mayor que 1:',not 3 > 1) # True


# EJERCICIOS DE REPASO

## Calcula el área de un triángulo cuyas base y altura las introduzca el usuario por pantalla

base = int(input('Introduzca la base: '))
altura = int(input('Introduzca la altura: '))
area_triangulo = base * altura
print('El área de el triángulo cuya base es', base, 'm y cuya altura es', altura, 'm es de', area_triangulo, 'm²')

## Calcula el perímetro de un triángulo y que el usuario introduzca la longitud de los lados

lado1 = int(input('Introduce la longitud del lado 1: '))
lado2 = int(input('Introduce la longitud del lado 2: '))
lado3 = int(input('Introduce la longitud del lado 3: '))
perimetro = lado1 + lado2 + lado3
print('El perímetro del triángulo es de', perimetro, 'metros')

## Calcula el perímetro y área de un rectángulo 

largo = int(input('Introduce el largo del rectángulo: '))
ancho = int(input('Introduce el ancho del rectángulo: '))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print('El perímetro del rectángulo es', perimetro_rectangulo, 'metros y el área es de', area_rectangulo, 'm²')

## Haz un código que simule esta tabla:
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")

## Haz un código que calcule el salario de un empleado

horas = int(input('Introduzca las horas trabajadas: '))
salario = int(input('Introduzca el salario por hora: '))
print('Su salario este mes es de', salario*horas,'€')