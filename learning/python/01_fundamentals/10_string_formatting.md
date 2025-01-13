# 10. PYTHON STRING INTERPOLATION, FORMATTING, AND SLICING

## 10.00 String Interpolation

### Basic String Interpolation
- The `%` operator can be used to format strings.
- Common format specifiers:
  - `%s`: String
  - `%d` or `%i`: Integer
  - `%f`: Float
  - `%x` or `%X`: Hexadecimal

```python
nome = 'Pedro'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)  # Pedro, o preço é R$1000.96

print('O hexadecimal de %d é %08X' % (1500, 1500))  # O hexadecimal de 1500 é 000005DC
```

## 10.01 String Formatting

### Basic String Formatting
- More control over the formatting of the output:
  - `%s`: String
  - `%d`: Integer
  - `%f`: Float
  - `x` or `X`: Hexadecimal
  - `.<number of digits>f`: Floating-point precision
  
- Formatting flags:
  - `>`: Left alignment
  - `<`: Right alignment
  - `^`: Center alignment
  - `=`: Forces the number to appear before zeros
  - Sign: `+` or `-`
  - Conversion flags: `!r`, `!s`, `!a` (repr, str, ascii)

```python
variavel = 'ABC'
print(f'{variavel}')  # ABC
print(f'{variavel: >10}')  # '       ABC'
print(f'{variavel: <10}.')  # 'ABC       .'
print(f'{variavel: ^10}.')  # '   ABC     .'
print(f'{1000.4873648123746:0=+10,.1f}')  # +1,000.5
print(f'O hexadecimal de 1500 é {1500:08X}')  # O hexadecimal de 1500 é 000005DC
print(f'{variavel!r}')  # 'ABC'
```

## 10.02 String Slicing

### String Slicing
- Strings can be sliced using the syntax `[start:end:step]`.
- Example:
  - `s[0:5]` returns the first five characters.
  - `s[::-1]` returns the string reversed.

```python
variavel = 'Olá mundo'
print(variavel[::-1])  # odnum alO
```

### Key Points
- **Interpolation** is done using the `%` operator, which is useful for basic formatting.
- **String Formatting** using `f-strings` gives more control over the output with alignment, padding, and more complex conversions.
- **Slicing** allows for extracting parts of strings using indexes and steps. 
- **len** the `len` function return the quantity of caracters in the object. 
