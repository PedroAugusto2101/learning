# Principal Component Analysis (PCA)

## Overview

- **PCA** (Principal Component Analysis) is an **unsupervised statistical method**.
- It examines relationships between multiple variables to identify **underlying structures**.
- Also known as **factor analysis**.
- While **regression** finds the best **fitting line**, **PCA** determines the best **orthogonal set of lines** to fit the data.

## Key Concepts

- **Orthogonality** means **perpendicular**.
- We search for **perpendicular axes** in an **n-dimensional space**.
- **n-dimensional space**:
  - The dataset has as many **dimensions as variables**.
  - A dataset with **4 variables** has **4 dimensions**.

## PCA in Action

- Consider data plotted along the **x and y axes**:
  - The **best-fitting line** captures the relationship between the two variables.

![image.png](../img/Screenshot%20from%202025-04-03%2016-26-46.png)

- We add a **perpendicular (orthogonal) line**.
- These lines represent the **principal components**.

![image.png](../img/Screenshot%20from%202025-04-03%2016-27-46.png)

## Principal Components

- **Principal components (PCs)** are **linear transformations** of the original variables.
- The first component captures the **greatest variance** in the dataset.
- The second component captures the **next largest variance**, and so on.
- This allows **dimensionality reduction** while preserving important information.

### Properties:

- **Components are uncorrelated** (orthogonal to each other).
- Example:
  - **First component** explains **70%** of the variance.
  - **Second component** explains **28%**.
  - **2% remains unexplained**.

## Why Use PCA?

- In datasets with **many variables**, PCA compresses the variance into **fewer components**.
- Helps in **data visualization, feature selection, and noise reduction**.
- **Challenge:** Interpreting the principal components correctly.
