# 03. PYTHON DATA TYPES

## 03.00 Introduction to Data Types

### Common Data Types
1. **`str` (String)**: Represents text, enclosed in quotes (single `'` or double `"`).  
   - Strings are immutable.
   - Example: `'Pedro Augusto'`, `"Pedro 'Augusto'"`

2. **`int` (Integer)**: Represents whole numbers (positive, negative, or zero).  
   - Example: `11`, `-11`, `0`

3. **`float` (Floating-point)**: Represents numbers with a decimal point.  
   - Example: `1.1`, `-1.5`, `0.0`

4. **`bool` (Boolean)**: Represents logical values (`True` or `False`).  
   - Commonly used in comparisons or logical operations.

### Examples of Data Types
```python
# Strings
print('Pedro Augusto')          # Single quotes
print("Pedro 'Augusto'")        # Double quotes
print("Pedro \"Augusto\"")      # Escape character
print(r"Pedro \"Augusto\"")     # Raw string

# Integers and Floats
print(11)                       # int
print(-11)                      # int
print(1.1, 10.11)               # float
print(type(11), type(1.1))      # Display the inferred type

# Boolean
print(10 == 10)                 # True
print(10 == 11)                 # False
print(type(True), type(False))  # Types of boolean values
```

## 03.01 Type Conversion and Inference
### What is Type Conversion?
- Type conversion (or typecasting) is the act of converting one type into another.
- Common immutable types in Python: str, int, float, bool.
### Python Typing
- **Strong Typing**: Type mismatches result in errors (e.g., int + str causes a TypeError).
- **Dynamic Typing**: Types are determined at runtime, no need to declare types explicitly.

### Examples of Type Conversion

```python
print(int('1'), type(int('1')))        # Convert str to int
print(type(float('1') + 1))            # Convert str to float, add to int
print(bool(' '))                       # Convert non-empty string to bool
print(str(11) + 'b')                   # Convert int to str and concatenate
```