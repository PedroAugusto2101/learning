# 06. PYTHON FORMATTED STRINGS (F-STRINGS AND .FORMAT)

## 06.00 F-Strings in Python

### What are F-Strings?
- F-strings, introduced in Python 3.6, allow the embedding of expressions inside string literals, using curly braces `{}`.
- They start with the letter `f` or `F` before the opening quotation mark.

### Syntax
```python
variable = "world"
f"Hello, {variable}!"
```

### Example with Calculations and Formatting

```python
name = 'Pedro Augusto'
height = 1.75
weight = 80
bmi = weight / height ** 2

line_1 = f'{name} is {height:.2f} meters tall,'
line_2 = f'weighs {weight} kilograms, and his BMI is'
line_3 = f'{bmi:.2f}'

print(line_1)
print(line_2)
print(line_3)
# Output:
# Pedro Augusto is 1.75 meters tall,
# weighs 80 kilograms, and his BMI is 26.12
```

### Key Features of F-Strings
- Expression evaluation: {2 + 2} results in 4.
- Format specification: Use :.2f to format as a float with 2 decimal places.
---
## 06.01 String Formatting with .format()
### What is `.format()`?
- An older method for formatting strings, which uses placeholders ({}) and the .format() method to insert values.
### Syntax
```python
template = "Hello, {}!"
formatted_string = template.format("world")
print(formatted_string)  # Output: Hello, world!
```
### Example with Named Arguments
```python
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

template = 'b={name2} a={name1} a={name1} c={name3:.2f}'
formatted_string = template.format(
    name1=a, name2=b, name3=c
)

print(formatted_string)
# Output: b=BBBBBB a=AAAAA a=AAAAA c=1.10
```

### Key Features of .format()
- Positional arguments: "{0} {1}".format("Hello", "world").
- Named arguments: "{greeting}, {name}!".format(greeting="Hello", name="world").
- Format specification: {value:.2f} formats the value with 2 decimal places.
---
## 06.02 Comparison: F-Strings vs .format()
| Feature        | F-Strings                     | .format()                              |
| -------------- | ----------------------------- | -------------------------------------- |
| Syntax         | `f"{variable}"`               | `"{}".format(variable)`                |
| Readability    | Easier and more concise       | Verbose                                |
| Performance    | Faster (evaluated at runtime) | Slightly slower (method call overhead) |
| Python Version | 3.6+                          | 2.7+                                   |
### Summary
- Prefer f-strings for readability and simplicity in Python 3.6+.
- Use `.format()` for compatibility with older Python versions.

