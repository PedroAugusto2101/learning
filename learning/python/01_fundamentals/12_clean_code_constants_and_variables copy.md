# 12. CONSTANTS, VARIABLES, AND CLEAN CODE

## 12.00 What Are Constants and Variables?

### Constants
- Constants are values that **do not change** during the execution of a program.
- In Python, constants are usually written in **uppercase** to distinguish them from variables.
- Example:
  ```python
  RADAR_1 = 60  # Maximum speed for radar 1
  LOCAL_1 = 100  # Location of radar 1
  RADAR_RANGE = 1  # Range of the radar
  ```
- **Constants** are used to define fixed values that represent settings or configurations, making the code more readable and easier to maintain.
### Variables
- Variables store data that **may change** during the program's execution.

- Example:

    ```python
    velocidade = 61  # Current speed of the car
    local_carro = 100  # Current location of the car
    ```
- **Variables** are used to store data that the program will use to perform calculations or make decisions.
---
## 12.01 Clean Code Practices
### Reducing Complexity
- Having **many conditions in the same `if` statement** can make the code difficult to read and maintain.

- Example of bad practice:

    ```python
    carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    ```
- This can be simplified by breaking it into smaller, more readable conditions:

    ```python
    radar_range_lower = LOCAL_1 - RADAR_RANGE
    radar_range_upper = LOCAL_1 + RADAR_RANGE
    carro_passou_radar_1 = local_carro >= radar_range_lower and local_carro <= radar_range_upper
    ``` 

- **Refactoring complex conditions** makes the code easier to understand and debug.

### Avoiding Repetition
- The code contains **repeated logic**, especially when checking conditions multiple times:

    ```python
    if vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')

    if carro_passou_radar_1:
        print('Carro passou radar 1')

    if carro_multado_radar_1:
        print('Carro multado em radar 1')
    ```
- Instead of repeating similar `if` statements, you can group related checks together and output all the results at once:

    ```python
    if carro_multado_radar_1:
        print('Carro multado em radar 1')
    elif carro_passou_radar_1:
        print('Carro passou radar 1')
    elif vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')
    ```
---
### 12.02 Simplifying Code with Variables
- To simplify the code and enhance readability, it is a good practice to store the results of calculations or conditions in variables.
- This reduces the number of operations performed in the `if` statements and makes the code more understandable.

- Example:

    ```python
    carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    vel_carro_pass_radar_1 = velocidade > RADAR_1
    # Combine both checks in a meaningful variable
    carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1
    ```

This makes the condition checking cleaner and easier to maintain, as each logic step is separated into its own meaningful variable.

---
### 12.03 Key Points
- **Constants** are values that do not change and should be written in uppercase for clarity.
- **Variables** hold data that can change during execution and should be named clearly based on their purpose.
- Reducing **complex conditions** and **repeated logic** improves readability and maintainability.
- **Code refactoring** with smaller, meaningful variables reduces complexity and enhances code clarity.
- **Group related logic** to minimize redundant checks and improve the flow of the code.