# **Classification Algorithms**

## **Introduction**

- A **classification** algorithm predicts a discrete label or category.
- **Supervised learning** task: model learns from input-output pairs (X → Y) where Y is a **finite set of classes**.
- Unlike regression (which predicts continuous values), classification predicts a **limited and fixed set of categories**.
- **Examples of classification tasks**:
  - Email filtering: spam (1) or not spam (0).
  - Predicting customer default: yes (1) or no (0).
  - Breast cancer diagnosis: malignant (1) or benign (0).
  - Voice recognition, image recognition, translation, etc.
  - Some tasks may have **more than two possible classes** (multi-class classification).

| Input (X)          | Output (Y)       | Application        |
| ------------------ | ---------------- | ------------------ |
| Email text         | Spam? (0/1)      | Spam filter        |
| Tumor size & shape | Malignant? (0/1) | Cancer detection   |
| Image              | Defective? (0/1) | Visual inspection  |
| Audio              | Transcription    | Speech recognition |
| Ad & user info     | Clicked? (0/1)   | Online advertising |
| Image & radar      | Car positions    | Autonomous driving |

## **Difference from Linear Regression**

- **Regression** predicts a number in a continuous range (e.g. house price).
- **Classification** predicts from a **small and finite set of possible outputs**.
- Despite the name, **logistic regression is used for classification**, not regression.
- **Binary classification** convention: classes represented as **0** and **1**.
- Linear regression is not suitable for classification, as it outputs values beyond the [0,1] range.

![img](../../img/Screenshot%20from%202025-04-01%2016-34-46.png)

## **Logistic Function (Sigmoid)**

- The **logistic (sigmoid) function** maps values to a range between **0 and 1**.
- Applied to the output of linear regression to generate **probabilities** for classification.

![img](../../img/Screenshot%20from%202025-04-01%2016-36-46.png)

### **Sigmoid Output Interpretation**

- The **sigmoid output** represents the **probability** of the input belonging to class **1**.
- For a new input, if the output is **> 0.5**, we predict class **1**; otherwise, class **0**.
- This approach enables **probabilistic classification**.

## **Multivariate Classification**

- Classification models can handle **multiple input features** (not just one).
- A decision boundary is learned, separating the space into regions of different class predictions.

![img](../../img/Screenshot%20from%202025-04-29%2007-35-26.png)

## **Confusion Matrix**

- Common evaluation tool for classification models.
- Especially used in **binary classification**.

![img](../../img/Screenshot%20from%202025-04-01%2016-41-46.png)
![img](../../img/Screenshot%20from%202025-04-03%2010-56-46.png)

| Actual \ Predicted | No (0) | Yes (1) |
| ------------------ | ------ | ------- |
| **No (0)**         | TN     | FP      |
| **Yes (1)**        | FN     | TP      |

### **Terminology**

- **TP (True Positive)**: Model correctly predicts positive class.
- **TN (True Negative)**: Model correctly predicts negative class.
- **FP (False Positive)**: Model incorrectly predicts positive.
- **FN (False Negative)**: Model incorrectly predicts negative.

## **Performance Metrics**

![img](../../img/Screenshot%20from%202025-04-01%2016-43-46.png)

- **Accuracy**:

  - Proportion of correct predictions.
  - Formula: **(TP + TN) / Total**
  - Example: **150 / 165 = 91%**

- **Misclassification Rate**:
  - Proportion of incorrect predictions.
  - Formula: **(FP + FN) / Total**
  - Example: **15 / 165 = 9%**
