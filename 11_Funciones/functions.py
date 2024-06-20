'''
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

'''
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

# 4)

# 5)

# 6)

# 7)

# 8)

# 9)

# 10)

# 11)

# 12)

# 13)

# 14)

# 15)

# 16)

# 17)

# 18)

# 19)

# 20)

# 21)

# 22)

# 23)