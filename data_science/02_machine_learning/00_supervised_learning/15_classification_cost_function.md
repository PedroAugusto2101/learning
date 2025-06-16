# 15. Cost Functions in Classification

## 15.00 Introduction to Cost Functions in Logistic Regression

- The cost function measures how well a specific set of parameters fits the training data, guiding the selection of better parameters.
- In logistic regression, the choice of cost function is crucial for effective learning.
- The goal is to find parameters \( w \) and \( b \) that minimize the cost function \( J(w, b) \), typically using gradient descent.

## 15.01 Squared Error Cost Function and Its Limitations

- In linear regression, the squared error cost function is commonly used:

  ```
  math
  J(w, b) = \frac{1}{m} \sum_{i=1}^{m} \frac{1}{2} (f(x^{(i)}) - y^{(i)})^2
  ```

- This function is convex for linear regression, allowing gradient descent to reliably find the global minimum.
- However, when applied to logistic regression, where

  ```
  math
  f(x) = \frac{1}{1 + e^{-(w \cdot x + b)}}
  ```

  the squared error cost function becomes non-convex, resulting in many local minima and making optimization unreliable.

## 15.02 Logistic Loss Function (Cross-Entropy Loss)

- To address this, logistic regression uses the **logistic loss** or **cross-entropy loss** as its cost function.
- For a single training example, the loss function is defined as:

  ```
  math
  L(f(x), y) =
    \begin{cases}
      -\log(f(x)), & \text{if } y = 1 \\
      -\log(1 - f(x)), & \text{if } y = 0
    \end{cases}
  ```

### 15.02.01 Intuition Behind the Logistic Loss

- If the true label \( y = 1 \):
  - The loss is small when \( f(x) \) (the predicted probability) is close to 1.
  - The loss increases rapidly as \( f(x) \) moves away from 1, strongly penalizing incorrect predictions.
- If the true label \( y = 0 \):
  - The loss is small when \( f(x) \) is close to 0.
  - The loss increases rapidly as \( f(x) \) approaches 1, penalizing confident but incorrect predictions.

### 15.02.02 Properties of the Logistic Loss

- The logistic loss function ensures that the overall cost function is **convex**, allowing gradient descent to reliably find the global minimum.
- The cost for the entire training set is the average loss over all examples:

  ```
  math
  J(w, b) = \frac{1}{m} \sum_{i=1}^{m} L(f(x^{(i)}), y^{(i)})
  ```

- Minimizing this cost function leads to optimal parameters \( w \) and \( b \) for logistic regression.

## 15.03 Gradient Descent for Logistic Regression

- Gradient descent is used to minimize the cost function \( J(w, b) \).
- The update rules for the parameters are:

  ```
  math
  w_j := w_j - \alpha \frac{\partial J(w, b)}{\partial w_j}
  b := b - \alpha \frac{\partial J(w, b)}{\partial b}
  ```

  where \( \alpha \) is the learning rate.

- The derivatives are:

  ```
  math
  \frac{\partial J(w, b)}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)}) x_j^{(i)}
  ```

  ```
  math
  \frac{\partial J(w, b)}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)})
  ```

- These updates are performed simultaneously for all parameters.
- Although the update equations look similar to those in linear regression, the key difference is that \( f(x) \) is the sigmoid function in logistic regression, not a linear function.

### 15.03.01 Practical Considerations

- **Feature Scaling**: Scaling features to similar ranges (e.g., between -1 and 1) can help gradient descent converge faster, just as in linear regression.
- **Vectorization**: Implementing gradient descent using vectorized operations can significantly speed up computation.
- **Monitoring Convergence**: You can monitor the cost function during training to ensure that gradient descent is converging properly.

### 15.03.02 Using Libraries

- Libraries like scikit-learn provide efficient implementations of logistic regression, widely used in industry.

## 15.04 Summary of Cost Functions in Classification

- **Squared Error Cost Function**: Suitable for linear regression, but not for logistic regression due to non-convexity.
- **Logistic Loss (Cross-Entropy Loss)**: The standard cost function for logistic regression, ensuring convexity and effective optimization.

### 15.04.01 Key Takeaways

- The cost function is central to training classification models.
- Logistic regression uses the cross-entropy (logistic) loss to ensure convexity and reliable optimization.
- Proper choice of cost function enables gradient descent to find the best parameters for accurate predictions.
- Gradient descent for logistic regression involves specific update rules based on the sigmoid function.
- Feature scaling and vectorization are important practical techniques for efficient training.
- Tools like scikit-learn make it easy to apply
