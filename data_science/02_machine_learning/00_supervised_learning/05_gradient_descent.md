# 04. GRADIENT DESCENT

## 04.00 Introduction to Gradient Descent

Gradient Descent is a fundamental optimization algorithm used to minimize any differentiable function, not just cost functions in linear regression. Its versatility allows it to be applied to a wide range of problems, including those with multiple parameters and complex cost functions.

- **General Applicability:** Gradient Descent can minimize functions with two or more parameters, making it suitable for various machine learning models.
- **Initial Assumptions:** The algorithm starts with initial guesses for the parameters (e.g., weights `w` and bias `b`). In linear regression, these are often set to zero, as the starting point does not significantly affect convergence.
- **Iterative Process:** Parameters are updated iteratively, moving towards values that minimize the cost function `J`. The process continues until `J` reaches its minimum value, which may not be unique—some functions have multiple minima.

## 04.01 Linear Regression and Cost Function

In linear regression, the model predicts:

$$
f_{w,b}(x^{(i)}) = w x^{(i)} + b
$$

The goal is to fit the parameters $w$ and $b$ by minimizing the cost function, which measures the average squared error between predictions and actual values:

$$
J(w, b) = \frac{1}{2m} \sum_{i=0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2
$$

## 04.02 Gradient Descent Algorithm

Gradient Descent works by repeatedly adjusting parameters in the direction that most rapidly decreases the cost function. This direction is given by the negative of the gradient (or derivative, for single-parameter cases).

- **Parameter Update:** At each iteration, parameters such as `w` and `b` are updated to reduce the value of the cost function `J`.
- **Learning Rate (`α`):** The update rule involves subtracting a fraction of the gradient from the current parameter value. This fraction is controlled by the learning rate `α`, a small positive number typically between 0 and 1.
  - If `α` is too large, the algorithm may overshoot the minimum, causing divergence.
  - If `α` is too small, convergence will be very slow, as the algorithm takes tiny steps toward the minimum.
- **Simultaneous Updates:** The partial derivatives for all parameters are calculated before any parameter is updated, ensuring a consistent update step.

The update rules are:

$$
\begin{align*}
w &:= w - \alpha \frac{\partial J(w, b)}{\partial w} \\
b &:= b - \alpha \frac{\partial J(w, b)}{\partial b}
\end{align*}
$$

Where the gradients are:

$$
\begin{align*}
\frac{\partial J(w, b)}{\partial w} &= \frac{1}{m} \sum_{i=0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)}) x^{(i)} \\
\frac{\partial J(w, b)}{\partial b} &= \frac{1}{m} \sum_{i=0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})
\end{align*}
$$

```python
# Example: Gradient Descent for Linear Regression

# Initialize parameters
w = 0
b = 0
alpha = 0.01  # Learning rate

for i in range(num_iterations):
    # Compute gradients
    dw = (1/m) * sum((w * X[i] + b - y[i]) * X[i] for i in range(m))
    db = (1/m) * sum((w * X[i] + b - y[i]) for i in range(m))

    # Update parameters simultaneously
    w = w - alpha * dw
    b = b - alpha * db
```

### 04.02.01 The Role of the Learning Rate

- **Too Small:** If the learning rate is extremely small (e.g., 0.0000001), gradient descent will take very tiny steps, requiring many iterations to approach the minimum. The algorithm will work, but convergence will be slow.
- **Too Large:** If the learning rate is too large, the algorithm may overshoot the minimum, jumping back and forth and potentially diverging—never settling at the minimum and possibly increasing the cost.
- **Automatic Step Adjustment:** As gradient descent approaches a minimum, the derivative naturally becomes smaller, causing the update steps to shrink even if the learning rate is fixed. This allows the algorithm to "settle" at the minimum.

### 04.02.02 Behavior at the Minimum

