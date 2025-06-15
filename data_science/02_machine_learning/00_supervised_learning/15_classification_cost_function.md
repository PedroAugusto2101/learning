# 15. Cost Functions in Classification

## 15.00 Introduction to Cost Functions in Logistic Regression

- The cost function measures how well a specific set of parameters fits the training data, guiding the selection of better parameters.
- In logistic regression, the choice of cost function is crucial for effective learning.

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

- To address this, logistic regression uses a different cost function, known as the **logistic loss** or **cross-entropy loss**.
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

## 15.03 Summary of Cost Functions in Classification

- **Squared Error Cost Function**: Suitable for linear regression, but not for logistic regression due to non-convexity.
- **Logistic Loss (Cross-Entropy Loss)**: The standard cost function for logistic regression, ensuring convexity and effective optimization.

### 15.03.01 Practical Implications

- Using the correct cost function is essential for the success of logistic regression.
- The logistic loss penalizes incorrect and overconfident predictions, guiding the model to output probabilities that match the true labels.

## 15.04 Key Takeaways

- The cost function is central to training classification models.
- Logistic regression uses the cross-entropy (logistic) loss to ensure convexity and reliable optimization.
- Proper choice of cost function enables gradient descent to find the best parameters for accurate
