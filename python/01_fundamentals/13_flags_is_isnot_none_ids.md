# 13. Flags, is/is not, None, and IDs

## 13.00 What Are Flags and None?

### Flags
- **Flags** are used to mark or indicate a specific state or location in the code.
- They are often implemented as variables with `True`, `False`, or other status values.

### None
- `None` represents **no value** or **the absence of a value**.
- It is frequently used to initialize variables or indicate that something is undefined.

---

## 13.01 is and is not Operators
- The `is` operator checks if two objects are the **same object** in memory (identity comparison).
- The `is not` operator checks if two objects are **not the same**.

- Example:
    ```python
    if passou_no_if is None:
        print('Did not pass the if')
    else:
        print('Passed the if')
    ```

---

## 13.02 id Function
- The `id()` function returns the **unique identity** of an object in memory.
- This can be useful for debugging or confirming whether two variables reference the same object.

---

## 13.03 Best Practices
- **Declare variables before using them**, especially in conditional blocks, to avoid runtime errors if the variable is not created within the block.
- Example:
    ```python
    condicao = False
    passou_no_if = None  # Pre-declare variable

    if condicao:
        passou_no_if = True
        print('Do something')
    else:
        print('Do not do something')
    ```

---

## 13.04 Key Points
- Flags are useful for marking states or conditions in the code.
- `None` is a placeholder indicating no value.
- Use `is` and `is not` for identity comparisons.
- The `id()` function helps check object identity.
- Pre-declaring variables avoids potential issues in conditional logic.
