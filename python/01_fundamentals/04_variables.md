# 04. PYTHON VARIABLES

## 04.00 Introduction to Variables

### What are Variables?

- Variables are used to store data in the computer's memory.
- They act as labels that point to data values.
- Defined using the `=` operator, which assigns a value to a name.

### Naming Variables

- Follow **PEP 8** guidelines:
  - Start with a lowercase letter.
  - Use numbers and underscores (`_`) if needed.
  - Avoid special characters and reserved words.

### Examples of Variable Assignment

```python
# Variable assignment
name = 'Pedro'
age = 22
is_adult = age >= 18

# Display variable values
print('Name:', name, 'Age:', age)
print('Is an adult?', is_adult)
```

## IMPORTANT

### **Variables and Object Referencing in Python**

- In Python, variables store references to objects in memory, not the actual data.
- When one variable is assigned to another, they both reference the same object.
- Modifying the new variable affects the original object, as both variables point to the same location in memory.
- To avoid this, use the `.copy()` method to create a new, independent object.
