# Los strings son un tipo de datos que básicamente es texto escrito.
# Cualquier información escrita entre comillas simples, dobles o triples es un string

saludo = '¡Hola Mundo!'
print(saludo)
print(len(saludo))

# Si usamos comillas triples () podemos hacer strings de más de una línea

#Concatenación de strings

nombre = 'Diego'
apellido = 'González'
espacio = ' '
nombre_completo = nombre + espacio + apellido
print(nombre_completo)


# En Python tenemos caracteres de escape, los más comunes son:

## \n : nueva línea
## \t : tabulador
## \\ : escribe un slash
## \' : nota simple (')
## \" : nota compuesta ('')

print('Línea 1 \n Línea 2')
print('Producto \t Unidades \t Precio')
print('Back slash (\\)')
print('Todos los lenguajes de programación empiezan con un \"¡Hola Mundo!\"')


# Formatos de string (ANTIGUOS)

## %s -> String
## %d -> Integers
## %f -> Float
## %.(nº dígitos)f -> Nº de decimales de los float

#Algunos ejemplos

pi = 3.141592
radio = 4
print('El área del círculo cuyo radio es %s, es de %.3f' %(radio, pi*radio))

librerias = ['Matplotlib','Flask','NumPy','Pandas']
print('Las siguientes son librerías de Python: %s' %(librerias))


# Formatos de string (NUEVOS, versión 3)

# Ahora no hace falta especificar el tipo de datos, simplemente pondremos un {} y luego 
# mediante .format() pondremos las variables a las que queramos referenciar
# Si queremos especificar el nº de decimales deberemos hacer {:.(nº)f}

string = 'Python'
numero = 3
flotante = 3.01
print("""En el lenguaje {} podemos usar un nuevo formateo de Strings.
Este cambio se introdujo en la versión {} (concretamente en la {})""" .format(string, numero, flotante))


# Podemos dividir un String en varias variables, el número de variables debe ser el mismo 
# que el tamaño del String 

lenguaje = 'Python'
a,b,c,d,e,f = lenguaje

# También podemos acceder a posiciones del String mediante índices (empezando desde 0)

print('{}' .format(lenguaje[0]))
print('{}' .format(lenguaje[-1]))

# Podemos también partir los Strings en partes

parte1 = lenguaje[0:3]
parte2 = lenguaje[3:6]
print(parte1)
print(parte2)

# Evitar caracteres cuando partimos Strings
corte = lenguaje[0:6:3] # Paso 3, el resultado sería Ph
print(corte)


# Métodos de String

## capitalize() convierte la primera letra del String a mayúscula
frase = 'hoy me he levantado con ganas de hacer cosas grandes'
print(frase.capitalize())

## count() devuelve el número de veces que aparece un substring
print(frase.count('e'))
print(frase.count('de'))

## endswith() comprueba si el string acaba de una forma concreta
print(frase.endswith('grandes'))

## startswith() comprueba si el string comienza de una forma concreta
print(frase.startswith('Hoy'))

## expandtabs lo que hace es reemplazar el tabulador (\t) con espacios. Podemos especificar los espacios
frase_tabulada = 'Hola\tme\tllamo\tDiego'
print(frase_tabulada)
print(frase_tabulada.expandtabs(12))

## find() devuelve el índice de la primera ocurrencia de una letra, si no se encuentra -> -1
print(frase.find('o'))

## rfind() devuelve el índice de la última ocurrencia de una letra, si no se encuentra -> -1
print(frase.rfind('o'))

## index() devuelve el índice menor de un substring, error si no lo encuentra
## rindex() devuelve el índice mayor de un substring, error si no lo encuentra
print(frase.index('de'))
print(frase.rindex('de'))

## isalnum() comprueba si todos los caracteres son alfanuméricos
frase_nueva = 'EstoEsAlfanumerico'
print(frase_nueva.isalnum())

## isalpha() comprueba que todos los caracteres estén entre a-z
print(frase_nueva.isalpha())
print('123'.isalpha())

## isdigit() comprueba que todos los caracteres sean dígitos
print('12345'.isdigit())

## isidentifier() comprueba si el String es un nombre de variable válido
invalid_identifier = '30diasPython'
print(invalid_identifier.isidentifier())

## replace('<old>','<new>') cambia todas las coincidencias de old con new

print(frase.replace('hoy', 'ayer'))

## format() visto en el dia 3
## islower() comprueba que todos los caracteres estén en minúscula
## isupper() comprueba que todos los caracteres estén en mayúscula
## join() devuelve un string concatenado
## strip('__') devuelve el string sin las letras incluidas 
## title() devuelve el String aplicando Title Case