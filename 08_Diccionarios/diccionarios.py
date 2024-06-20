# Los diccionarios son una colección desordenada y modificable que usa pares clave-valor

# CREACIÓN DE UN DICCIONARIO
## Usaremos {} como con los sets, pero esta vez dentro los declararemos de forma distinta
persona = {
    'nombre':'Juan', 
    'apellido':'Hernández', 
    'edad': 32,
    'casado': True,
    'skills':['Python', 'C', 'JavaScript'],
    'direccion':{
        'calle':'Calle Real 21',
        'codigo_postal':32981
    }
    }

# LONGITUD DE UN DICCIONARIO (número de keys)
print(len(persona))

# ACCESO A ELEMENTOS DE UN DICCIONARIO (referenciando la key)
## Si tratamos de acceder a un elemento que no existe, devolverá error. Para evitarlo usaremos get()
print(persona.get('nombre'))
print(persona.get('skills')[2])
# print(persona['trabajo']) Devolerá error
print(persona.get('trabajo')) # Devolverá None

# AÑADIR ELEMENTOS A UN DICCIONARIO
persona['trabajo'] = 'programador'
print(persona)

# MODIFICAR ELEMENTOS EN UN DICCIONARIO
persona['nombre'] = 'Pedro'
print(persona)

# COMPROBAR KEYS EN UN DICCIONARIO
print('salario' in persona)
print('casado' in persona)

# ELIMINAR PARES DE CLAVES DE UN DICCIONARIO
## pop(key) elimina la clave especificada
persona.pop('casado')
## popitem() elimina el último elemento
persona.popitem()
## del elimina un elemento con un nombre específico
del persona['direccion']
print(persona)

# CAMBIO DICCIONARIO <-> LISTA DE TUPLAS
print(persona.items())

# COPIAR UN DICCIONARIO
copy_dict = persona.copy()
print(copy_dict)

# OBTENER LAS KEYS COMO LISTA
keys = copy_dict.keys()
print(keys)

# OBTENER LAS CLAVES COMO LISTA
values = copy_dict.values()
print(values)

# VACIAR UN DICCIONARIO
persona.clear()

# ELIMINAR UN DICCIONARIO
del persona


# EJERCICIOS

#1) Crea un diccionario vacío llamado dog
dog = {}
print(dog)
#2) Añade nombre, color, raza y edad al diccionario
dog['nombre'] = 'Vovi'
dog['color'] = 'negro'
dog['raza'] = 'American Stanford'
dog['edad'] = '12'
print(dog)

#3) Obtén la longitud del diccionario
print(len(dog))

#4) Recupera la definicion de persona de antes y obtén el valor de skills, comprueba su tipo
persona = {
    'nombre':'Juan', 
    'apellido':'Hernández', 
    'edad': 32,
    'casado': True,
    'skills':['Python', 'C', 'JavaScript'],
    'direccion':{
        'calle':'Calle Real 21',
        'codigo_postal':32981
    }
    }

skills = []
skills = persona.get('skills')
print(type(skills))

#5) Añade varias skills nuevas
sk = ['Django', 'Pandas']
n_skills = skills + sk
persona['skills'] = n_skills
print(persona)

#6) Obtén las claves del diccionario
persona_values = persona.values()
print(persona_values)

#7) Obtén las keys del diccionario
persona_keys = persona.keys()
print(persona_keys)

#8) Pasa el diccionario a una lista de tuplas
print(persona.items())

#9) Borra uno de los items del diccionario
persona.popitem()
print(persona)

#10) Borra el diccionario
del persona