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

# ascii(__obj) returns string representation that you can use to display
# the object in a context where only ASCII characters are allowed.
print(ascii('Buenos días'))

# With the ord(__c) function we can obtain the ASCII representation of a char
print(ord('A'))

# bin(__number) convert given number into decimal to binary base
print(bin(32))

# breakpoint() interrupts the program and an interactive debugger start at that point
byte_array = bytearray([65, 66, 67])
