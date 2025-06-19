# 16. UNDERFITTING AND OVERFITTING IN MACHINE LEARNING

## 16.00 Introduction

- Understanding the challenges of underfitting and overfitting in machine learning models.

### What are Underfitting and Overfitting?

- **Underfitting** occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance even on the training set (**high bias**).
- **Overfitting** happens when a model is too complex and fits the training data too closely, including noise and outliers, leading to poor generalization on new, unseen data (**high variance**).

## 16.01 Examples in Regression

### Linear Regression Example

- **Scenario:** Predicting housing prices based on house size.
- **Underfitting:** Using a simple linear model (straight line) fails to capture the true relationship if the data is more complex. The model cannot fit the training data well, indicating high bias.
- **Just Right:** Introducing a quadratic model (using features like x and x²) allows the model to fit the data better and generalize well to new examples.
- **Overfitting:** Using a fourth-order polynomial (features x, x², x³, x⁴) can fit the training data perfectly, but the resulting curve is overly complex and does not generalize well to new data, indicating high variance.

## 16.02 Generalization and Model Selection

### Generalization

- The goal in machine learning is to build models that perform well not only on the training data but also on new, unseen examples. This property is called **generalization**.

### Bias-Variance Tradeoff

- **High Bias (Underfitting):** Model is too simple, ignores relevant patterns.
- **High Variance (Overfitting):** Model is too complex, captures noise as if it were a pattern.
- The ideal model achieves a balance, fitting the data well without being too rigid or too flexible.

## 16.03 Analogy: Goldilocks Principle

- The process of finding the right model is similar to the Goldilocks story: one model is too simple (underfitting), another is too complex (overfitting), and the best model is "just right," balancing bias and variance.

## 16.04 Examples in Classification

### Logistic Regression Example

- **Scenario:** Classifying tumors as malignant or benign using features like tumor size and patient age.
- **Underfitting:** A simple logistic regression model with a linear decision boundary may not separate the classes well (high bias).
- **Just Right:** Adding quadratic features allows for a more flexible decision boundary (e.g., an ellipse), improving classification and generalization.
- **Overfitting:** Using many high-order polynomial features creates a highly complex decision boundary that fits the training data perfectly but fails to generalize (high variance).

## 16.05 Addressing Underfitting and Overfitting

### Strategies to Address Overfitting

1. **Collect More Training Data**

   - Increasing the size of the training set helps the model learn a less complex, more generalizable function, especially when using complex models with many features.
   - More data reduces the risk of the model fitting noise or outliers.

2. **Feature Selection**

   - Reducing the number of features (e.g., using only the most relevant ones) can help prevent overfitting, especially when the dataset is small relative to the number of features.
   - Feature selection can be done manually using domain knowledge or automatically using algorithms.
   - Note: Removing features may discard useful information, so this method should be used thoughtfully.

3. **Regularization**
   - Regularization techniques penalize large parameter values, encouraging the model to keep weights small and thus reducing the influence of less relevant features.
   - Regularization allows you to keep all features but limits their impact, helping to prevent overfitting without discarding information.
   - Typically, regularization is applied to the weights (w₁, w₂, ..., wₙ), not necessarily to the bias term (b).
   - Regularization is a widely used and effective method, especially in models like linear regression, logistic regression, and neural networks.

### 16.05.01 How Regularization Works

- Regularization modifies the cost function by adding a penalty term to discourage large weights.
- For linear regression, the regularized cost function is:

  ```
  math
  J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)})^2 + \frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2
  ```

  - The first term measures the fit to the training data (mean squared error).
  - The second term is the regularization term, penalizing large weights.
  - λ (lambda) is the regularization parameter that controls the trade-off between fitting the data and keeping weights small.

- If λ = 0, there is no regularization, and the model may overfit.
- If λ is very large, the weights are forced to be close to zero, leading to underfitting.
- The best results are achieved with a λ value that is "just right," balancing both objectives.

- By convention, regularization is usually applied only to the weights (w), not the bias (b), as penalizing b has little effect in practice.

### 16.05.02 Gradient Descent with Regularization

- To minimize the regularized cost function, gradient descent is used with modified update rules.
- For each weight \( w_j \):

  ```
  math
  w_j := w_j - \alpha \left( \frac{1}{m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)}) x_j^{(i)} + \frac{\lambda}{m} w_j \right)
  ```

- For the bias term \( b \):

  ```
  math
  b := b - \alpha \left( \frac{1}{m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)}) \right)
  ```

- The regularization term \( \frac{\lambda}{m} w_j \) in the update for \( w_j \) causes the weights to shrink slightly on each iteration, discouraging large values and reducing overfitting.
- The update for \( b \) remains unchanged, as regularization is not applied to the bias.

### 16.05.03 Intuition Behind Regularization Updates

- On each iteration, the weights are multiplied by a factor slightly less than 1, effectively shrinking them.
- This shrinkage helps prevent the model from fitting noise in the data, promoting simpler and more generalizable models.

### 16.05.04 Practical Implications

- Regularization is especially useful when there are many features and it is unclear which are most important.
- It allows the use of all features while reducing the risk of overfitting.
- The value of λ should be chosen carefully, often through model selection techniques.

### Interactive Learning

- Labs and interactive tools can help visualize overfitting and experiment with different strategies, such as adding data or selecting features, to build intuition about these concepts.

## 16.06 Summary

- **Underfitting (High Bias):** Model too simple, poor fit to training data.
- **Overfitting (High Variance):** Model too complex, fits training data too closely, poor generalization.
- **Generalization:** The ability of a model to perform well on new, unseen data.
- **Addressing Overfitting:** Collect more data, select relevant features, or use regularization to control model complexity.
- **Regularization:** Adds a penalty to the cost function to keep weights small and reduce overfitting. Gradient descent with regularization shrinks weights on each iteration.
- **Next Steps:** Learn how to apply regularization to logistic regression and further improve model performance.
