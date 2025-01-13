# 05. PYTHON ARITHMETIC OPERATORS

## 05.00 Arithmetic Operations in Python

### Basic Arithmetic Operators
Python supports several arithmetic operations:  

| Operator | Description         | Example   | Result      |
| -------- | ------------------- | --------- | ----------- |
| `+`      | Addition            | `10 + 10` | `20`        |
| `-`      | Subtraction         | `10 - 5`  | `5`         |
| `*`      | Multiplication      | `10 * 10` | `100`       |
| `/`      | Division (float)    | `10 / 3`  | `3.3333...` |
| `//`     | Floor division      | `10 // 3` | `3`         |
| `**`     | Exponentiation      | `2 ** 10` | `1024`      |
| `%`      | Modulus (remainder) | `55 % 2`  | `1`         |

### Examples of Arithmetic Operations
```python
addition = 10 + 10
print('Addition:', addition)

subtraction = 10 - 5
print('Subtraction:', subtraction)

multiplication = 10 * 10
print('Multiplication:', multiplication)

division = 10 / 3  # Result is a float
print('Division:', division)

floor_division = 10 // 3
print('Floor Division:', floor_division)

exponentiation = 2 ** 10
print('Exponentiation:', exponentiation)

modulus = 55 % 2  # Remainder of the division
print('Modulus:', modulus)
```

## 05.01 Special Arithmetic Operations
### Concatenation
- Strings can be concatenated using the + operator.
- Example:
```python
concatenation = 'Pedro' + ' ' + 'Augusto'
print(concatenation)  # Output: Pedro Augusto
```

### Repetition
- Strings can be repeated using the * operator.
- Example:
```python
repeat_a = 'A' * 10
repeat_name = 3 * 'Pedro'
print(repeat_a)  # Output: AAAAAAAAAA
print(repeat_name)  # Output: PedroPedroPedro
```

## 05.02 Operator Precedence
### Rules of Precedence
The order in which operations are evaluated:

1. Parentheses (n + n)
2. Exponentiation **
3. Multiplication, Division, Floor Division, Modulus * / // %
4. Addition and Subtraction + -
### Example of Precedence
```python
# Following operator precedence
result = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(result)  # Output: 1024
```
### Summary Table of Operator Precedence
| Precedence | Operators           | Example       | Result |
| ---------- | ------------------- | ------------- | ------ |
| 1          | Parentheses         | `(2 + 3) * 4` | `20`   |
| 2          | Exponentiation      | `2 ** 3`      | `8`    |
| 3          | `*`, `/`, `//`, `%` | `10 / 2 + 1`  | `6.0`  |
| 4          | `+`, `-`            | `5 + 2 - 3`   | `4`    |