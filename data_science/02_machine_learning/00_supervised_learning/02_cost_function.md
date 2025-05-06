# 02. COST FUNCTION

## 02.00 Introduction

- The **cost function** evaluates how well a model fits the training data.
- In linear regression, the model is defined as:

```python
f_wb(x) = w * x + b
```

- `w` and `b` are parameters (also called weights or coefficients) adjusted during training to improve model performance.

## 02.01 Parameter Influence

- `w` determines the **slope** of the line.
- `b` determines the **y-intercept**.
- Choosing different values for `w` and `b` results in different model fits.
- The goal is to find the best combination such that the prediction line fits the data accurately.
  ![img](../../img/Screenshot%20from%202025-05-06%2007-35-03.png)

## 02.02 Cost Function Definition

### 02.02.01 Objective

- We want predicted values `ŷ(i)` to be as close as possible to actual values `y(i)` for all training examples `(x(i), y(i))`.

### 02.02.02 Mean Squared Error (MSE)

- The cost function used in linear regression is the **Mean Squared Error**:

```python
J(w, b) = (1 / (2 * m)) * Σ (f_wb(x(i)) - y(i))²
```

Where:

- `m` is the number of training examples.
- `f_wb(x(i))` or `ŷ(i)` is the model prediction.
- `y(i)` is the true label.

### 02.02.03 Why Squared Error?

- Squaring ensures:
  - All errors are positive (avoids cancellation).
  - Larger errors have a stronger penalty.
- This encourages the model to focus on reducing large deviations.

## 02.03 Cost Function in ML Context

- The MSE is widely used for **linear regression**.
- Other ML tasks (e.g., classification) use different cost functions (like cross-entropy).
- The core principle remains: **minimize the cost to improve accuracy**.
  ![img](../../img/Screenshot%20from%202025-05-06%2007-37-32.png)

```python
# Example: Compute MSE
def compute_cost(x, y, w, b):
    m = len(x)
    total_cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        total_cost += (f_wb - y[i])**2
    return total_cost / (2 * m)
```
