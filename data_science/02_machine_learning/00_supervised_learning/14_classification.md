# 03. Classification and Logistic Regression

## 03.00 Introduction to Classification

- Classification vs. Regression

Classification is a type of supervised learning where the output variable \( y \) can only take on one of a small set of possible values, unlike regression, which predicts continuous values. Classification predicts discrete categories, such as "spam" or "not spam," rather than any number in an infinite range.

### 03.00.01 Examples of Classification Problems

- Spam detection: Is an email spam? (Yes/No)
- Fraud detection: Is a financial transaction fraudulent? (Yes/No)
- Medical diagnosis: Is a tumor malignant? (Yes/No)

In all these cases, the output variable \( y \) can only be one of two possible values.

## 03.01 Binary Classification

- Definition and Terminology

Binary classification refers to problems with only two possible output classes or categories. The terms "class" and "category" are used interchangeably.

### 03.01.01 Labeling Conventions

- Classes are often labeled as:
  - No/Yes
  - False/True
  - 0/1 (common in computer science, with 0 = False, 1 = True)

The class labeled as 0 is called the **negative class**, and the class labeled as 1 is called the **positive class**. For example, in spam detection, a non-spam email is a negative example (0), while a spam email is a positive example (1). These labels indicate the absence (0) or presence (1) of a property, not good or bad.

### 03.01.02 Arbitrary Assignment of Labels

- The assignment of which class is 0 or 1 can be arbitrary and may vary depending on the problem or the engineer's choice.

## 03.02 Building a Classification Algorithm

- Example: Tumor Classification

Suppose we want to classify tumors as malignant (1) or benign (0). We can plot tumor size on the horizontal axis and the label \( y \) on the vertical axis.

### 03.02.01 Attempting Linear Regression for Classification

- Linear regression fits a straight line to the data and predicts continuous values, not just 0 or 1.
- To adapt linear regression for classification, we can set a threshold (e.g., 0.5):
  - If the model outputs a value below 0.5, predict \( y = 0 \) (benign).
  - If the model outputs a value equal to or above 0.5, predict \( y = 1 \) (malignant).

### 03.02.02 Problems with Linear Regression for Classification

- Adding an outlier (e.g., a new data point far to the right) can shift the best-fit line and the threshold, leading to incorrect classifications.
- The decision boundary (the threshold dividing the classes) can move undesirably due to such outliers.
- Linear regression can output values less than 0 or greater than 1, which are not valid class labels.

## 03.03 Logistic Regression: A Solution for Classification

Logistic regression is one of the most widely used algorithms for classification. Despite its name, it is used for classification, not regression.

### 03.03.01 The Sigmoid (Logistic) Function

- The core of logistic regression is the **Sigmoid function** (also called the logistic function), which maps any real-valued number to a value between 0 and 1.
- The Sigmoid function is defined as:

  ```
  math
  g(z) = 1 / (1 + e^{-z})
  ```

  where \( e \) is the mathematical constant (~2.718).

- The Sigmoid function produces an S-shaped curve. For large positive \( z \), \( g(z) \) approaches 1; for large negative \( z \), \( g(z) \) approaches 0; and for \( z = 0 \), \( g(z) = 0.5 \).

### 03.03.02 Logistic Regression Model

- Logistic regression combines a linear function and the Sigmoid function:

  ```
  math
  z = w \cdot x + b
  f(x) = g(z) = 1 / (1 + e^{-z})
  ```

- The model takes input features \( x \), computes \( z \) as a linear combination of the features, and then applies the Sigmoid function to output a value between 0 and 1.

### 03.03.03 Interpreting Logistic Regression Output

- The output of logistic regression, \( f(x) \), can be interpreted as the probability that the label \( y \) is 1 given the input \( x \).
- For example, if \( f(x) = 0.7 \), the model predicts a 70% chance that \( y = 1 \) (e.g., the tumor is malignant).
- Since \( y \) must be either 0 or 1, the probability that \( y = 0 \) is \( 1 - f(x) \). If the probability of \( y = 1 \) is 0.7, then the probability of \( y = 0 \) is 0.3.

- In notation, you may see:

  ```
  math
  f(x) = P(y = 1 \mid x; w, b)
  ```

  where \( w \) and \( b \) are model parameters.

### 03.03.04 From Probability to Prediction: Threshold and Decision Boundary

- To make a final prediction, a threshold is set (commonly 0.5):
  - If \( f(x) \geq 0.5 \), predict \( \hat{y} = 1 \).
  - If \( f(x) < 0.5 \), predict \( \hat{y} = 0 \).
- This threshold translates to the condition \( w \cdot x + b \geq 0 \) for predicting 1, and \( w \cdot x + b < 0 \) for predicting 0.

#### Decision Boundary

- The **decision boundary** is the set of points where \( w \cdot x + b = 0 \). It separates the feature space into regions where the model predicts different classes.
- For two features (\( x_1, x_2 \)), the decision boundary is a line (e.g., \( x_1 + x_2 = 3 \) if \( w_1 = 1, w_2 = 1, b = -3 \)).
- Points on one side of the boundary are classified as 1, and on the other side as 0.

#### Nonlinear Decision Boundaries

- By including polynomial features (e.g., \( x_1^2, x_2^2, x_1 x_2 \)), logistic regression can model more complex, nonlinear decision boundaries.
- For example, with \( z = x_1^2 + x_2^2 - 1 \), the decision boundary \( x_1^2 + x_2^2 = 1 \) is a circle.
- Higher-order polynomials allow for even more complex boundaries, such as ellipses or irregular shapes, enabling logistic regression to fit complex data distributions.

### 03.03.05 Practical Use and Applications

- Logistic regression is widely used in real-world applications, such as medical diagnosis and online advertising.
- It provides a clear probabilistic interpretation and stable decision boundaries, avoiding the pitfalls of linear regression for classification.
- The decision boundary can be visualized and interpreted, helping to understand how the model separates classes.

## 03.04 Key Takeaways

- Classification predicts discrete categories, not continuous values.
- Binary classification deals with two possible classes, often labeled 0 (negative) and 1 (positive).
- Linear regression is not suitable for classification due to its output range and sensitivity to outliers.
- Logistic regression uses the Sigmoid function to output probabilities between 0 and 1, making it ideal for binary classification.
- The output of logistic regression can be interpreted as the probability of the positive class.
- The decision boundary, defined by \( w \cdot x + b = 0 \), separates the feature space into regions for each class. With polynomial features, logistic regression can model complex, nonlinear
