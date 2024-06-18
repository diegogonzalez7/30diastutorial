# Los IF son formas de controlar el flujo de un programa mediante el establecimiento de condiciones

# IF
## Si se cumple la condición del if, se ejecuta el código de dentro
num = -5
if num > 0:
    print('{} es un número positivo' .format(num))

# IF ELSE
## Si la condición del if no se cumple, se ejecuta el código del else

num = -3
if num > 0:
    print('{} es un número positivo' .format(num))
else:
    print('{} es un número negativo o 0' .format(num))

# IF ELIF ELSE
## Permite que se verifique más de una condición antes de ejecutar el código del else

num = 0
if num > 0:
    print('{} es un número positivo' .format(num))
elif num == 0:
    print('El número ({}) es 0' .format(num))
else:
    print('{} es un número negativo o 0' .format(num))

# CONDICIONES ANIDADAS
## Podemos anidar condiciones situándolas dentro del bloque de código que se ejecuta si se cumple la condición
num = 7
if num > 0:
    if num <= 10:
        if num % 2 != 0:
            print('El número ({}) es un número impar mayor que 0 y menor que 10' .format(num))
        else:
            print('El número ({}) es un número par mayor que 0 y menor o igual que 10' .format(num))
    else:
        print('El número ({}) es un número mayor 10' .format(num))
else:
    print('El número ({}) es un número menor o igual que 0' .format(num)) 

# OPERADORES LÓGICOS EN CONDICIONES
## Si queremos verificar varias condiciones juntas, podemos usar operadores lógicos como and y or
if num > 0 and num % 2 != 0:
    print('El número ({}) es impar y mayor que 0' .format(num))

num = -7
if num > 0 or num % 2 != 0:
    print('El número ({}) es impar o mayor que 0' .format(num))


# EJERCICIOS
import time


#1) Haz un programa para que el usuario introduzca su edad por pantalla y comprueba si es 
# mayor de edad. En caso de que no lo sea, di cuantos años le faltan para serlo
edad = int(input('Introduzca su edad: '))
if edad >= 18:
    print('Usted es mayor de edad, ya que tiene {} años' .format(edad))
else:
    print('Usted no es mayor de edad, ya que tiene {} años, le faltan {} años para serlo' .format(edad, 18-edad))

    
#2) Compara dos valores de edad introducidos por el usuario
mi_edad = int(input('Introduce tu edad: '))
su_edad = int(input('Introduce la edad de tu compañero: '))
if mi_edad > su_edad:
    print('Eres {} mayor que tu compañero' .format(mi_edad-su_edad))
elif mi_edad < su_edad:
    print('Tu compañero es {} años mayor que tú' .format(su_edad-mi_edad))
else: 
    print('Teneis la misma edad los dos')

    
#3) Haz un programa que diga si la nota de un usuario es:
# Sobresaliente (9 - 10), Notable (7 - 8.9), Bien (6 - 6.9), Suficiente (5 - 5.9) o Suspenso (0 - 4.9)
nota = float(input('Introduce tu nota: '))
if nota >= 0 and nota <= 10:
    if nota <= 4.9:
        print('Tu nota ({}) es un Suspenso' .format(nota))
    elif nota >= 5 and nota < 6:
        print('Tu nota ({}) es un Suficiente' .format(nota))        
    elif nota >= 6 and nota < 7:
        print('Tu nota ({}) es un Bien' .format(nota))
    elif nota >= 7 and nota < 9:
        print('Tu nota ({}) es un Notable' .format(nota))
    else: 
        print('Tu nota ({}) es un Sobresaliente' .format(nota))
else: 
    print('La nota introducida ({}) no es válida' .format(nota)) 

    
#4) Haz un programa que diga la estación en la que se encuentra el mes introducido
mes = input('Introduce el mes: ')
primavera = ['marzo','abril','mayo','Marzo','Abril','Mayo']
verano = ['junio','julio','agosto','Junio','Julio','Agosto']
otoño = ['septiembre','octubre','noviembre','Septiembre','Octubre','Noviembre']
invierno = ['diciembre','enero','febrero','Diciembre','Enero','Febrero']
if mes in primavera:
    print('El mes que has introducido ({}) pertenece a Primavera' .format(mes))
elif mes in verano:
    print('El mes que has introducido ({}) pertenece a Verano' .format(mes))
elif mes in otoño:
    print('El mes que has introducido ({}) pertenece a Otoño' .format(mes))
elif mes in invierno:
    print('El mes que has introducido ({}) pertenece a Invierno' .format(mes))
else:
    print('El mes introducido no existe, prueba a escribirlo bien o a desactivar las mayúsculas')

    
#5) Haz un programa que compruebe si una fruta introducida está en la lista, 
# si no está, añádela e imprime la lista. Si ya está no hagas nada
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input('Introduce el nombre de una fruta: ')
if fruta not in frutas:
    print('{} no se encuentra en la lista de frutas. Añadiendo...' .format(fruta))
    time.sleep(2)
    frutas.append(fruta)
    print('Esta es la nueva lista de frutas', frutas)
else: 
    print('La fruta introducida ya está en la lista')


#6) Teniendo el siguiente diccionario, resuelve las preguntas:
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

# Comprueba si la persona tiene skills, si las tiene imprime la de la mitad de la lista
if 'skills' in persona:
    print('{} es la skill de la mitad de la lista' .format(persona['skills'][len(persona['skills'])//2]))
else:
    print('La persona no tiene skills')

# Comprueba si la persona tiene skills, si las tiene comprueba si Python es una de ellas
if 'skills' in persona:
    if 'Python' in persona['skills']:
        print('Python se encuentra entre las skills')
    else:
        print('Python no se encuentra entre las skills')
else:
    print('La persona no tiene skills')

# Di si la persona es:
# Si las skills de una persona son JavaScript y React -> desarrollador frontend
# Si las skills de una persona son Node, Python y MongoDB -> desarrollador backend
# Si las skills de una persona son React, Node y MongoDB -> desarrollador fullstack
frontend = {'JavaScript', 'React'}
backend = {'Node', 'Python', 'MongoDB'}
fullstack = {'React', 'Node', 'MongoDB'}

if 'skills' in persona:
    skills_set = set(persona['skills'])
    if frontend.issubset(skills_set):
        print('La persona es un desarrollador frontend')
    elif backend.issubset(skills_set):
        print('La persona es un desarrollador backend')
    elif fullstack.issubset(skills_set):
        print('La persona es un desarrollador full stack')
    else:
        print('La persona no está en estas tres categorías')
else:
    print('La persona no tiene skills')

# Pon si la persona está estudiando y en qué país
if persona['estudiando']:
    print('El alumno {} {} está estudiando en {}' .format(persona['nombre'], persona['apellido'], persona['pais']))
else:
    print('El alumno {} {} no está estudiando' .format(persona['nombre'], persona['apellido']))