# 07. PYTHON INPUT AND DATA CONVERSION

## 07.00 Capturing User Input

### `input()` Function
- The `input()` function is used to capture user input as a string.
- Syntax:
  ```python
  variable = input('Prompt message: ')
  ```
### Example
```python
name = input('What is your name? ')
print(f'Your name is {name}')
# {name=} displays both the variable name and its value
```

## 07.01 Type Conversion in Input
### Why Convert Input Data?
- The `input()` function always returns a string.
- To perform numerical operations, you need to convert the input using functions like `int()` or `float()`.
### Example of Conversion
```python
number_1 = input('Enter a number: ')
number_2 = input('Enter another number: ')

int_number_1 = int(number_1)
int_number_2 = int(number_2)

print(f'The sum of the numbers is: {int_number_1 + int_number_2}')
# Output (if input is 5 and 10):
# The sum of the numbers is: 15
```

## 07.02 Important Notes on Input Handling
1. **Error Handling**:
   - Converting input directly using `int(input())` is not a good practice.
   - If the user enters invalid data (e.g., a letter), the program will throw a `ValueError`.
2. **Recommended Practice**:
   - Capture the input as a string first, then handle conversion and validation separately.
   - Example:
        ```python
        raw_input = input('Enter a number: ')
        if raw_input.isdigit():
            number = int(raw_input)
            print(f'Your number is {number}')
        else:
            print('Invalid input. Please enter a numeric value.')
        ```
1. **String Interpolation**:
   - Use `f-strings` to display input and results more clearly.
   - `{variable=}` in f-strings is a convenient way to show both the variable name and its value (Python 3.8+).
## 07.03 Summary
- Always validate user input to avoid unexpected errors.
- Convert input data only after ensuring it is in the correct format.
- Use `f-strings` for clear and concise output.