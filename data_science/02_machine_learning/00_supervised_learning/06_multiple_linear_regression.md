# 05. MULTIPLE LINEAR REGRESSION

## 05.00 Introduction to Multiple Linear Regression

- Linear regression can be extended to use multiple features, making predictions more accurate and models more powerful.

### 05.00.01 Notation and Feature Representation

- Each feature is denoted as X<sub>j</sub>, where j = 1, 2, ..., n (n = number of features).
- For each training example i, the feature vector is X<sup>(i)</sup> = [X<sup>(i)</sup><sub>1</sub>, X<sup>(i)</sup><sub>2</sub>, ..., X<sup>(i)</sup><sub>n</sub>].
- Example: If X<sup>(2)</sup> = [1416, 3, 2, 40], then X<sup>(2)</sup><sub>3</sub> = 2 (number of floors in the second example).
  ![img](../../img/Captura%20de%20tela%202025-06-05%20122043.png)

### 05.00.02 Model Definition with Multiple Features

- The model for multiple features is:

```
f_w,b(X) = w₁X₁ + w₂X₂ + w₃X₃ + w₄X₄ + b
```

- Example for house price prediction:

```
f_w,b(X) = 0.1·X₁ + 4·X₂ + 10·X₃ - 2·X₄ + 80
```

- Interpretation of parameters:
  - b = 80: base price ($80,000)
  - 0.1: each additional square foot adds $100
  - 4: each additional bedroom adds $4,000
  - 10: each additional floor adds $10,000
  - -2: each additional year of age subtracts $2,000

### 05.00.03 Vector Notation and Dot Product

- To simplify, use vector notation:

  - W = [w₁, w₂, ..., wₙ] (parameter vector)
  - X = [X₁, X₂, ..., Xₙ] (feature vector)

- The model becomes:

```
f_w,b(X) = W · X + b
```

- The dot product (W · X) is calculated as:

```
W · X = w₁X₁ + w₂X₂ + ... + wₙXₙ
```

- This compact notation is equivalent to the expanded form and is widely used in machine learning.

### 05.00.04 Terminology

- This model is called **multiple linear regression** (not multivariate regression, which refers to a different concept).
- The case with one feature is called **univariate regression**.

### 05.00.05 Implementation Example

```python
import numpy as np

# Feature vector for one example
X = np.array([1416, 3, 2, 40])
# Parameter vector
W = np.array([0.1, 4, 10, -2])
# Bias term
b = 80

# Prediction
y_pred = np.dot(W, X) + b
print(y_pred)  # Output: predicted price
```

### 05.00.06 Next Steps

- To efficiently implement multiple linear regression, a technique called **vectorization** is used, which simplifies and accelerates computations.
