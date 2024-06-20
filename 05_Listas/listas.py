# En Python existen cuatro tipos de colecciones:

## Listas: colección ordenada y modificable que puede admitir duplicados.
## Tuplas: colección ordenada y no modificable que puede admitir duplicados.
## Colecciones (Sets): colección desordenada, no indexada y no modificada. No permite duplicados.
## Diccionarios: colección no ordenada, modificable e indexada. No permite duplicados.


# Podemos crear una lista usando funciones built-in o con corchetes ([])

lista1 = list()
lista2 = ['Python', 'C', 'Java']

# Podemos acceder a los valores de la lista usando el índice (empieza desde 0)
print('Los lenguajes más usados son {}, {} y {}' .format(lista2[0], lista2[1], lista2[2]))

# Las listas pueden tener elementos de distintos tipos de datos
lista_hibrida = ['str', 1, 1.112]


# Desempaquetar elementos de una lista, podemos usar * para alojar una sublista
# De esta forma, la sublista sería ['Portugal', 'España', 'Andorra']
paises = ['Paises Bajos','Francia','Reino Unido','Portugal','España','Andorra','Dinamarca']
nd, fr, uk, *peninsula_iberica, dn = paises

# Tal y como hemos hecho con los Strings (que funcionan como listas también), podemos partirlas 
p1 = paises[0:3]
p2 = paises[3:7]
print(p1,p2)

# Verificar si existe un elemento en una lista
existe = 'España' in paises # True


# MODIFICAR LISTAS

## Usaremos append() para añadir un elemento a una lista (lo añade al final)
paises.append('Suiza')
# ['Paises Bajos', 'Francia', 'Reino Unido', 'Portugal', 'España', 'Andorra', 'Dinamarca', 'Suiza']


## Podemos insertar elementos en un índice concreto usando insert(idx, item)
paises.insert(0,'Alemania')
# ['Alemania', 'Paises Bajos', 'Francia', 'Reino Unido', 'Portugal', 'España', 'Andorra', 'Dinamarca', 'Suiza']


## Para eliminar elementos de una lista usaremos pop(), sin argumentos elimina el último elemento,
## o podemos eliminar un índice concreto si lo pasamos como argumento
paises.pop(1)
print(paises)
# ['Alemania', 'Francia', 'Reino Unido', 'Portugal', 'España', 'Andorra', 'Dinamarca', 'Suiza']


## Podemos borrar un elemento de una lista o la lista completa haciendo del lista
del lista1

## Usando clear podemos vaciar una lista para dejarla vacía
lista2.clear()

## Mediante sort() ordenamos los valores de una lista, por orden alfabético o de menor a mayor
## Si pasamos reverse=True como argumento, la ordena revertida
paises.sort(reverse=True)
paises.sort()

## Podemos copiar el contenido de una lista en otra usando copy()
copia = paises.copy()

## El operador + permite juntar el contenido de dos listas
## Podemos usar extend() en vez de join(), funcionando de igual manera
neg = [-2,-1]
zero = [0]
pos = [1,2]
num_op = neg + zero + pos
num_extend = []
num_extend.extend(neg)
num_extend.extend(zero)
num_extend.extend(pos)


## count() para contar el número de veces que aparece un elemento en una lista
print(paises.count('Alemania'))

## Podemos obtener el índice de un elemento usando lista.index(item)
print(paises.index('España'))


# EJERCICIOS


#1) Declara una lista vacía
lista = list()

#2) Declara una lista con más de 5 elementos
lista2 = [1,2,3,4,5,6,7]

#3) Imprime la longitud de la lista
print('La longitud de la lista es', len(lista2))

#4) Imprime el primer elemento, el del medio y el último
print('El primer elemento de la lista es:', lista2[0])
print('El elemento del medio de la lista es:', lista2[len(lista2) // 2])
print('EL último elemento de la lista es:',lista2[-1])

#5) Declara una lista mixta 
lista_mixta = ['Diego', 20, 1.69, 'diegogonza@gmail.com']
print(lista_mixta)

#6) Modifica la lista e imprímela
lista_mixta[2] = 1.80
print('La lista modificada es:', lista_mixta)

#7) Modifica el nombre y ponlo todo en mayúscula
lista_mixta[0] = lista_mixta[0].upper()
print('Lista con nombre en mayúsucula:', lista_mixta)

#8) Comprueba si existe un elemento en una lista
existe_num = 1 in lista2
print('¿El número {} existe en la lista {}?: {}' .format(lista2[0], lista2, existe_num))

#9) Ordena una lista usando sort()
lista_sort = ['Zambia','Andorra','Polonia','Portugal']
lista_sort.sort()
print('Ordenada:', lista_sort)

#10) Revierte el orden de la lista
lista_sort.sort(reverse=True)
print('Ordenada revertida:', lista_sort)

#11) Elimina el primer elemento de la lista
del lista_sort[0]
print('Lista sin el primer elemento:', lista_sort)

#12) Vacía la lista
lista_sort.clear()

#13) Destruye la lista
del lista_sort

#14) Crea una lista con 10 edades y haz lo siguiente:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

# Ordena la lista y obtén la edad máxima y mínima
ages.sort()
edad_minima = ages[0]
edad_maxima = ages[-1]
print('La edad máxima es {} y la edad mínima es {}' .format(edad_maxima, edad_minima))

# Añade otra vez la edad máxima y mínima a la lista
ages.insert(0, edad_minima)
ages.insert(-1, edad_maxima)
print('La lista con los elementos nuevos insertados es:', ages)

# Encuentra la edad que se encuentra en la mitad de la lista, dos si hay pares
if len(ages) % 2 == 0:
    mitad = len(ages) // 2
    print('Los elementos en la mitad son {} y {}' .format(ages[mitad-1], ages[mitad]))
else:
    mitad = len(ages) // 2
    print('El elemento situado en la mitad es {}' .format(ages[mitad]))

# Encuentra la edad media y devuélvela
suma = 0
average = 0
for i in range(0,len(ages)):
    suma += ages[i]
average = suma / len(ages)
print('La edad media es', average)

# Encuentra el rango de edades
rango = edad_maxima - edad_minima
print('Rango de edades:', rango)

# Compara el valor de (min - media) y (max - media) usando abs()

dif_min = abs(edad_minima - average)
dif_max = edad_maxima - average
print('La diferencia entre la media y la edad mínima es {} años, mientras que con la máxima es de {} años' .format(dif_min, dif_max))