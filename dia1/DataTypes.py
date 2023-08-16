integer = 1
floating = 1.3
String = 'Diego'
Countries_List = ['Spain', 'Denmark', 'Germany', 'France', "UK"]
Student_dict = {
    'name': 'Diego',
    'last_name': 'Gonzalez',
    'age': 18,
    'direction': 'Pontevedra'
}
Planets_tuple = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus')
numbers_set = {2.81, 3.14, 9.81}

"""
print(type(integer))
print(type(floating))
print(type(String))
print(type(Countries_List))
print(type(Student_dict))
print(type(Planets_tuple))
print(type(numbers_set))
"""

"""
n = 0
while n < len(Planets_tuple):
    print(Planets_tuple[n])
    n = n + 1
"""

"""
while len(Countries_List) != 0:
    print(*Countries_List)
    Countries_List.pop(0) # Si ponemos 0 se elimina el primer elemento, si no ponemos nada se elimina el último elemento
"""

"""
if Student_dict['age'] >= 18:
    print('The student is adult')
"""

# Mediante la función pop, podemos usar una lista como una pila

print(type(10))     # <class 'int'>
print(type(9.8))    # <class 'float'>
print(type(3.14))   # <class 'float'>
print(type(4-4j))   # <class 'complex'>
print(type(['Asabeneh', 'Python', 'Finland']))  # <class 'list'>
print(type('Diego'))    # <class 'str'>
print(type(('Diego', 'Luis', 'Bea', 'Luz')))    # <class 'tuple'>
print(type({'name': 'Diego', 'Country': 'Spain'}))  # <class 'dict'>