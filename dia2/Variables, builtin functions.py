"""
In Python, we have many built-in functions (view image).
The built-in features are globally available for use, which means you can use
the built-in features without importing or configuring them.

With the following line of code we can obtain the complete list of Python reserved words
which we cannot use as names for the variables we create.
help('keywords')
"""

# abs(__x) function returns the absolute value of a number
print(abs(-20))

# all(iterable) and any(iterable) take an iterable and determine if all arguments are true
# or if there is at least one true respectively.
booleans = [True, False, True]
if all(booleans):
    print('Tautology')
else:
    print('Contradiction')

if any(booleans):
    print('There are some true statement there')

# ascii(__obj) calculate the ascii number associated to the obj given
print(ord('A'))