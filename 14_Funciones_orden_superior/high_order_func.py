# En Python podemos llevar a cabo varias operaciones con funciones:
## Una función puede ser modificada
## Una función puede ser asignada a una variable
## Una función puede ser devuelta como el resultado de otra función
## Una función puede recibir una o más funciones como parámetros


# FUNCIONES COMO PARÁMETROS

def suma (numeros):
    return sum(numeros)

def suma_func_param(funcion, lista):
    suma = funcion(lista)
    return suma

resultado = suma_func_param(suma, [1,2,3,4,5])
print(resultado)

# FUNCIÓN COMO VALOR DEVUELTO
## Le pasamos el tipo a la función de orden superior y devuelve uno de las funciones en base al valor
## La función devuelve una referencia a una función en lugar de ejecutarla, de esta forma se guarda 
## la referencia y luego podemos llamar a esa variable como si fuera la función original

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def v_absoluto (x):
    if x < 0:
        return x - (x*2)
    else:
        return x
    
def higher_order_function(tipo):
    if tipo == 'cuadrado':
        return cuadrado
    elif tipo == 'cubo':
        return cubo
    elif tipo == 'v_absoluto':
        return v_absoluto
    
resultado = higher_order_function('cuadrado')
print(resultado(9)) #81
resultado = higher_order_function('cubo')
print(resultado(9)) #729
resultado = higher_order_function('v_absoluto')
print(resultado(-2001)) #2001

# CIERRES EN PYTHON
## Python permite que una función anidada acceda al ámbito exterior de la función que la contiene (Cierre o Closure)
## Podemos crearlos anidando una función dentro de otra encapsuladora y luego devolviendo la función interna

def suma10():
    diez = 10
    def sumar(n):
        return n + diez
    return sumar

resultado_cierre = suma10()
## Cuando llamamos a suma10, la referencia a la función sumar se almacena en resultado_cierre, 
## y cuando le pasamos luego un parámetro, lleva a cabo la función sumar
print(resultado_cierre(5)) #15


# DECORADORES EN PYTHON
def saludo():
    return 'Bienvenido a Python'
def decorador_mayusculas(funcion):
    def wrapper():
        func = funcion()
        mayusculas = func.upper()
        return mayusculas
    return wrapper

g = decorador_mayusculas(saludo)
print(g())

# Implementaremos el ejemplo de arriba con decoradores
@decorador_mayusculas
def saludo2():
    return 'Bienvenido a Python otra vez'
print(saludo2())

# Podemos aplicar varios decoradores a una función
def split_string_decorator(funcion):
    def wrapper():
        func = funcion()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@decorador_mayusculas
def saludo3():
    return 'Hola Python'
print(saludo3())

# ACEPTAR PARÁMETROS EN FUNCIONES DECORADORAS
def decorador_con_parametros(funcion):
    def wrapper_aceptar_parametros(param1, param2, param3):
        funcion(param1, param2, param3)
        print("Vivo en {}" .format(param3))
    return wrapper_aceptar_parametros

@decorador_con_parametros
def print_full_name(nombre, apellido, pais):
    print("Soy {} {}. " .format(nombre, apellido, pais))

print_full_name("Diego", "Gonzalez", "España")


# FUNCIONES DE ORDEN SUPERIOR INTEGRADAS 
## map(function, iterable)  -   recibe una función y un iterable como parámetros
numeros = [1, 2, 3, 4, 5]

numeros_al_cuadrado = map(cuadrado, numeros)
print(list(numeros_al_cuadrado))

numeros_al_cuadrado = map(lambda x : x ** 2, numeros)
print(list(numeros_al_cuadrado))

## filter(function, iterable)   -   filtra los elementos atendiendo a un determinado criterio
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
numeros_pares = filter(par, numeros)
print(list(numeros_pares))


## reduce(function, iterable)   -   definida en el módulo functools. Devuelve un solo valor
from functools import reduce
def suma_2_nums(a, b):
    return int(a) + int(b)

suma = reduce(suma_2_nums, numeros)
print(suma)


# EJERCICIOS
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1) Usa las funciones map, filter y reduce
# map
def cubo(x):
    return x ** 3
numeros_al_cubo = map(cubo, numbers)
print(list(numeros_al_cubo))

nordic_countries_list = ['Denmark', 'Sweden', 'Norway', 'Finland', 'Iceland', 'Faroe Islands', 'Aland', 'Greenland']

# filter
def nordic_countries(country):
    if country in nordic_countries_list:
        return True
    else:
        return False
    
nordics = filter(nordic_countries, countries)
print(list(nordics))

#reduce
def mayor(a,b):
    if a > b:
        return a
    else:
        return b
num_mayor = reduce(mayor, numbers)
print(num_mayor)

# 2) Usa map para crear una nueva lista que ponga los países en mayúscula

def uppercase_countries(country):
    return country.upper()

paises_mayus = map(uppercase_countries, countries)
print(list(paises_mayus))


# 3) Usa map para crear una nueva lista con los cuadrados de todos los numeros
def cuadrado (n):
    return n ** 2

nums_cuadrado = map(cuadrado, numbers)
print(list(nums_cuadrado))


# 4) Usa filter para filtrar todos los países que tengan 'land' en su nombre
def land_filter(country):
    if 'land' in country:
        return True
    else:
        return False
    
land_countries = filter(land_filter, countries)
print(list(land_countries))


# 5) Usa filter para filtrar los países con 6 letras exactamente
def six_letters_countries(country):
    if len(country) == 6:
        return True
    else:
        return False

six_letters = filter(six_letters_countries, countries)
print(list(six_letters))

# 6) Usa filter para filtrar los países con 6 letras o más
def six_or_more_letters_countries(country):
    if len(country) >= 6:
        return True
    else:
        return False

six_or_more_letters = filter(six_or_more_letters_countries, countries)
print(list(six_or_more_letters))


# 7) Usa filter para filtrar por los países que empiecen por la letra 'E'
def starting_E_country(country):
    if country[0] == 'E':
        return True
    else:
        return False
    
paises_por_e = filter(starting_E_country, countries)
print(list(paises_por_e))


# 8) Crea una función que reciba una lista y devuelva una lista conteniendo solo elementos string
def convert_to_string (a):
    if type(a) != 'String':
        return str(a)
    else:
        return a

numeros_string = map(convert_to_string, numbers)
print(list(numeros_string))

# 9) Usa reduce para concatenar todos los países y muestra un mensaje final
def concat (country1, country2):
    return country1 + ', ' + country2

paises_concatenados = reduce(concat, countries) + ' son países del Norte de Europa'
print(paises_concatenados)


# 10) Haz una función que devuelva un diccionario cuya clave sea la inicial del país, 
# y el valor sea el número de países que empiezan por dicha letra

def contar_paises_por_letra(paises):
    conteo = {}
    for pais in paises:
        letra_inicial = pais[0].upper()
        if letra_inicial in conteo:
            conteo[letra_inicial] += 1
        else:
            conteo[letra_inicial] = 1
    return conteo

paises = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland",
    "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

conteo = contar_paises_por_letra(paises)
print(conteo)