- When the parameter (e.g., `w`) reaches a local minimum, the derivative at that point is zero.
- The update rule becomes `w := w - α * 0`, so `w` remains unchanged.
- This means that once at a minimum, further steps of gradient descent do nothing, keeping the solution at the minimum.

### 04.02.03 Convexity and Global Minimum in Linear Regression

- **Convex Cost Function:** The squared error cost function for linear regression is convex (bowl-shaped), meaning it has only one global minimum and no local minima.
- **Implication:** Gradient Descent, with an appropriate learning rate, will always converge to the global minimum for linear regression, regardless of the initial values of `w` and `b`.

### 04.02.04 Batch Gradient Descent in Practice

- **Batch Gradient Descent:** In linear regression, the standard approach is batch gradient descent, where all training examples are used to compute the gradients at each update step. This ensures stable and consistent progress toward the minimum.
- **Visualization:** As gradient descent progresses, the parameters `w` and `b` follow a trajectory on the cost function surface, steadily decreasing the cost and improving the fit of the model to the data. The straight line fit becomes better with each step until the global minimum is reached.
- **Prediction:** Once the model is trained, it can be used to make predictions, such as estimating the price of a house given its size.

### 04.02.05 Other Variants

- There are other versions of gradient descent, such as stochastic and mini-batch gradient descent, which use subsets of the data at each update. However, for linear regression, batch gradient descent is commonly used.

### 04.02.06 Key Considerations

- **Multiple Minima:** Some cost functions may have several local minima; Gradient Descent may converge to any of them depending on the initial values. However, for linear regression with squared error, there is only one global minimum.
- **Choice of Learning Rate:** Selecting an appropriate learning rate is crucial for efficient and stable convergence.
- **Stopping Criteria:** Common criteria include a maximum number of iterations or when the change in cost function value falls below a threshold.

## 04.03 Monitoring Convergence

To determine if gradient descent is converging, plot the cost function $J$ (calculated on the training set) at each iteration. This plot, known as a learning curve, has the number of iterations on the horizontal axis and the cost $J$ on the vertical axis.

- **Expected Behavior:** If gradient descent is working properly, the cost $J$ should decrease after every iteration. If $J$ increases at any point, the learning rate $\alpha$ may be too large or there may be a bug in the code.
- **Convergence:** When the curve flattens out and $J$ no longer decreases significantly, gradient descent has likely converged.
- **Automatic Convergence Test:** You can set a small threshold $\epsilon$ (e.g., 0.001). If the decrease in $J$ between iterations is less than $\epsilon$, you can declare convergence. However, visually inspecting the learning curve is often more reliable.

- **Number of Iterations:** The number of iterations required for convergence varies widely depending on the application and data. It is difficult to predict in advance, so plotting the learning curve is a practical approach.

## 04.04 Practical Use of Gradient Descent in Machine Learning

- **Where is Gradient Descent Used?**  
  Gradient descent is used in many machine learning models to optimize parameters, especially in linear regression, logistic regression, neural networks, and deep learning. It is the core optimization method for models where the cost function is differentiable.

- **Is Gradient Descent already inside scikit-learn?**  
  Yes, most scikit-learn models that require optimization (such as linear regression, logistic regression, and neural networks) use gradient descent or its variants internally. When you call `.fit()` on these models, scikit-learn handles the optimization process for you. You do not need to implement gradient descent manually unless you want to customize or understand the algorithm in detail.

## 04.05 Summary

Gradient Descent is an iterative algorithm for finding parameter values (`w`, `b`, etc.) that minimize a cost function `J`. By leveraging the direction and magnitude of the gradient, and controlling the step size with the learning rate, it efficiently navigates the parameter space toward a minimum. For linear regression, the cost function is convex, guaranteeing convergence to the global minimum. Batch gradient descent uses all training data at each step, ensuring stable progress. The learning rate must be chosen carefully: too small leads to slow progress, too large can cause divergence. Monitoring the learning curve helps verify convergence. Most modern machine learning libraries, like scikit-learn, implement gradient descent internally, making it easy
