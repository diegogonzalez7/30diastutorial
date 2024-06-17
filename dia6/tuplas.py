# Una tupla es una colección de diferentes tipos de datos ordenada e inmutable.
# Las tuplas se declaran usando paréntesis (), y una vez sea creada, no se podrá modificar sus valores
# A pesar de que no se puede insertar o borrar elementos, cuenta con métodos que veremos a continuación

# CREACIÓN DE TUPLA VACÍA
tupla_vacia1 = ()
tupla_vacia2 = tuple()

# CREACIÓN DE TUPLA CON VALORES
## Podemos crear una tupla con elementos si le pasamos a tuple() una lista o una tupla ya creada. 
tupla1 = (1,2,3,4,5)
tupla2 = tuple(tupla1)

# LONGITUD DE UNA TUPLA
print(len(tupla1))

# ACCESO ELEMENTOS DE UNA TUPLA
## Tal y como hemos hecho con las listas, usaremos índices positivos y negativos
primer_elemento = tupla1[0]
ultimo_elemento = tupla1[-1]
print(primer_elemento, ultimo_elemento)

# PARTIR TUPLAS
parte1 = tupla1[0:2]
parte2 = tupla1[2:5]
print(parte1, parte2)

# CAMBIO LISTAS <-> TUPLAS
## Como las tuplas son inmutables, si queremos modificar su contenido deberemos convertirlas en listas
tupla1 = list(tupla1)
print('Ahora la tupla es una lista:', tupla1)
tupla1 = tuple(tupla1)
print('Ahora la lista es una tupla:', tupla1)

# COMPROBAR SI UN ELEMENTO ESTÁ EN UNA TUPLA
existe = 1 in tupla1
print(existe) # True

# JOIN DE TUPLAS
## Como hacíamos con listas, usaremos el operador '+'
tupla3 = tupla1 + tupla2
print(tupla3)

# BORRADO DE TUPLAS
## No podemos borrar un solo elemento de una tupla, pero podemos borrarla en su totalidad
del tupla2


# EJERCICIOS

# 1) Crea tuplas con nombres y apellidos de personas
nombres = ('Juan', 'María', 'Mar', 'Sergio')
apellidos = ('Pérez', 'Márquez', 'Rodríguez', 'Castro')
print(nombres)
print(apellidos)

# 2) Une las dos tuplas y asígnalas a una nueva llamada nombre_apellidos
nombre_apellido = nombres + apellidos
print(nombre_apellido)

# 3) ¿Cuántos nombres y apellidos hay?
print('Hay {} nombres y apellidos' .format(len(nombre_apellido)))

# 4) Modifica la tupla añadiendo tu nombre y apellido y asígnala a una nueva tupla
lista_nombres = list(nombre_apellido)
lista_nombres.insert(0, 'Diego')
lista_nombres.insert(-1, 'González')
tupla_nombres = tuple(lista_nombres)
print(tupla_nombres)

# 5) Desempaqueta los nombres y apellidos de la tupla
nombres2 = tupla_nombres[0:len(tupla_nombres)//2]
apellidos2 = tupla_nombres[len(tupla_nombres)//2:len(tupla_nombres)]
print(nombres2, apellidos2)

# 6) Crea tres tuplas distintas, únelas en una nueva y extrae el elemento del medio y di a qué tupla pertenecía originalmente
marcas = ('Nike', 'Adidas', 'Puma')
coches = ('Citroen', 'Renault', 'Ferrari')
comida = ('Fruta', 'Pasta', 'Postres')
mix_tuple = marcas + coches + comida
elemento_medio = mix_tuple[len(mix_tuple)//2]
if elemento_medio in marcas:
    print('El elemento medio {} pertenece a la tupla {}' .format(elemento_medio, marcas))
elif elemento_medio in coches:
    print('El elemento medio {} pertenece a la tupla {}' .format(elemento_medio, coches))
else: 
    print('El elemento medio {} pertenece a la tupla {}' .format(elemento_medio, comida))