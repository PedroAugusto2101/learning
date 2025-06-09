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

### 05.00.04 Cost Function and Vectorization

- The cost function for multiple linear regression is written as J(W, b), where W is the parameter vector and b is the bias.
- Instead of treating each w<sub>j</sub> separately, we use the vector W for all parameters.
- **Vectorization** allows operations on entire vectors or arrays at once, making code shorter, faster, and more readable.
- Libraries like NumPy provide optimized functions (such as `np.dot()`) for efficient vectorized operations, leveraging parallel hardware (CPUs, GPUs).

#### Example: Non-vectorized vs. Vectorized Implementation

```python
import numpy as np

# Parameters and features
W = np.array([0.1, 4, 10, -2])
X = np.array([1416, 3, 2, 40])
b = 80

# Non-vectorized (using a loop)
y_pred = 0
for j in range(len(W)):
    y_pred += W[j] * X[j]
y_pred += b
print(y_pred)

# Vectorized (using np.dot)
y_pred_vec = np.dot(W, X) + b
print(y_pred_vec)
```

- The vectorized version using `np.dot()` is both more concise and much faster, especially as the number of features increases.

#### Vectorized Parameter Updates

- Vectorization is also used to efficiently update model parameters during training, such as in gradient descent:

```python
# Non-vectorized update
for j in range(len(W)):
    W[j] = W[j] - 0.1 * d[j]

# Vectorized update
W = W - 0.1 * d
```

- Here, `d` is the vector of derivatives (gradients) for each parameter. The vectorized update applies the operation to all parameters simultaneously.

### 05.00.05 Gradient Descent for Multiple Linear Regression

- Gradient descent is used to minimize the cost function J(W, b) and find optimal parameters.
- For each parameter w<sub>j</sub>, the update rule is:

```
w_j := w_j - α * ∂J/∂w_j
```

- For the bias term b:

```
b := b - α * ∂J/∂b
```

- In vectorized form, all weights can be updated together:

```
W := W - α * ∇_W J(W, b)
b := b - α * ∂J/∂b
```

- The error term (prediction minus target) is still central to the update, but now W and X are vectors, and updates are performed for all features simultaneously.

### 05.00.06 What is np.dot()?

- `np.dot()` is a NumPy function that computes the dot product of two vectors (or matrices).
- For vectors, it multiplies corresponding elements and sums the results, matching the mathematical definition of the dot product.
- Example: `np.dot([a, b, c], [x, y, z])` computes `a*x + b*y + c*z`.

### 05.00.07 Vectorization in NumPy

- In NumPy, vectorization means using array operations that apply to entire arrays or vectors at once, without explicit Python loops.
- NumPy arrays are stored in contiguous memory and NumPy functions are implemented in optimized C code, allowing for fast execution.
- Example: `W - 0.1 * d` subtracts `0.1 * d[j]` from each `W[j]` in parallel.
- Vectorized operations are not only more concise but also take advantage of hardware acceleration, making them essential for efficient scientific computing and machine learning.

### 05.00.08 Alternative: The Normal Equation

- Besides gradient descent, another method to solve for W and b in linear regression is the **normal equation**.
- The normal equation uses linear algebra to directly compute the optimal parameters without iterative updates.
- It is rarely implemented manually; mature machine learning libraries may use it internally for linear regression.
- Disadvantages:
  - Does not generalize to other algorithms (e.g., logistic regression, neural networks).
  - Becomes slow and impractical for large numbers of features.
- For most practical purposes, gradient descent is preferred for its flexibility and scalability.

### 05.00.09 Relation Between Vectorization and Embedding in LLMs

- **Vectorization** refers to performing operations on entire vectors or arrays at once for computational efficiency.
- **Embeddings** in the context of Large Language Models (LLMs) are vector representations of words, sentences, or other data. Each embedding is a vector in a high-dimensional space.
- Vectorization is used to efficiently compute with these embeddings, such as calculating similarities (dot products) or updating parameters during training.
- In summary, vectorization is a computational technique, while embeddings are data representations; vectorization enables fast operations on embeddings and other vectors in LLMs.

### 05.00.10 Terminology

- This model is called **multiple linear regression** (not multivariate regression, which refers to a different concept).
- The case with one feature is called **univariate regression**.

### 05.00.11 Next Steps

- To efficiently implement multiple linear regression and other machine learning algorithms, always prefer vectorized operations when possible, leveraging libraries like NumPy and hardware acceleration from CPUs and GPUs.
- Practice using NumPy for vectorized operations, as it is a foundational skill for modern machine learning.
