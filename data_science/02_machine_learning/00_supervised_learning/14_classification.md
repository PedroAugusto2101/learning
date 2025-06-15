# 03. Classification and Logistic Regression

## 03.00 Introduction to Classification

- Classification vs. Regression

Classification is a type of supervised learning where the output variable, \( y \), can only take on one of a small set of possible values, rather than any value in an infinite range as in regression. Unlike linear regression, which predicts continuous numbers, classification predicts discrete categories.

### 03.00.01 Examples of Classification Problems

- Spam detection: Is an email spam? (Yes/No)
- Fraud detection: Is a financial transaction fraudulent? (Yes/No)
- Medical diagnosis: Is a tumor malignant? (Yes/No)

In all these cases, the output variable \( y \) can only be one of two possible values.

## 03.01 Binary Classification

- Definition and Terminology

Binary classification refers to problems where there are only two possible output classes or categories. The terms "class" and "category" are used interchangeably.

### 03.01.01 Labeling Conventions

- Classes are often labeled as:
  - No/Yes
  - False/True
  - 0/1 (common in computer science, with 0 = False, 1 = True)

The class labeled as 0 is called the **negative class**, and the class labeled as 1 is called the **positive class**. For example, in spam detection, a non-spam email is a negative example (0), while a spam email is a positive example (1). These labels do not imply good or bad, but rather the absence (0) or presence (1) of a property.

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

- Logistic regression is designed for classification, not regression, despite its name.
- It always outputs values between 0 and 1, making it suitable for binary classification.
- Logistic regression avoids the problems seen with linear regression, such as inappropriate shifting of the decision boundary.

### 03.03.01 Why Use Logistic Regression?

- Ensures output is always between 0 and 1.
- Provides a clear probabilistic interpretation for classification.
- Widely used for binary classification problems.

## 03.04 Key Takeaways

- Classification predicts discrete categories, not continuous values.
- Binary classification deals with two possible classes, often labeled 0 (negative) and 1 (positive).
- Linear regression is not suitable for classification due to its output range and sensitivity to outliers.
- Logistic regression is the preferred algorithm for binary classification, providing stable and interpretable results.
