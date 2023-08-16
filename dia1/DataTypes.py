#import math

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
            With the len(object) function we obtain the exact length (total objects) of:
                A tuple
                A set
                The number of categories of a dictionary
                A list

n = 0
while n < len(Planets_tuple):
    print(Planets_tuple[n])
    n = n + 1
"""

"""
                                            pop(list) function 

                    # If we put * before the list name, it prints the whole list
                    # Instead, if we don't put it, it prints the list with the [] and ''

while len(Countries_List) != 0:
    print(*Countries_List) 
    Countries_List.pop(0)
    # If we put 0 the first element is eliminated, if we do not put anything the last element is eliminated
"""

"""
if Student_dict['age'] >= 18:
    print('The student is adult')
"""

"""
# Using the function type, we can obtain the class of a variable, list, tuple or dictionary  

print(type(integer))
print(type(floating))
print(type(String))
print(type(Countries_List))
print(type(Student_dict))
print(type(Planets_tuple))
print(type(numbers_set))

print(type(10))     # <class 'int'>
print(type(9.8))    # <class 'float'>
print(type(3.14))   # <class 'float'>
print(type(4-4j))   # <class 'complex'>
print(type(['Madrid', 'Python', 'Finland']))  # <class 'list'>
print(type('Diego'))    # <class 'str'>
print(type(('Diego', 'Jose', 'Maria', 'Cristian')))    # <class 'tuple'>
print(type({'name': 'Diego', 'Country': 'Spain'}))  # <class 'dict'>
"""

"""
                                Euclidian distance
In math, the euclidian distance is the distance between two points in a euclidian 
space using the Pythagorean theorem
                                    ___________________________
                    dE (P1, P2) = \/ (x2 - x1)^2 + (y2 - y1)^2

P1 = (2, 3)
P2 = (10, 8)

distance = math.sqrt(((P2[0] - P1[0]) ** 2) + ((P2[1] - P1[1]) ** 2))
print('The distance between', P1, 'and', P2, 'is', distance)

"""
