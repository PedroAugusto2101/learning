# 09. PYTHON LOGICAL OPERATORS AND `IN`/`NOT IN`

## 09.00 Logical Operators

### What Are Logical Operators?
- Logical operators are used to combine conditional statements.
- Common operators:
  - `and` (logical AND): All conditions must be `True`.
  - `or` (logical OR): At least one condition must be `True`.
  - `not` (logical NOT): Reverses the boolean value.

---

### `and` Operator
- All conditions need to evaluate to `True` for the expression to be `True`.
- If any condition is `False`, the entire expression evaluates to `False`.
- Example:
  ```python
  # Falsy values: 0, 0.0, '', False, None
  entrada = input('[E]nter [S]exit: ')
  senha_digitada = input('Password: ')

  senha_permitida = '123456'

  if entrada == 'E' and senha_digitada == senha_permitida:
      print('Access granted')
  else:
      print('Access denied')

  # Short-circuit evaluation
  print(True and False and True)  # False
  print(True and 0 and True)  # 0
  ```
---
### `or` Operator
- The expression is `True` if at least one condition is `True`.
- If any value is `True`, the expression stops evaluating (short-circuit evaluation).
- Example:
```python
entrada = input('[E]nter [S]exit: ')
senha_digitada = input('Password: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Access granted')
else:
    print('Access denied')

# Short-circuit evaluation
senha = input('Password: ') or 'No password'
print(senha)
```
---
### `not` Operator
- Used to reverse the boolean value of an expression.
- Example:
```python
print(not True)  # False
print(not False)  # True
```
---
## 09.01 `in` and `not in` Operators
### What Are `in` and `not in`?
- Used to check for the presence (or absence) of a substring in a string.
- Strings are iterable, meaning each character has an index.
### Examples:
```python
# String indexes
#  0  1  2  3  4  5
#  O  t  á  v  i  o
# -6 -5 -4 -3 -2 -1

name = 'Pedro'
print(name[2])  # 'd'
print(name[-3])  # 'á'

print('dro' in nome)  # True
print('zero' in nome)  # False
print('dro' not in nome)  # False
print('zero' not in nome)  # True

# User input example
name = input('Enter your name: ')
find = input('Enter what you want to find: ')

if find in name:
    print(f'{find} is in {name}')
else:
    print(f'{find} is not in {name}')
```
---
## 09.02 Key Points
- `and` requires all conditions to be `True`, while `or` requires at least one.
- Use `not` to invert the truth value of expressions.
- The `in` and `not in` operators are useful for checking membership in strings or other iterable objects.

