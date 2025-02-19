# 02. PYTHON PRINT FUNCTION

## 02.00 Using the `print()` function

### What is the `print()` function?
- The `print()` function is used to display output to the console.
- It accepts a series of arguments, both **non-named** (positional) and **named** (keyword).

### Parameters of `print()`
1. **`sep`**: Defines the string that separates the non-named arguments.  
   - Default is a single space (`' '`).
   - Example: `print(1, 2, 3, sep='-')` outputs `1-2-3`.

2. **`end`**: Specifies the string that will be printed at the end of the output.  
   - Default is a newline (`'\n'`).
   - Example: `print("Hello", end="!")` outputs `Hello!` instead of moving to the next line.

3. **Non-named arguments**: These are the values you want to print.  
   - Example: `print(1, 2, 3)` outputs `1 2 3`.

### Example Code:
```python
## \r\n -> CRLF (used in Windows)
# \n -> LF (used in Linux and macOS)
print(12, 34, 1011, sep='-', end='\n##')  # Output: 12-34-1011##
print(56, 78, sep='-', end='\n')          # Output: 56-78
print(9, 10, sep='-', end='\n')           # Output: 9-10
```