"""
Docstring
Python = Programming language
Typing type = Dynamic / Strong
str -> string -> text
Strings are texts enclosed in quotes
"""
print(1234)

# Simple quotes
print('Pedro Augusto')
print(1, 'Pedro "Augusto"')

# Double quotes
print("Pedro Augusto")
print(2, "Pedro 'Augusto'")

# Escape
print("Pedro \"Augusto\"")

# r -> raw
print(r"Pedro \"Augusto\"")

# int and float types

# int -> Integer
# The int type represents any positive or negative number.
# Unsigned int is considered positive.
# print(11) # int
# print(-11) # int
# print(0)

# float -> Floating-point number
# The float type represents any positive or negative number with a decimal point.
# Unsigned float is considered positive.
# print(1.1, 10.11)
# print(0.0, -1.5)

# The type function shows the type that Python
# inferred for the value.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

# bool (boolean) data type

# When asking a question in a program,
# there are only two possible answers:
# yes (True) or no (False).
# There are several operators to "ask questions".
# Among them is ==, a logical operator that
# asks if one value is equal to another.
print(10 == 10)  # Yes => True
print(10 == 11)  # No  => False
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# Type conversion, typecasting, coercion
# The act of converting one type into another
# Immutable and primitive types:
# str, int, float, bool - immutables
# Tipagem fraca significa que a linguagem converte
# um dos valores pra executar corretamente
# Já a tipagem forte, resulta em um erro, pois
# não converte
# Tipagem dinâmica não exige a declaração do tipo do dado
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
