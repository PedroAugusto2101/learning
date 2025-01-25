# 11. TRY/EXCEPT IN PYTHON

## 11.00 Introduction to Try/Except

### What Is Try/Except?
- **try**: Used to attempt running a block of code.
- **except**: Catches errors that occur during the execution of the try block.

---

## 09.01 Using Try/Except to Handle Errors

### Example of Try/Except Block
- If an error occurs within the `try` block, the program moves to the `except` block to handle the error.
  
  ```python
  numero_str = input('I will double the number you enter: ')

  try:
      numero_float = float(numero_str)
      print('FLOAT:', numero_float)
      print(f'The double of {numero_str} is {numero_float * 2:.2f}')
  except:
      print('That is not a number')
  ```

- In this example:
  - The user input is attempted to be converted into a float.
  - If successful, the doubled value is printed.
  - If an error occurs (such as entering a non-numeric value), the error is caught and a message is printed.
---
## 09.02 Using isdigit() for Basic Error Handling
- An alternative way to check if a string is a number is to use the isdigit() method.

- Example:

```python
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'The double of {numero_str} is {numero_float * 2:.2f}')
else:
    print('That is not a number')
```
- This method ensures the input is numeric before attempting conversion, providing an additional check before using `try/except`.
- But it doesn't work with `float` numbers, only `int`.
---
## 09.03 Key Points
- The `try/except` block is used to handle errors gracefully and prevent the program from crashing.
- `try` executes the code, while `except` handles any exceptions that may occur.
- Using methods like `isdigit()` can help preempt errors before using `try/except`.