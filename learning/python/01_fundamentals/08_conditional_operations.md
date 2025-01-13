# 08. PYTHON CODE BLOCKS AND CONDITIONALS

## 08.00 Code Blocks in Python

### What Are Code Blocks?
- A code block is a group of statements executed together.
- Python uses **indentation** (spaces or tabs) to define code blocks.

---

## 08.01 Conditional Statements

### `if` Statement
- Used to execute a block of code if a condition is `True`.
- Syntax:
  ```python
  if condition:
      # code block
    ```
### `elif` Statement
- Stands for "else if." It checks additional conditions if the previous ones are `False`.
- Syntax:
    ```python
    elif another_condition:
        # code block
    ```
### `else` Statement
- Executes a block of code if all previous conditions are False.
- Syntax:
    ```python
    else:
        # code block
    ```
### Example
```python
entry = input('Do you want to "enter" or "exit"? ')

if entry == 'enter':
    print('You entered the system.')
    print('Additional code inside the block.')
elif entry == 'exit':
    print('You exited the system.')
else:
    print('Invalid input: neither "enter" nor "exit".')

print('OUTSIDE THE BLOCKS')
```
---
## 08.02 Nested Conditions
- `if` statements can be nested to check multiple conditions.
- Example:
    ```python
    if condition1:
        if condition2:
            print('Both conditions are True')
    ```
---
## 08.03 Debugging with VS Code
- Use breakpoints to pause program execution and inspect variable values.
- Example:
```python
condition1 = True
condition2 = False

if condition1:
    print('Code for condition1')
elif condition2:
    print('Code for condition2')
else:
    print('No conditions were met.')
```
---
## 08.04 Comparison Operators
### What Are Comparison Operators?
- Operators used to compare values. They return a boolean (`True` or `False`).

| Operator | Meaning               | Example (`True`) |
| -------- | --------------------- | ---------------- |
| `>`      | Greater than          | `2 > 1`          |
| `>=`     | Greater than or equal | `2 >= 2`         |
| `<`      | Less than             | `1 < 2`          |
| `<=`     | Less than or equal    | `2 <= 2`         |
| `==`     | Equal to              | `'a' == 'a'`     |
| `!=`     | Not equal to          | `'a' != 'b'`     |
### Example
```python
greater = 2 > 1
greater_or_equal = 2 >= 2
less = 1 < 2
less_or_equal = 2 <= 2
equal = 'a' == 'a'
not_equal = 'a' != 'b'

print(greater, greater_or_equal, less, less_or_equal, equal, not_equal)
```

## 08.05 Key Points
- Python relies on indentation to define code blocks.
- The if-elif-else structure is essential for decision-making in programs.
- Use comparison operators to evaluate conditions effectively.