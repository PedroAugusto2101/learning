# 02. COST FUNCTION

---

## 02.00 Introduction

- The **cost function** evaluates how well a model fits the training data.
- In linear regression, the model is defined as:

```python
f_wb(x) = w * x + b
```

- `w` and `b` are parameters (also called weights or coefficients) adjusted during training to improve model performance.
- The goal of training is to find values for `w` and `b` that minimize the cost function, leading to better predictions.

## 02.01 Parameter Influence

- `w` determines the **slope** of the line.
- `b` determines the **y-intercept**.
- Different combinations of `w` and `b` produce different model fits.
- The best model minimizes the difference between predicted and actual values.
  ![img](../../img/Screenshot%20from%202025-05-06%2007-35-03.png)

## 02.02 Cost Function Definition

### 02.02.01 Objective

- We want predicted values `ŷ(i)` to be as close as possible to actual values `y(i)` for all training examples `(x(i), y(i))`.
- The cost function measures **how far off** the predictions are from the real values.
- The objective of training is to **minimize** this difference.
  ![img](../../img/Captura%20de%20tela%202025-05-13%20180941.png)

### 02.02.02 Mean Squared Error (MSE)

- In linear regression, the cost function is the **Mean Squared Error**:

```python
J(w, b) = (1 / (2 * m)) * Σ (f_wb(x(i)) - y(i))²
```

Where:

- `m` is the number of training examples.
- `f_wb(x(i))` or `ŷ(i)` is the model prediction.
- `y(i)` is the true label.
- The division by 2 is for convenience when computing gradients.

### 02.02.03 Why Squared Error?

- Squaring ensures:
  - All errors are positive (prevents positive/negative cancellation).
  - Larger errors are penalized more heavily.
- This drives the model to reduce large deviations, focusing on improving its worst predictions.

### 02.02.04 Common Cost Functions by Task

| Task Type                 | Common Cost Function          | Description                                                   |
| ------------------------- | ----------------------------- | ------------------------------------------------------------- |
| Regression                | **Mean Squared Error (MSE)**  | Penalizes large errors more.                                  |
| Binary Classification     | **Binary Cross-Entropy**      | Measures difference between predicted and real binary labels. |
| Multiclass Classification | **Categorical Cross-Entropy** | Similar to binary but for multiple classes.                   |

## 02.03 Cost Function in ML Context

- MSE is widely used for **regression** tasks.
- Other ML problems (like classification) use different cost functions depending on the task.
- Regardless of the algorithm, the guiding principle remains:
  - **Minimize the cost function to improve prediction accuracy**.
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
