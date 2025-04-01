# Bias-Variance Tradeoff

- A fundamental concept for understanding model performance.
- Determines the point at which adding complexity only introduces noise.
- As model complexity increases:
  - **Training error** decreases.
  - **Test error** starts increasing.
- This leads to the well-known issue of **overfitting**.
  ![img](../img/Screenshot%20from%202025-04-01%2015-06-46.png)

## Key Concepts

- The **target center** represents the true value the model aims to predict.
- As we move away from it, predictions become less accurate.
- A model is **biased** when the average predictions are far from the target.
- **Variance** refers to the spread of prediction errors; higher variance means predictions are less consistent.
  ![img](../img/Screenshot%20from%202025-04-01%2015-12-46.png)

## Overfitting vs. Underfitting

- **Beginners' common mistake**: continuously increasing model complexity to fit training data perfectly.
- **Overfitting**:
  - The model learns noise instead of actual data patterns.
  - Performs well on training data but poorly on new, unseen data.
- **Underfitting**:
  - The model is too simple and fails to capture important patterns.

## Tradeoff Examples

- **Simple models** (e.g., linear regression):
  - Easy to interpret but may underfit, missing key relationships.
- **Complex models** (e.g., neural networks):
  - Can capture intricate patterns but risk overfitting.

## Key Problems

- **Underfitting**: The model is too simple and does not learn enough from data.
- **Overfitting**: The model is too complex and learns noise instead of true patterns.
  ![img](../img/Screenshot%20from%202025-04-01%2015-16-46.png)
