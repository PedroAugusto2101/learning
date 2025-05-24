# 04. GRADIENT DESCENT

## 04.00 Introduction to Gradient Descent

Gradient Descent is a fundamental optimization algorithm used to minimize any differentiable function, not just cost functions in linear regression. Its versatility allows it to be applied to a wide range of problems, including those with multiple parameters and complex cost functions.

- **General Applicability:** Gradient Descent can minimize functions with two or more parameters, making it suitable for various machine learning models.
- **Initial Assumptions:** The algorithm starts with initial guesses for the parameters (e.g., weights `w` and bias `b`). In linear regression, these are often set to zero, as the starting point does not significantly affect convergence.
- **Iterative Process:** Parameters are updated iteratively, moving towards values that minimize the cost function `J`. The process continues until `J` reaches its minimum value, which may not be unique—some functions have multiple minima.

## 04.01 Gradient Descent Algorithm

Gradient Descent works by repeatedly adjusting parameters in the direction that most rapidly decreases the cost function. This direction is given by the negative of the gradient (or derivative, for single-parameter cases).

- **Parameter Update:** At each iteration, parameters such as `w` are updated to reduce the value of the cost function `J`.
- **Learning Rate (`α`):** The update rule involves subtracting a fraction of the gradient from the current parameter value. This fraction is controlled by the learning rate `α`, a small positive number typically between 0 and 1.
  - If `α` is too large, the algorithm may overshoot the minimum, causing divergence.
  - If `α` is too small, convergence will be slow.
- **Derivative/Gradient Term:** The gradient (or derivative) of the cost function with respect to each parameter indicates the direction and rate of the steepest ascent. By moving in the opposite direction, we descend towards the minimum.
  - For a single parameter `w`, the update is:  
    `w := w - α * dJ/dw`
  - The derivative at a point is the slope of the tangent to the cost function at that point. If the slope is positive, `w` decreases; if negative, `w` increases—both moving towards the minimum.
- **Convergence:** The algorithm repeats the update steps until convergence, meaning the parameter values change negligibly with further iterations.
- **Simultaneous Updates:** For functions with multiple parameters (e.g., `w` and `b`), all parameters are updated simultaneously at each iteration.

```python
# Example: Gradient Descent for Linear Regression

# Initialize parameters
w = 0
b = 0
alpha = 0.01  # Learning rate

for i in range(num_iterations):
    # Compute gradients
    dw = compute_derivative_w(w, b, X, y)
    db = compute_derivative_b(w, b, X, y)

    # Update parameters simultaneously
    w = w - alpha * dw
    b = b - alpha * db
```

### 04.01.01 Intuition Behind the Derivative

- The derivative at a point on the cost function represents the slope of the tangent line at that point.
  - **Positive Slope:** If the derivative is positive, decreasing `w` moves you toward the minimum.
  - **Negative Slope:** If the derivative is negative, increasing `w` moves you toward the minimum.
- This mechanism ensures that each update step moves the parameter closer to the minimum of the cost function.

### 04.01.02 Key Considerations

- **Multiple Minima:** Some cost functions may have several local minima; Gradient Descent may converge to any of them depending on the initial values.
- **Choice of Learning Rate:** Selecting an appropriate learning rate is crucial for efficient and stable convergence.
- **Stopping Criteria:** Common criteria include a maximum number of iterations or when the change in cost function value falls below a threshold.

## 04.02 Summary

Gradient Descent is an iterative algorithm for finding parameter values (`w`, `b`, etc.) that minimize a cost function `J`. By leveraging the direction and magnitude of the gradient, and controlling the step size with the learning rate, it efficiently navigates the parameter space toward a minimum, making it a cornerstone of modern machine learning optimization.
