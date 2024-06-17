'''
# Un set es una colección desordenada, no indexada y sin elementos repetidos
# En Python suele usarse para almacenar elementos únicos


# CREACIÓN DE UN SET
## A diferencia de las listas [] y de las tuplas (), los sets se crean con {}
set0 = set()
frutas_set = {'manzana', 'pera', 'plátano', 'sandía'}
print(frutas_set)

# LONGITUD DE UN SET
print(len(frutas_set))

# ACCESO A ELEMENTOS
## Puesto un set no está indexado, deberemos usar bucles para acceder al contenido
## Sí podremos comprobar si existe un elemento en un set

existe = 'manzana' in frutas_set
print(existe) # True

# MODIFICAR UN SET
## Podemos añadirlos uno a uno usando add(), los añade en posiciones aleatorias
## O podemos usar update() para añadir varios, recibe una lista como argumento
frutas_set.add('melón')
print(frutas_set)

frutas_set.update(['mandarina', 'naranja'])
print(frutas_set)

# BORRAR ELEMENTOS
frutas_set.remove('pera')
print(frutas_set)

## pop() elimina un elemento random del set y lo recupera
fruta = frutas_set.pop()
print(fruta)

# CAMBIO SET <-> LISTA 
frutas_lista = list(frutas_set)
print(frutas_lista)
set1 = set(frutas_lista)
print(set1)

# JOIN DE SETS (los une en orden)
s1 = {1,2,3}
s2 = {11,12,13}
s3 = s1.union(s2)
print(s3)

## Usando update
s1.update(s2)
print(s1)

# INTERSECCIÓN DE ELEMENTOS
## Devuelve un set con los elementos comunes en ambos sets
interseccion = s2.intersection(s3)
print(interseccion)

# DIFERENCIA ENTRE SETS
## Devuelve un set con los elementos del primer set menos los del segundo
diferencia = s2.difference(s3)
print(diferencia)

# DIFERENCIA SIMÉTRICA ENTRE SETS
## Devuelve un set con los elementos que no están en los dos sets
diferencia_sim = s3.symmetric_difference(s2)
print(diferencia_sim)

# CONJUNTOS DISJUNTOS
## Si son disjuntos -> no tienen elementos en común
pares = {0,2,4,6,8}
impares = {1,3,5,7,9}
disjuntos = pares.isdisjoint(impares)
print(disjuntos) # True

# SUPER SET y SUBSET
## Para explicar esto podemos pensar en la teoría de conjuntos, los números naturales 
# serían un subset de los números reales, y los reales un super set de los racionales
print(s1.issuperset(s2)) # True
print(s1.issubset(s2)) # False

# VACIAR UN SET
frutas_set.clear()

# BORRAR UN SET
del frutas_set

'''
# EJERCICIOS
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1) Halla la longitud de it_companies
print(len(it_companies))

#2) Añade 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)

#3) Inserta varias compañías a la vez
new_companies = ['Meta', 'Instagram', 'Youtube']
it_companies.update(new_companies)
print(it_companies)

#4) Elimina una de las compañías
it_companies.pop()
print(it_companies)

#5) Diferencia entre remove y discard
#it_companies.remove('WhatsApp') # No lo encuentra y lanza un KeyError
#it_companies.discard('WhatsApp') # No lo encuentra y no lanza excepción

#6) JOIN de A y B
C = A.union(B)
print(C)

#7) Intersección de A y B
intersection = A.intersection(B)
print(intersection)

#8) ¿A subset de B?
AsubsetB = A.issubset(B)
print(AsubsetB) # True

#9) ¿A y B conjuntos disjuntos?
AdisjuntoB = A.isdisjoint(B)
print(AdisjuntoB) # False

#10) Diferencia simétrica entre A y B
sim_diff = B.symmetric_difference(A)
print(sim_diff)

#11) Convierte las edades en un set y compara sus tamaños
## Son diferentes porque el set no admite duplicados y los elimina.
ages_set = set(age)
print('El tamaño de la lista es {} y el del set es {}' .format(len(age), len(ages_set)))